import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
filepaths = glob.glob("Invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    filename = Path(filepath).stem # Path obj/Intelligent string
    invoice_num = filename.split("-")
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=80, h=8, txt=f"Invoice #: {invoice_num[0]}")
    pdf.output(f"PDFs/{filename}.pdf")