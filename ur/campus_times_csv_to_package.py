#!/usr/bin/python

import mods
import csv
import xml.etree.ElementTree as elementTree
import os
import sys


# ##########################################
# Build the xml file using the MODS classes
# ##########################################
def build_xml(row, template):
    print('build xml')

    # deal with namespace issues
    tree = elementTree.iterparse(template)
    for _, el in tree:
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
    root = tree.root

    title_info = root.find('titleInfo')
    title = title_info.find('title')

    new_title = str(row[1])
    title.text = new_title

    origin_info = root.find('originInfo')
    date_created = origin_info.find('dateCreated')
    date_issued = origin_info.find('dateIssued')

    date_created.text = str(row[6])
    date_issued.text = str(row[6])

    physical_description = root.find("physicalDescription")
    extent = physical_description.find('extent')
    extent.text = str(row[2])

    note = root.find("note")
    note_text = note.text
    note.text = note_text.replace("[Title]", row[1])

    new_tree = elementTree.ElementTree(root)
    new_tree.write("text.xml")
    sys.exit()


def process_csv(a_file, template):
    with open(a_file, 'r') as csv_file:
        file_reader = csv.reader(csv_file)
        next(file_reader, None)  # skip the headers
        counter = 1
        for row in file_reader:
            build_xml(row, template)


def print_row(row_count, row, num_columns):
    print("************* " + str(row_count) + " *********************")
    for x in range(0, num_columns):
        print("row " + str(x) + " = " + row[x].strip())
    print("*************  DONE - " + str(row_count) + " *********************")
    print("")


#
#  Use this to print out the fields of a csv file and allows programmer
#  to see the output
#
def print_csv_info(a_file, num_columns):
    with open(a_file, 'r') as csv_file:
        file_reader = csv.reader(csv_file)
        counter = 1
        for row in file_reader:
            print_row(counter, row, num_columns)
            counter += 1


# ########################################
# Main Program - if needed
# ########################################


def main():

    num_excel_columns = 8
    print("****** main ****** ")

    # get the csv file input
    # csv_file = input("Please enter csv file name: ")
    csv_file = '/Users/ndsarr/rcl/campus-times-data/csv-reports/tcw.csv'

    if not os.path.isfile(csv_file):
        print("Could not find file " + csv_file)
        sys.exit()
    else:
        print("csv found file ")

    # template_file = input("Please enter template file name: ")
    template_file = '/Users/ndsarr/rcl/campus-times-data/mods/CloisterWindow_MODS_template.xml'
    if not os.path.isfile(template_file):
        print("Could not find file " + template_file)
        sys.exit()
    else:
        print("template found file ")

    # test = input("Test csv file (yes) to test: ")
    test = 'no'
    if test.lower() == "yes":
        print("testing csv file")
        print_csv_info(csv_file, num_excel_columns)
    else:
        # output directory for processing
        # output_directory = input("Please enter output directory: ")
        output_directory = '/Users/ndsarr/rcl/campus-times-data/output'
        if not os.path.isdir(output_directory):
            print("Directory " + output_directory + " does not exist or is not a directory")
            sys.exit()
        else:
            print("Directory found " + output_directory)
            process_csv(csv_file, template_file)
            # create_xml_files(csv_file, output_directory)


if __name__ == '__main__':
    main()
