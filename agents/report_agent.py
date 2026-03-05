from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime
import os

def report_agent(state):

    df = state["result"]

    os.makedirs("pdf_reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = f"pdf_reports/report_{timestamp}.pdf"

    styles = getSampleStyleSheet()

    elements = []

    # Title
    title = Paragraph("AI Generated Sales Report", styles['Title'])
    elements.append(title)

    elements.append(Spacer(1, 20))

    # Date
    date_text = Paragraph(f"Generated on: {datetime.now()}", styles['Normal'])
    elements.append(date_text)

    elements.append(Spacer(1, 20))

    # Table data
    data = [list(df.columns)] + df.values.tolist()

    table = Table(data)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),

        ('ALIGN',(0,0),(-1,-1),'CENTER'),

        ('GRID',(0,0),(-1,-1),1,colors.black),

        ('BACKGROUND',(0,1),(-1,-1),colors.beige),
    ]))

    elements.append(table)

    pdf = SimpleDocTemplate(file_path, pagesize=letter)

    pdf.build(elements)

    return {"pdf_file": file_path}