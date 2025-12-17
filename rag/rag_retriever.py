from rag.embedding_model import EmbeddingModel
from rag.vector_store import VectorStore


class RAGRetriever:
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore(dim=384)

    def retrieve(self, question: str):
        embedding = self.embedding_model.embed_text(question)

        result = self.vector_store.search(embedding)

        # UNKNOWN → must be None (important for tests)
        if result is None:
            return None

        # KNOWN → return metadata + distance
        return {
            "metadata": result["metadata"],
            "distance": result["distance"]
        }