from rag.embedding_model import EmbeddingModel

from rag.vector_store import VectorStore

# Distance threshold (lower = more similar)

SIMILARITY_THRESHOLD = 0.8  

class RAGRetriever:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        # all-MiniLM-L6-v2 produces 384-dim embeddings

        self.vector_store = VectorStore(dim=384)

    def retrieve(self, question: str):

        embedding = self.embedding_model.embed_text(question)

        results = self.vector_store.search(embedding)

        if not results:

            return None

        best_match = results[0]

        if best_match["distance"] <= SIMILARITY_THRESHOLD:

            return best_match

        return None