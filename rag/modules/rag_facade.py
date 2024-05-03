from fusion import RAGFusion
from rerank import RAGRerank

class RAGFacade:
    @staticmethod
    def retrieve_context(question):
        search_result_scores = RAGFusion.generating_search_results(question)
        reciprocal_ranked = RAGFusion.reciprocal_rank_fusion(search_result_scores, limit=25)
        # filtered = RAGRerank.filtering(reciprocal_ranked, question)
        reranked = RAGRerank.reranking(reciprocal_ranked, question)

        return reranked

    @staticmethod
    def generate_response(question):
        retrieved_context = RAGFacade.retrieve_context(question)
        return retrieved_context
        