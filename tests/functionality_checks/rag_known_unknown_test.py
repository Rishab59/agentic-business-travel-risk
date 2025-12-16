import sys

import os

# Add project root to Python path

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

sys.path.append(PROJECT_ROOT)

from rag.rag_retriever import RAGRetriever

retriever = RAGRetriever()

questions = [

    "What visa is required for business travel to Germany?",

    "What is the dress code for offices in Japan?"

]

for q in questions:

    result = retriever.retrieve(q)

    print(f"\nQuestion: {q}")

    if result:

        print("Result: KNOWN")

        print("Matched Data:", result["metadata"])

        print("Distance:", result["distance"])

    else:

        print("Result: UNKNOWN")