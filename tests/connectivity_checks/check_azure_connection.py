import os

from dotenv import load_dotenv

from azure.identity import ClientSecretCredential

from azure.ai.projects import AIProjectClient

load_dotenv()

tenant_id = os.getenv("TENANT_ID")

client_id = os.getenv("CLIENT_ID")

client_secret = os.getenv("CLIENT_SECRET")

endpoint = os.getenv("PROJECT_ENDPOINT")

credential = ClientSecretCredential(

    tenant_id=tenant_id,

    client_id=client_id,

    client_secret=client_secret

)

project_client = AIProjectClient(

    credential=credential,

    endpoint=endpoint

)

print("Azure AI Project client initialized successfully")