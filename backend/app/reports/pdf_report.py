from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

from reportlab.lib.units import inch


class PDFReportGenerator:

    @staticmethod
    def create(filename, title, content):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(title, styles["Title"])
        )

        story.append(Spacer(1, 0.3 * inch))

        # Split into lines
        for line in content.split("\n"):

            line = line.strip()

            if not line:
                story.append(Spacer(1, 0.15 * inch))
                continue

            # Remove markdown characters
            line = (
                line.replace("#", "")
                    .replace("*", "")
                    .replace("`", "")
            )

            story.append(
                Paragraph(line, styles["BodyText"])
            )

        doc.build(story)

        return filename
