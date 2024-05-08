from langchain.docstore.document import Document
from langchain_core.prompts import PromptTemplate
from rag.modules.app_vars import AppVariables
import re

class RAGFusion:
    template = """Bạn là một chatbot hỗ trợ sinh các câu hỏi đồng nghĩa dựa vào câu hỏi gốc về thủ tục hành chính. Hãy tuân thủ các nguyên tắc sau khi tạo ra HAI câu hỏi đồng nghĩa:
    - Hai câu hỏi phải sử dụng MỘT trong bốn các cụm từ sau: 'trình tự các bước', 'cách thức thực hiện', 'hồ sơ cần', 'cơ quan thực hiện', 'điều kiện thực hiện' .
    - Với những câu hỏi chung chung, hãy ưu tiên hỏi một câu về về 'trình tự các bước' .

    Hai câu hỏi phải được phân cách bằng ký tự '\n' . KHÔNG thêm bất kỳ ký tự nào khác ngoài hai câu hỏi được bạn tạo ra.
    Câu hỏi gốc : {question}
    """

    template2 = """Bạn là một chatbot hỗ trợ sinh làm rõ câu hỏi của người dùng về thủ tục hành chính. Dựa vào đoạn hội thoại dưới đây, hãy viết lại câu hỏi của người dùng ngắn gọn chứa tên thủ tục hành chính nếu được.
    KHÔNG thêm bất kỳ ký tự nào khác ngoài câu hỏi được bạn tạo ra.

    ------
    Đoạn hội thoại: {dialogue}
    
    ------
    Câu hỏi từ người dùng : {question}

    ------
    Câu hỏi viết lại: 
    """

    rewrite_chain = PromptTemplate.from_template(template2) | AppVariables.llm

    def rewrite_question(question, messages=[]):
        dialogue = "\n"
        for message in messages:
            dialogue += f"{message['role']}: {message['content']}\n"
        
        completion = RAGFusion.rewrite_chain.invoke({"question": question, "dialogue": dialogue})
        completion = RAGFusion.process_question(completion)
        return completion



    prompt = PromptTemplate.from_template(template)

    llm_chain = prompt | AppVariables.llm 
    
    @staticmethod
    def reciprocal_rank_fusion(search_results_dict, k=25):
        fused_scores = {}        
        for query, doc_scores in search_results_dict.items():
            for rank, (doc, score) in enumerate(sorted(doc_scores.items(), key=lambda x: x[1]['score'], reverse=True)):
                if doc not in fused_scores:
                    fused_scores[doc] = {
                        "rank": 0,
                        "metadata": score["metadata"]
                    }
                fused_scores[doc]["rank"] += 1 / (rank + k)

        reranked_results = sorted(fused_scores.items(), key=lambda x: x[1]['rank'], reverse=True)
        reranked_results = [Document(page_content=doc[0], metadata=doc[1]["metadata"]) for doc in reranked_results]
        return reranked_results

    @staticmethod
    def process_question(question):
        question = question.strip()
        question = question.split(":")[-1].strip()
        question = re.sub(r'^[^a-zA-Z]*', '', question)
        question = re.sub(r'\W+$', '', question)
        return question

    @staticmethod
    def generate_questions(question):
        completion = RAGFusion.llm_chain.invoke(question)
        questions = completion.split("\n")

        processed_questions = [ question ]
        for generated_question in questions:
            generated_question = RAGFusion.process_question(generated_question)
            if generated_question != "":
                processed_questions.append(generated_question)
        processed_questions = processed_questions[0:min(3, len(processed_questions))]
        return processed_questions

    @staticmethod
    def generating_search_results(question):
        processed_questions = RAGFusion.generate_questions(question)
        search_result_scores = {}
        for question in processed_questions:
            scored_docs = AppVariables.retrieve(question)
            result = {doc.page_content: {
                "score": score,
                "metadata": doc.metadata
            } for (doc, score) in scored_docs}
            search_result_scores[question] = result

        return processed_questions
    
    @staticmethod
    def retrieve_fusion_set(questions):
        search_result_scores = {}
        for question in questions:
            scored_docs = AppVariables.retrieve(question)
            result = {doc.page_content: {
                "score": score,
                "metadata": doc.metadata
            } for (doc, score) in scored_docs}
            search_result_scores[question] = result

        return search_result_scores