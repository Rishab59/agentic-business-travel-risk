from enum import Enum

class QuestionType(Enum):

    KNOWN = "known"

    UNKNOWN = "unknown"

    CONFIDENTIAL = "confidential"

    IRRELEVANT = "irrelevant"

CONFIDENTIAL_KEYWORDS = [

    "salary", "payroll", "compensation", "passport number",

    "aadhaar", "pan", "bank account", "ssn", "personal phone",

    "medical record", "health report"

]

IRRELEVANT_KEYWORDS = [

    "movie", "song", "music", "cricket score", "joke", "weather today",

    "who won", "latest meme"

]

def classify_question(question: str) -> QuestionType:

    q = question.lower()

    for word in CONFIDENTIAL_KEYWORDS:

        if word in q:

            return QuestionType.CONFIDENTIAL

    for word in IRRELEVANT_KEYWORDS:

        if word in q:

            return QuestionType.IRRELEVANT

    # RAG / LLM-based classification will be added later

    return QuestionType.UNKNOWN