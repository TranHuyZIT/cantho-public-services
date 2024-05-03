from fusion import RAGFusion
from rerank import RAGRerank
from app_vars import AppVariables

class RAGFacade:
    @staticmethod
    def retrieve_context(question):
        search_result_scores = RAGFusion.generating_search_results(question)
        reciprocal_ranked = RAGFusion.reciprocal_rank_fusion(search_result_scores, limit=25)
        reranked = RAGRerank.reranking(reciprocal_ranked, question)

        return reranked

    @staticmethod
    def generate_response(question, return_documents=True):
        retrieved_context = RAGFacade.retrieve_context(question)
        context = "\n\n".join([doc.metadata['full_text'] for doc in retrieved_context])
        client = AppVariables.openai_client
        inputs = f" Đây là các đoạn văn bản chứa thông tin, bạn có thể dùng nếu cần:\n{context}.Hãy trả lời câu hỏi, nếu không có thông tin trong văn bản, hãy yêu cầu người dùng cung cấp thêm thông tin."

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Bạn là một tư vấn viên cho các dịch vụ công tại Cần Thơ Việt Nam, hãy trả lời lịch sự."},
                {"role": "system", "content": inputs},
                {"role": "user", "content": question}
            ]
        )
        response = {
            "answer": completion.choices[0].message.content
        }
        if return_documents:
            response["documents"] = retrieved_context
        
        return response

        