import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import os

# Path to the Excel file
excel_path = r"E:\\College_Studies\\pdftoexcel\\student_data1.xlsxx"
# Read data from Excel
df = pd.read_excel(excel_path)

# Path to save the PDF file
pdf_path = "E:\\College_Studies\\pdftoexcel\\output.pdf"  # Update this path

def create_pdf(dataframe, pdf_path):
    # Ensure the directory for the PDF path exists
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    # Initialize a canvas for the PDF
    pdf = canvas.Canvas(pdf_path, pagesize=A4)
    pdf.setTitle("Student Data Report")

    # Title on the PDF
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 800, "Student Data Report")

    # Set up table data and column headers
    data = [list(dataframe.columns)] + dataframe.values.tolist()

    # Create a Table with data
    table = Table(data)

    # Add styling to the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
        ('FONTSIZE', (0, 0), (-1, 0), 12),  # Header font size
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Padding for headers
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Background color for data rows
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Table grid lines
    ])
    table.setStyle(style)

    # Define position and size for the table on the PDF
    table.wrapOn(pdf, 450, 400)  # ✅ Remove 'width=' and 'height='

    table.drawOn(pdf, 30, 600 - (len(data) * 20))  # Adjust table position on the page

    # Save the PDF file
    pdf.save()
    print(f"PDF created successfully at {pdf_path}")

# Run the function to create the PDF
create_pdf(df, pdf_path)
