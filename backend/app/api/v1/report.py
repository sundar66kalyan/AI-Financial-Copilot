from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.dependencies.auth import get_current_user

from app.services.ai_service import AIService
from app.reports.pdf_report import PDFReportGenerator

router = APIRouter(
    prefix="/api/v1/report",
    tags=["AI Report"]
)


@router.get("/generate")
def generate_report(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    report = AIService.generate_financial_report(
        db=db,
        user_id=current_user.id
    )

    print("=" * 80)
    print(report)
    print("=" * 80)

    pdf = PDFReportGenerator.create(
        filename="financial_report.pdf",
        title="AI Financial Report",
        content=report
    )

    return {
        "message": "Report generated successfully",
        "pdf": pdf,
        "report": report
    }


@router.get("/download")
def download_report():

    return FileResponse(
        path="financial_report.pdf",
        filename="financial_report.pdf",
        media_type="application/pdf"
    )
