import sys

import os

# Add project root to Python path

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(PROJECT_ROOT)


from agents.travel_risk_agent import TravelRiskAgent

agent = TravelRiskAgent()

questions = [

    "What visa is required for business travel to Germany?",

    "What is the dress code for offices in Japan?"

]

for q in questions:

    print("\nQuestion:", q)

    response = agent.answer(q)

    print("Response:", response)