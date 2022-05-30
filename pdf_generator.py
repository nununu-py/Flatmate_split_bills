from fpdf import FPDF
import os
import webbrowser


class PdfReport:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, fm1, fm2, fm1_days, fm2_days, bill_period, total_bill, bill_year, fm1_pays, fm2_pays):
        """
        make a program result into a pdf file
        """
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # add icon
        pdf.image(name="files/house.png", h=40, w=40)

        # add title
        pdf.set_title(title="My First App")
        pdf.set_font(family="Times", size=24, style="BU")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", align="C", ln=1)

        # add bill information
        pdf.set_font(family="Times", size=18)
        pdf.cell(w=135, h=50, txt=f"Total Bill : ${total_bill}", border=0, ln=1)
        pdf.cell(w=110, h=50, txt=f"Period : {bill_period}", border=0, ln=1)
        pdf.cell(w=120, h=50, txt=f"Year : {bill_year}", border=0, ln=1)
        pdf.cell(w=0, h=50, ln=1)

        # add program result
        pdf.cell(w=269, h=50, txt="Flatmate 1", border=1, align="C")
        pdf.cell(w=270, h=50, txt="Flatmate 2", border=1, align="C", ln=1)
        pdf.cell(w=269, h=50, txt=f"Name : {fm1}", border=1, align="C")
        pdf.cell(w=270, h=50, txt=f"Name : {fm2}", border=1, align="C", ln=1)
        pdf.cell(w=269, h=50, txt=f"Days in flat : {str(fm1_days)}", border=1, align="C")
        pdf.cell(w=270, h=50, txt=f"Days in flat : {str(fm2_days)}", border=1, align="C", ln=1)
        pdf.cell(w=269, h=50, txt=f"Total pays : {str(fm1_pays)}", border=1, align="C")
        pdf.cell(w=270, h=50, txt=f"Total pays : {str(fm2_pays)}", border=1, align="C", ln=1)

        # change directory and open the pdf file
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
