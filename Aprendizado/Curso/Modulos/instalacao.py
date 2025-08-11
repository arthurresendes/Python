"""

pip install package_name

from colorama import init, Fore
init()

print(Fore.GREEN + 'Arthur Resende')

"""

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=22)
pdf.cell(200, 10, txt="Olá, sou o Arthur", ln=True, align='C')
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="Este é um PDF criado usando Python com a biblioteca FPDF.")
pdf.output("meu_pdf.pdf")