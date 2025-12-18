import sys

import os

# Add project root to Python path

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(PROJECT_ROOT)


from dotenv import load_dotenv
from app.app_entry import TravelRiskApp


def main():
    load_dotenv()
    
    agent_id = os.getenv("AGENT_ID")
    if not agent_id:
        raise ValueError("AGENT_ID not set in environment")

    app = TravelRiskApp(agent_id)

    print("Business Travel Risk Agent Ready")
    print("Type 'exit' to quit\n")

    while True:
        question = input("User: ")
        if question.lower() == "exit":
            break

        response = app.process_question(question)

        print("\nAgent Response:")
        for k, v in response.items():
            print(f"{k}: {v}")
        print("-" * 40)


if __name__ == "__main__":
    main()

'''
import os

import time

from dotenv import load_dotenv

from azure.identity import ClientSecretCredential

from azure.ai.projects import AIProjectClient

load_dotenv()

credential = ClientSecretCredential(

    tenant_id=os.getenv("TENANT_ID"),

    client_id=os.getenv("CLIENT_ID"),

    client_secret=os.getenv("CLIENT_SECRET")

)

project = AIProjectClient(

    credential=credential,

    endpoint=os.getenv("PROJECT_ENDPOINT")

)

agent_id = os.getenv("AGENT_ID")

# Create a new thread

thread = project.agents.threads.create()

print("Thread created:", thread.id)

# Send a test message

project.agents.messages.create(

    thread_id=thread.id,

    role="user",

    content="What should I know before traveling to Russia for work?"

)

# Run the agent

run = project.agents.runs.create_and_process(

    thread_id=thread.id,

    agent_id=agent_id

)

# Fetch responses

messages = list(project.agents.messages.list(thread_id=thread.id))

for msg in messages:

    if msg.role == "assistant":

        print("\nAgent Response:\n")

        print(msg.content[0].text)

'''