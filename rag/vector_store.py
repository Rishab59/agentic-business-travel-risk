import faiss

import os

import pickle

import numpy as np

class VectorStore:

    def __init__(self, dim: int, index_path: str = "data/faiss.index"):

        self.dim = dim

        self.index_path = index_path

        self.meta_path = index_path + ".meta"

        if os.path.exists(self.index_path) and os.path.exists(self.meta_path):

            self.index = faiss.read_index(self.index_path)

            with open(self.meta_path, "rb") as f:

                self.metadata = pickle.load(f)

        else:

            self.index = faiss.IndexFlatL2(dim)

            self.metadata = []

    def _normalize(self, vector):

        vector = np.array(vector, dtype="float32")

        faiss.normalize_L2(vector)

        return vector

    def add(self, embedding, meta):

        embedding = np.array([embedding], dtype="float32")

        faiss.normalize_L2(embedding)

        self.index.add(embedding)

        self.metadata.append(meta)

        self._persist()

    def search(self, embedding, top_k: int = 1, distance_threshold: float = 0.7):

        """

        distance_threshold:

        - 0.0 → identical

        - ~0.3–0.7 → similar

        - >0.9 → unrelated

        """

        if self.index.ntotal == 0:

            return None

        embedding = np.array([embedding], dtype="float32")

        faiss.normalize_L2(embedding)

        distances, indices = self.index.search(embedding, top_k)

        idx = int(indices[0][0])

        dist = float(distances[0][0])

        if idx == -1 or idx >= len(self.metadata):

            return None

        if dist > distance_threshold:

            return None

        return {

            "distance": dist,

            "metadata": self.metadata[idx]

        }

    def _persist(self):

        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)

        faiss.write_index(self.index, self.index_path)

        with open(self.meta_path, "wb") as f:

            pickle.dump(self.metadata, f)