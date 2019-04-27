from openpyxl import Workbook


file_name = "results.xlsx"

def create_file():
    book = Workbook()
    book.create_sheet("Training Set")
    book.create_sheet("Result Set")
    book.save("results.xlsx")

    return book

def save_data(sheet_name, data_hash={}):
    book = create_file()
    sheet = book[sheet_name]
    
    for key, value in data_hash:
        row_data = (key, value)
        sheet.append(row_data)
    book.save(file_name)

