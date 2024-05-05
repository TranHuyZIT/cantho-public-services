from rag.modules.fusion import RAGFusion
from rag.modules.rerank import RAGRerank
from rag.modules.app_vars import AppVariables
import time

class RAGFacade:
    @staticmethod
    def generate_truth_answer(context):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Bạn là một tư vấn viên cho các dịch vụ công tại Cần Thơ Việt Nam, hãy trả lời lịch sự."},
                {"role": "system", "content": inputs},
                {"role": "user", "content": question}
            ],
            temperature=0
        )

    @staticmethod
    def retrieve(question, k=25):
        return AppVariables.retrieve(question, k=k)

    @staticmethod
    def retrieve_context(question):
        times = []
        start = time.time()
        questions = RAGFusion.generating_search_results(question)
        times.append(time.time() - start)
        start = time.time()

        search_result = RAGFusion.retrieve_fusion_set(questions)
        reciprocal_ranked = RAGFusion.reciprocal_rank_fusion(search_result)
        times.append(time.time() - start)
        start = time.time()

        
        reranked = RAGRerank.reranking(reciprocal_ranked, question)
        times.append(time.time() - start)

        return {
            "context": reranked,
            "questions": questions,
            "times": times
        }

    @staticmethod
    def generate_response(question, return_steps=True, eval=False, context=None):
        if context is None:
            retrieved_context = RAGFacade.retrieve_context(question)
            context = "\n\n".join([doc.metadata['full_text'] for doc in retrieved_context['context']])[:16380]
        client = AppVariables.openai_client
        inputs = f" Đây là các đoạn văn bản chứa thông tin cho câu hỏi của người dùng, bạn hãy chọn lọc thông tin:\n{context}.Hãy trả lời câu hỏi CHỈ dựa vào các thông tin trên."

        start = time.time()
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Bạn là một tư vấn viên cho các dịch vụ công tại Cần Thơ Việt Nam, hãy trả lời lịch sự."},
                {"role": "system", "content": inputs},
                {"role": "user", "content": question}
            ],
            temperature=0
        )
        response_time = time.time() - start
        response = {
            "answer": completion.choices[0].message.content
        }
        if return_steps:
            response["documents"] = retrieved_context["context"]
            response['questions'] = retrieved_context['questions']
        if eval:
            times = retrieved_context['times']
            times.append(response_time)
            response['times'] = times
        
        return response

        