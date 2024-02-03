from PypDF2 import PdfFileWriter, PdfFileReader
import getpass

pdfwriter = PdfFileWriter()
pdf = PdfFileReader("contoh.pdf")
for page_num in range(pdf.numPages):
    pdfwriter.addPage(pdf.getPages(page_num))
passw = getpass.getpass(prompt=' Enter Password: ')
pdfwriter.encrypt(passw)
with open('ho.pdf','wb') as f :
    pdfwriter.write(f)