# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import xlrd
import xlwt
from tempfile import TemporaryFile
# tempfile module creates TemporaryFiles and Directories
# This tutorial uses it as an introduction to this tool as well


def read_excel():
    book = xlrd.open_workbook("Sample_XLSX.xlsx")
    print("The number of worksheets is {0}".format(book.nsheets))
    print("Worksheet name(s): {0}".format(book.sheet_names()))
    sh = book.sheet_by_index(0)
    print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
    print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
    for rx in range(sh.nrows):
        # Each element in this row is of type cell.type
        # Each cell has attributes ctype (content type), value
        # ctype is always an integer that corresponds to
        # 0 - Empty , 1 - Text, 2 - Float, 3 - Date, 4- Boolean, 5-Error, 6- Blank
        print(sh.row(rx))


def write_excel():
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('Sheet 1')
    book.add_sheet('Sheet 2')

    sheet1.write(0, 0, 'A1')
    sheet1.write(0, 1, 'B1')
    row1 = sheet1.row(1)
    row1.write(0, 'A2')
    row1.write(1, 'B2')
    sheet1.col(0).width = 10000

    sheet2 = book.get_sheet(1)
    sheet2.row(0).write(0, 'Sheet 2 A1')
    sheet2.row(0).write(1, 'Sheet 2 B1')
    sheet2.flush_row_data()
    sheet2.write(1, 0, 'Sheet 2 A3')
    sheet2.col(0).width = 5000
    sheet2.col(0).hidden = True

    book.save('XLSX_output.xls')
    book.save(TemporaryFile())


def main():
    read_excel()
    write_excel()


if __name__ == "__main__":
    main()
