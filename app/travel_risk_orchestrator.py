from app.question_classifier import classify_question, QuestionType

from rag.rag_retriever import RAGRetriever

from app.unknown_question_handler import UnknownQuestionHandler

class TravelRiskOrchestrator:

    def __init__(self, agent_id: str):

        self.rag = RAGRetriever()

        self.unknown_handler = UnknownQuestionHandler(agent_id)

    def handle(self, question: str):

        # 1. Safety & relevance check

        category = classify_question(question)

        if category == QuestionType.CONFIDENTIAL:

            return {

                "status": "BLOCKED",

                "message": "This question involves confidential or sensitive information and cannot be answered."

            }

        if category == QuestionType.IRRELEVANT:

            return {

                "status": "BLOCKED",

                "message": "This question is not related to business travel risk."

            }

        # 2. Try RAG for KNOWN knowledge

        rag_result = self.rag.retrieve(question)

        if rag_result:

            return {

                "status": "KNOWN",

                "answer": rag_result["metadata"]["answer"],

                "source": "RAG",

                "confidence": round(1 - rag_result["distance"], 2),

                "matched_question": rag_result["metadata"]["question"]

            }

        # 3. Truly UNKNOWN → draft + pending review

        return self.unknown_handler.handle(question)