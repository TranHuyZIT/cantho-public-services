from langchain.docstore.document import Document
from langchain_core.prompts import PromptTemplate
from app_vars import AppVariables


class RAGFusion:
    template = """Bạn là một chatbot hỗ trợ sinh các câu hỏi đồng nghĩa dựa vào câu hỏi gốc. Hãy sinh ra 3 câu hỏi, phân cách bằng ký tự '\n' và không thêm bất kỳ ký tự nào khác ngoài câu hỏi.
    Câu hỏi gốc : {question}
    """
    prompt = PromptTemplate.from_template(template)

    llm_chain = prompt | AppVariables.llm 
    
    @staticmethod
    def reciprocal_rank_fusion(search_results_dict, k=25, limit=25):
        fused_scores = {}        
        for query, doc_scores in search_results_dict.items():
            for rank, (doc, score) in enumerate(sorted(doc_scores.items(), key=lambda x: x[1]['score'], reverse=True)):
                if doc not in fused_scores:
                    fused_scores[doc] = {
                        "rank": 0,
                        "metadata": score["metadata"]
                    }
                fused_scores[doc]["rank"] += 1 / (rank + k)

        reranked_results = sorted(fused_scores.items(), key=lambda x: x[1]['rank'], reverse=True)[:limit]
        reranked_results = [Document(page_content=doc[0], metadata=doc[1]["metadata"]) for doc in reranked_results]
        return reranked_results

    @staticmethod
    def generating_search_results(question):
        
        completion = RAGFusion.llm_chain.invoke(question)
        questions = completion.split("\n")
        processed_questions = []
        for question in questions:
            question = question.strip()
            question = question.replace('?','')
            if question != "":
                processed_questions.append(question)
    
        search_result_scores = {}
        for question in processed_questions:
            scored_docs = AppVariables.retrieve(question)
            result = {doc.page_content: {
                "score": score,
                "metadata": doc.metadata
            } for (doc, score) in scored_docs}
            search_result_scores[question] = result

        return search_result_scores
