import os

from dotenv import load_dotenv

from azure.identity import ClientSecretCredential

from azure.ai.projects import AIProjectClient

load_dotenv()

tenant_id = os.getenv("TENANT_ID")

client_id = os.getenv("CLIENT_ID")

client_secret = os.getenv("CLIENT_SECRET")

endpoint = os.getenv("PROJECT_ENDPOINT")

model_name = os.getenv("MODEL_NAME")

agent_name = os.getenv("AGENT_NAME")

credential = ClientSecretCredential(

    tenant_id=tenant_id,

    client_id=client_id,

    client_secret=client_secret

)

project = AIProjectClient(

    credential=credential,

    endpoint=endpoint

)

agent = project.agents.create_agent(

    model=model_name,

    name=agent_name,

    instructions=(

        "You are an enterprise Business Travel Risk Analysis Agent. "

        "You help employees understand legal, compliance, cultural, health, "

        "safety, and company policy requirements before traveling to any country. "

        "You must classify questions, use retrieved knowledge when available, "

        "and handle unknown or sensitive questions safely."

    )

)

print("Agent created successfully")

print("AGENT_ID =", agent.id)