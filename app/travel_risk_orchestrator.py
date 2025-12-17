from app.question_classifier import classify_question, QuestionType
from rag.rag_retriever import RAGRetriever
from app.unknown_question_handler import UnknownQuestionHandler


class TravelRiskOrchestrator:
    def __init__(self, agent_id: str):
        self.rag = RAGRetriever()
        self.unknown_handler = UnknownQuestionHandler(agent_id)

    def handle(self, question: str):
        category = classify_question(question)

        if category == QuestionType.KNOWN:
            result = self.rag.retrieve(question)
            if result and result["status"] == "KNOWN":
                return {
                    "status": "KNOWN",
                    "answer": result["answer"],
                    "source": "RAG"
                }

        if category == QuestionType.UNKNOWN:
            return self.unknown_handler.handle(question)

        if category == QuestionType.CONFIDENTIAL:
            return {
                "status": "BLOCKED",
                "message": "This question involves confidential or sensitive information and cannot be answered."
            }

        return {
            "status": "IRRELEVANT",
            "message": "This question is not related to business travel risk analysis."
        }