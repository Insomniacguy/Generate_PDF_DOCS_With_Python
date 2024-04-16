from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')
print(df)

pdf = FPDF(orientation='p', unit='mm', format="A4")  # FPDF is a class which creates pdf object instances just like
# string obj creates "hello" instances

# 1st Page
# w=0 will expand the border till the end of the page. It is recommended to set to 0.
# ln is breakline and it is always recommended to keep it 1 so
# you will go to the next line when you make the next cell. 0 will make the next string appear on same line where
# width ends

for index, row in df.iterrows():
    pdf.add_page()  # a method of class FPDF to add pages to the document.
    pdf.set_font(family='Times', size=12, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    pdf.line(10,20, 200, 20)
# adding more pages
    for i in range(row['Pages'] - 1):
        pdf.add_page()

pdf.output("output")





