import sys

import os

# Add project root to Python path

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(PROJECT_ROOT)


from app.travel_risk_orchestrator import TravelRiskOrchestrator


class TravelRiskApp:
    def __init__(self, agent_id: str):
        self.orchestrator = TravelRiskOrchestrator(agent_id)

    def process_question(self, question: str):
        return self.orchestrator.handle(question)