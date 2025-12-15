import sys

import os

# Add project root to Python path

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(PROJECT_ROOT)


from rag.embedding_model import EmbeddingModel

from rag.vector_store import VectorStore

from data.initial_knowledge import INITIAL_KNOWLEDGE

embedding_model = EmbeddingModel()

vector_store = VectorStore(dim=384)

for item in INITIAL_KNOWLEDGE:

    embedding = embedding_model.embed_text(item["question"])

    vector_store.add(embedding, item)

print("Initial knowledge ingested successfully")