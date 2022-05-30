from share_file import ShareFile
from flatmate import Bill, Flatmate
from pdf_generator import PdfReport

bill_amount = int(input("Please input total bill amount : $"))
bill_period_month = input("What month ? ")
bill_period_year = input("What Year ? ")

bill = Bill(amount=bill_amount, month=bill_period_month, year=bill_period_year)

flatmate1_info = Flatmate(name=input("Insert your name : "), days_in_flat=int(input("Total Days in flat : ")))
flatmate2_info = Flatmate(name=input("Insert your flatmate name : "), days_in_flat=int(input("Total Days in flat : ")))

flatmate1_pays = flatmate1_info.pays(bill_result=bill.amount, flatmate=flatmate2_info)
flatmate2_pay = flatmate2_info.pays(bill_result=bill.amount, flatmate=flatmate1_info)

pdfResult = PdfReport(f"{bill.month}, {bill.year}.pdf")
pdfResult.generate(fm1=flatmate1_info.name, fm2=flatmate2_info.name, fm1_days=flatmate1_info.days_in_flat,
                   fm2_days=flatmate2_info.days_in_flat, bill_period=bill.month, total_bill=bill.amount,
                   bill_year=bill.year, fm1_pays=flatmate1_pays, fm2_pays=flatmate2_pay)

get_file = ShareFile(pdfResult.filename)
print(get_file.share_file())
