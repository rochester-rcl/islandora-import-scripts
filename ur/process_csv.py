import csv
import os
import sys
import requests


def check_image_url(url):
    r = requests.head(url)
    return r.status_code


def process_csv(a_file):
    output_file = open('out.csv', "w")
    csv_writer = csv.writer(output_file)
    with open(a_file, 'r') as csv_file:
        file_reader = csv.reader(csv_file)
        headers = next(file_reader, None)  # skip the headers
        headers.append('rights')
        csv_writer.writerow(headers)
        for row in file_reader:
            row.append('http://rightsstatements.org/page/CNE/1.0/?language=en')
            if check_image_url(row[1]) != 200:
                print("row " + str(1) + " = " + row[1] + " status = " + str(check_image_url(row[1])))
                row[1] = 'http://vrc.lib.rochester.edu/imagedrive/VRCIMAGES/1024/placeholder.jpg'
            csv_writer.writerow(row)

#
#  Use this to print out the fields of a csv file and allows programmer
#  to see the output
#


def print_csv_info(a_file):
    with open(a_file, 'r') as csv_file:
        file_reader = csv.reader(csv_file)
        counter = 1
        for row in file_reader:
            print("************* " + str(counter) + " *********************")
            counter += 1
            for x in range(0, 63):
                print("row " + str(x) + " = " + row[x])
            print("*************  DONE - " + str(counter) + " *********************")
            print("")

# ########################################
# Main Program
# ########################################

def main():
    # get the csv file input
    a_file = input("Please enter csv file name: ")
    if not os.path.isfile(a_file):
        print("Could not find file " + a_file)
        sys.exit()
    else:
        print("found file ")
        print_csv_info(a_file)

if __name__ == '__main__':
    main()
