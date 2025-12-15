import sys

import os

# Add project root to Python path

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

sys.path.append(PROJECT_ROOT)


from app.question_classifier import classify_question, QuestionType

questions = [

    "What visa do I need for Germany?",

    "What is my salary in euros?",

    "Tell me a joke"

]

for q in questions:

    result = classify_question(q)

    print(f"Question: {q}")

    print(f"Classified as: {result.value}")

    print("-" * 50)