from rag.draft_answer_generator import DraftAnswerGenerator
from rag.pending_knowledge_store import PendingKnowledgeStore


class UnknownQuestionHandler:
    def __init__(self, agent_id: str):
        self.generator = DraftAnswerGenerator(agent_id)
        self.pending_store = PendingKnowledgeStore()

    def handle(self, question: str):
        draft = self.generator.generate(question)

        self.pending_store.add(
            question=question,
            draft_answer=draft,
            source="azure-agent"
        )

        return {
            "status": "UNKNOWN",
            "message": "This question requires verification. A draft answer has been generated for review.",
            "draft_answer": draft
        }