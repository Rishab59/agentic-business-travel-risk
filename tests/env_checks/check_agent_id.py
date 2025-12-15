from dotenv import load_dotenv

import os

load_dotenv()

agent_id = os.getenv("AGENT_ID")

print("AGENT_ID:", agent_id if agent_id else "MISSING")