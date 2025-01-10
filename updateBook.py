from sheet_dimensions import start_row, end_row, subject_col_map
import openpyxl


def saveBook(book):
    book.save("D:\\Python\\attendance_tracker.py\\Book1.xlsx")
    print("Book Updated Successfully")


def handle(subject_code, roll_absentees):
    try:

        book = openpyxl.load_workbook("D:\\Python\\attendance_tracker.py\\Book1.xlsx")
        sheet = book["Sheet1"]
        #   r = sheet.max_row
        #   c = sheet.max_column
        for r in range(start_row, end_row):
            cell = sheet.cell(row=r, column=5)
            if cell.value in roll_absentees:
                active_cell = sheet.cell(row=r, column=subject_col_map[subject_code])
                if active_cell.value == 1:
                    print(f"warning mail to {sheet.cell(row = r, column=6)} be sent/ only 1 leave left for subject {sheet.cell(row=r, column=7)}")  ## todo

                elif active_cell.value == 2:
                    print("Exam withdrawal mail to be sent / Penalty imposed")
                active_cell.value += 1
                saveBook(book)

    except RuntimeError as e:
        print(e)

    pass
