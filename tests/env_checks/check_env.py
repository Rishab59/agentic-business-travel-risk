from dotenv import load_dotenv

import os

load_dotenv()

print("TENANT_ID:", "FOUND" if os.getenv("TENANT_ID") else "MISSING")

print("CLIENT_ID:", "FOUND" if os.getenv("CLIENT_ID") else "MISSING")

print("CLIENT_SECRET:", "FOUND" if os.getenv("CLIENT_SECRET") else "MISSING")

print("PROJECT_ENDPOINT:", "FOUND" if os.getenv("PROJECT_ENDPOINT") else "MISSING")

print("MODEL_NAME:", os.getenv("MODEL_NAME"))

print("AGENT_NAME:", os.getenv("AGENT_NAME"))