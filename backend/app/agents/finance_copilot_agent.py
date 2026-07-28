from app.services.ai_service import AIService


class FinanceCopilotAgent:

    @staticmethod
    def chat(db, user_id: int, question: str):
        return AIService.ask_finance_copilot(
            db=db,
            user_id=user_id,
            question=question,
        )
