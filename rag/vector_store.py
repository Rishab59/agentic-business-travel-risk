import faiss

import os

import pickle

import numpy as np

class VectorStore:

    def __init__(self, dim: int, index_path: str = "data/faiss.index"):

        self.dim = dim

        self.index_path = index_path

        self.meta_path = index_path + ".meta"

        if os.path.exists(self.index_path):

            self.index = faiss.read_index(self.index_path)

            with open(self.meta_path, "rb") as f:

                self.metadata = pickle.load(f)

        else:

            self.index = faiss.IndexFlatL2(dim)

            self.metadata = []

    def add(self, embedding, meta):

        embedding = np.array([embedding]).astype("float32")

        self.index.add(embedding)

        self.metadata.append(meta)

        self._persist()

    def search(self, embedding, top_k: int = 1):

        embedding = np.array([embedding]).astype("float32")

        distances, indices = self.index.search(embedding, top_k)

        results = []

        for idx, dist in zip(indices[0], distances[0]):

            if idx < len(self.metadata):

                results.append({

                    "distance": float(dist),

                    "metadata": self.metadata[idx]

                })

        return results

    def _persist(self):

        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)

        faiss.write_index(self.index, self.index_path)

        with open(self.meta_path, "wb") as f:

            pickle.dump(self.metadata, f)