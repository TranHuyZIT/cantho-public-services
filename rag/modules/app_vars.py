from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI
import openai
from langchain_community.embeddings import HuggingFaceEmbeddings
from os import getenv
from dotenv import load_dotenv
import cohere
from typing import List

load_dotenv()
OPENAI_API_KEY = getenv("OPENAI_API_KEY")
COHERE_API_KEY = getenv("COHERE_API_KEY")
class AppVariables:
    embeddings = HuggingFaceEmbeddings(model_name="keepitreal/vietnamese-sbert")
    vectorstore = Chroma(persist_directory="../data", embedding_function=embeddings)
    llm = OpenAI(api_key=OPENAI_API_KEY)
    co = cohere.Client(api_key=COHERE_API_KEY)
    openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)


    @staticmethod
    def retrieve(question):
        return AppVariables.vectorstore.similarity_search_with_relevance_scores(question, k=25)
    
    @staticmethod
    def reranking(docs: List[str], question):
        results = AppVariables.co.rerank(model="rerank-multilingual-v3.0", query=question, 
                                            documents=docs, top_n=3, return_documents=True)
        
        return results.results
    