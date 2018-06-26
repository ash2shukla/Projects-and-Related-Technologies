# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import csv

def read_csv_list():
    # Read csv file line by line as list
    file_pointer = open('Sample_CSV.csv')
    csv_reader = csv.reader(file_pointer)
    for line in csv_reader:
        print(line)

    file_pointer.close()


def read_csv_dict():
    # Read csv file line by line as an ordered dictionary
    # We can convert it into an unordered dictionary if needed using dict(line)
    # Where the keys are the values in first row
    file_pointer = open('Sample_CSV.csv')
    csv_reader = csv.DictReader(file_pointer)
    for line in csv_reader:
        print(dict(line))

    file_pointer.close()


def write_csv_list():
    file_pointer = open('NewListCSV.csv', 'w')
    csv_writer = csv.writer(file_pointer)
    # Let us write number - their_squares
    for number in range(1, 100 + 1):
        csv_writer.writerow([number, number**2])
    file_pointer.close()


def write_csv_dict():
    file_pointer = open('NewDictCSV.csv', 'w')
    headers = ['Number', 'Square']
    csv_writer = csv.DictWriter(file_pointer, fieldnames=headers)
    # Let us write number - their_squares
    csv_writer.writeheader()
    for number in range(1, 100 + 1):
        csv_writer.writerow({'Number': number, 'Square': number**2})
    file_pointer.close()


def sniff_header(filename):
    file_pointer = open(filename)
    csv_sniffer = csv.Sniffer()
    # Let us write number - their_squares
    if csv_sniffer.has_header(file_pointer.read()):
        print('First line of CSV is a header')
    else:
        print('First line of CSV is not a header')
    file_pointer.close()


def main():
    #read_csv_list()
    #read_csv_dict()
    #write_csv_list()
    #write_csv_dict()
    sniff_header('NewDictCSV.csv')


if __name__ == "__main__":
    main()
