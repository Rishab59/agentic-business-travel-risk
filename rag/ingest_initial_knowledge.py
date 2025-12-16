import sys

import os

# Add project root to Python path

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(PROJECT_ROOT)


from rag.embedding_model import EmbeddingModel

from rag.vector_store import VectorStore

from rag.knowledge_seed import SEED_KNOWLEDGE

def main():

    print("Loaded seed knowledge count:", len(SEED_KNOWLEDGE))

    embedder = EmbeddingModel()

    vector_store = VectorStore(dim=384)

    print("Before ingest, vectors:", vector_store.index.ntotal)

    for item in SEED_KNOWLEDGE:

        print("Ingesting:", item["question"])

        text_to_embed = f"Question: {item['question']} Answer: {item['answer']}"

        embedding = embedder.embed_text(text_to_embed)

        vector_store.add(

            embedding=embedding,

            meta=item

        )

        print("Vectors after add:", vector_store.index.ntotal)

    print("Final vectors:", vector_store.index.ntotal)

    print("Initial knowledge ingested successfully")

if __name__ == "__main__":

    main()

'''
from rag.embedding_model import EmbeddingModel

from rag.vector_store import VectorStore

from rag.knowledge_seed import SEED_KNOWLEDGE

def main():

    embedder = EmbeddingModel()

    vector_store = VectorStore(dim=384)

    for item in SEED_KNOWLEDGE:

        text_to_embed = f"Question: {item['question']} Answer: {item['answer']}"

        embedding = embedder.embed_text(text_to_embed)

        vector_store.add(

            embedding=embedding,

            meta=item

        )

    print("Initial knowledge ingested successfully")

if __name__ == "__main__":

    main()
'''