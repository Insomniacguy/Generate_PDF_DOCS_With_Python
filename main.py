from fpdf import FPDF
import pandas as pd

# page_height = 297
# av_height = page_height - 20
# line_space = 10
# num_lines = int(page_height / line_space)


df = pd.read_csv('topics.csv')
print(df)

pdf = FPDF(orientation='p', unit='mm', format="A4")  # FPDF is a class which creates pdf object instances just like
# string obj creates "hello" instances
pdf.set_auto_page_break(auto=False, margin=0)

# 1st Page
# w=0 will expand the border till the end of the page. It is recommended to set to 0.
# ln is breakline and it is always recommended to keep it 1 so
# you will go to the next line when you make the next cell. 0 will make the next string appear on same line where
# width ends

# the first for loop adds the parent page. The page that contains the header
for index, row in df.iterrows():
    # Set the header
    pdf.add_page()  # a method of class FPDF to add pages to the document.
    pdf.set_font(family='Times', size=12, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    # for line in range(num_lines):
    #     y = 20 + line * line_space
    #     pdf.line(10, y, 200, y)
    # adding multiple lines with a distance of 10mm
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # Set the footer
    pdf.ln(260)
    pdf.set_font(family='Times', size=8, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=8, txt=row['Topic'], align='R', ln=1)

    # adding more pages
    for i in range(row['Pages'] - 1):
        pdf.add_page()

        pdf.ln(272)  # Here we increase the nunber of break lines because our footer was displaying a little higher.
        # We added the original number of
        # breaklines and the height of the cell component 260 + 12
        pdf.set_font(family='Times', size=8, style='B')
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=8, txt=row['Topic'], align='R', ln=1)
        # for line in range(num_lines):
        #     y = 20 + line * line_space
        #     pdf.line(10, y, 200, y)
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)


pdf.output("output")
