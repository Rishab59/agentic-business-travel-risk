import json

import os

from datetime import datetime

class PendingKnowledgeStore:

    FILE_PATH = "data/pending_knowledge.json"

    def __init__(self):

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.FILE_PATH):

            with open(self.FILE_PATH, "w") as f:

                json.dump([], f)

    def add(self, question: str, draft_answer: str, source="llm"):

        with open(self.FILE_PATH, "r") as f:

            data = json.load(f)

        entry = {

            "question": question,

            "draft_answer": draft_answer,

            "source": source,

            "status": "PENDING_REVIEW",

            "created_at": datetime.utcnow().isoformat()

        }

        data.append(entry)

        with open(self.FILE_PATH, "w") as f:

            json.dump(data, f, indent=2)

    def list_pending(self):

        with open(self.FILE_PATH, "r") as f:

            return json.load(f)