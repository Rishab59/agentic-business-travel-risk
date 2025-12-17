class UnknownQuestionHandler:

    def handle(self, question: str):

        return {

            "status": "UNKNOWN",

            "reason": "No sufficiently similar knowledge found",

            "question": question

        }