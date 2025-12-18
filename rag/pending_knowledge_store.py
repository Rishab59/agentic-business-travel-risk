import json

import os

from datetime import datetime

from typing import Any

class PendingKnowledgeStore:

    FILE_PATH = "data/pending_knowledge.json"

    def __init__(self):

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.FILE_PATH):

            with open(self.FILE_PATH, "w", encoding="utf-8") as f:

                json.dump([], f, indent=2)

    def _safe_load(self):

        """

        Safely load JSON file.

        If file is empty or corrupted, reset to empty list.

        """

        try:

            with open(self.FILE_PATH, "r", encoding="utf-8") as f:

                return json.load(f)

        except (json.JSONDecodeError, FileNotFoundError):

            return []

    def _safe_save(self, data):

        """

        Safely write JSON to disk.

        """

        with open(self.FILE_PATH, "w", encoding="utf-8") as f:

            json.dump(data, f, indent=2, ensure_ascii=False)

    def add(self, question: str, draft_answer: Any, source="llm"):

        """

        Store UNKNOWN question draft answers for human review.

        """

        data = self._safe_load()

        # 🔒 CRITICAL FIX: force draft_answer into plain text

        if not isinstance(draft_answer, str):

            try:

                draft_answer = str(draft_answer)

            except Exception:

                draft_answer = "[DRAFT_ANSWER_NOT_SERIALIZABLE]"

        entry = {

            "question": question,

            "draft_answer": draft_answer,

            "source": source,

            "status": "PENDING_REVIEW",

            "created_at": datetime.utcnow().isoformat()

        }

        data.append(entry)

        self._safe_save(data)

    def list_pending(self):

        return self._safe_load()