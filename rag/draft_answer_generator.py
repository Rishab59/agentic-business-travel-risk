from agents.agent_client import AgentClient

class DraftAnswerGenerator:

    def __init__(self, agent_id: str):

        self.agent_client = AgentClient(agent_id)

    def generate(self, question: str) -> str:

        prompt = f"""

You are a corporate travel risk assistant.

Generate a cautious, factual draft answer.

Rules:

- Do not assume certainty

- Mention that policies vary by company and country

- Do NOT give legal guarantees

Question:

{question}

"""

        return self.agent_client.ask(prompt)