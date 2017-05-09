import csv
import os
import sys
import requests


def download_url(url, fileName):
    full_file_path = os.path.join("ur_output_dir", fileName)
    out_file = open(full_file_path, 'wb')
    print('file path = ' + full_file_path + ' url = ' + url)
    header = requests.head(url)
    if header.status_code == 200:
        print('downloading')
        data = requests.get(url)
        out_file.write(data.content)
    else:
        print('could not download file ' + url)


def process_csv(a_file):
    with open(a_file, 'r') as csv_file:
        file_reader = csv.reader(csv_file)
        next(file_reader, None)  # skip the headers
        for row in file_reader:
            download_url(row[3], row[0])

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
            for x in range(0, 5):
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
        process_csv(a_file)

if __name__ == '__main__':
    main()
