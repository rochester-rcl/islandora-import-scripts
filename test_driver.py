import ur.xmlrow as xml_row
import os
import csv
import sys

# ########################################
# Main Program for testing output
# ########################################

# get the csv file input
a_file = input("Please enter csv file name: ")
if not os.path.isfile(a_file):
    print("Could not find file " + a_file)
    sys.exit()
else:
    print("found file ")

print("testing csv file")
xml_row.print_csv_info(a_file)

test_xml = input("Test xml output (yes) to test: ")
if test_xml.lower() == "yes":
    output_directory = input("Please enter xml output directory: ")
    if not os.path.isdir(output_directory):
        print("Directory " + output_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + output_directory)
        # open the csv and start iterating through the rows
        with open(a_file, 'r') as csv_file:
            fileReader = csv.reader(csv_file)
            counter = 1
            for row in fileReader:
                if row[30]:
                    pages = int(row[30])
                    if pages > 0:
                        print("processing " + str(pages) + " pages")
                        xmlFile = os.path.join(output_directory, "MODS_" + str(counter) + ".xml")
                        xml_row.create_xml_file(row, xmlFile)
                else:
                    print("Skipping row " + str(counter) + " pages found were " + row[30])
                counter += 1
