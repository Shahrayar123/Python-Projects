from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a new PDF document
pdf = canvas.Canvas("example.pdf", pagesize=letter)

# Set up fonts and styles
pdf.setFont("Helvetica", 12)

# Add content to the PDF
pdf.drawString(50, 750, "Hello, World!")
pdf.drawString(50, 700, "This is a PDF generated using Python and ReportLab.")

# Save and close the PDF document
pdf.save()
