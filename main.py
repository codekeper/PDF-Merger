import PyPDF2

try:
    # specifying the path of all files:
    pdf1 = "pdf1.pdf"
    pdf2 = "pdf2.pdf"
    pdf3 = "pdf3.pdf"

    # creating list of PDFs to merge:
    all_pdfs = [pdf1, pdf2, pdf3]

    # apply the merge function:
    merger = PyPDF2.PdfMerger()

    # iterate through each file in the list & merge:
    for pdf in all_pdfs:
        merger.append(pdf)
    merger.write("merged.pdf")
    merger.close()

except FileNotFoundError:
    print("error: file not found")
