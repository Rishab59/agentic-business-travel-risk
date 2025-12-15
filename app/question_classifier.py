from enum import Enum

class QuestionType(Enum):

    KNOWN = "known"

    UNKNOWN = "unknown"

    CONFIDENTIAL = "confidential"

    IRRELEVANT = "irrelevant"

def classify_question(question: str) -> QuestionType:

    """

    Placeholder classification logic.

    Real logic (LLM + rules + RAG signals) will be added next.

    """

    return QuestionType.UNKNOWN