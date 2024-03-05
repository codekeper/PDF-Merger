import PyPDF2
import subprocess

try:
    project_slides = "project_slides.pdf"
    with open(project_slides, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        subprocess.run(["cmd", "/c", "start", project_slides])
except FileNotFoundError:
    print("error: file not found")
