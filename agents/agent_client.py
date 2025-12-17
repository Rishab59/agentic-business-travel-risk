import os

import time

from azure.identity import ClientSecretCredential

from azure.ai.projects import AIProjectClient

class AgentClient:

    def __init__(self, agent_id: str):

        self.agent_id = agent_id

        tenant_id = os.getenv("TENANT_ID")

        client_id = os.getenv("CLIENT_ID")

        client_secret = os.getenv("CLIENT_SECRET")

        endpoint = os.getenv("PROJECT_ENDPOINT")

        if not all([tenant_id, client_id, client_secret, endpoint]):

            raise ValueError("Azure credentials are not fully set in environment variables")

        creds = ClientSecretCredential(

            tenant_id=tenant_id,

            client_id=client_id,

            client_secret=client_secret

        )

        self.project = AIProjectClient(

            credential=creds,

            endpoint=endpoint

        )

    def ask(self, prompt: str) -> str:

        thread = self.project.agents.threads.create()

        self.project.agents.messages.create(

            thread_id=thread.id,

            role="user",

            content=prompt

        )

        run = self.project.agents.runs.create_and_process(

            thread_id=thread.id,

            agent_id=self.agent_id

        )

        while True:

            status = self.project.agents.runs.get(

                thread_id=thread.id,

                run_id=run.id

            ).status

            if status in ("completed", "failed"):

                break

            time.sleep(1)

        if status == "failed":

            raise RuntimeError("Agent execution failed")

        messages = list(self.project.agents.messages.list(thread_id=thread.id))

        for msg in messages:

            if msg.role == "assistant":

                return msg.content[0].text

        return ""