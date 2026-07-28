from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.dependencies.auth import get_current_user

from app.schemas.copilot import (
    CopilotRequest,
    CopilotResponse,
)

from app.agents.finance_copilot_agent import (
    FinanceCopilotAgent,
)

router = APIRouter(
    prefix="/copilot",
    tags=["AI Financial Copilot"],
)


@router.post(
    "/chat",
    response_model=CopilotResponse,
)
def chat(
    request: CopilotRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    answer = FinanceCopilotAgent.chat(
        db=db,
        user_id=current_user.id,
        question=request.question,
    )

    return CopilotResponse(
        answer=answer,
    )
