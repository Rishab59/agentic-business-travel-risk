from rag.rag_retriever import RAGRetriever

from agents.unknown_question_handler import UnknownQuestionHandler

class TravelRiskAgent:

    def __init__(self):

        self.retriever = RAGRetriever()

        self.unknown_handler = UnknownQuestionHandler()

    def answer(self, question: str):

        result = self.retriever.retrieve(question)

        if result is None:

            return self.unknown_handler.handle(question)

        return {

            "status": "KNOWN",

            "answer": result["metadata"]["answer"],

            "distance": result["distance"]

        }