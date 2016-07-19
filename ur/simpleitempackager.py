import ur.csvtoxml as xmlrow
import os
import csv
import sys
import xml.etree.ElementTree as ET
import shutil


# ##################################
# find first file with the specified name
# in the base path - walks the directory tree
# ##################################
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


# ##################################1
# Creates a folder for every page based on the file name - this is a
# requirement of Islandora
# ##################################
def add_obj(source_directory, dest_directory, base_filename, extension):
    filename = base_filename + "." + extension
    source_file = find(filename, source_directory)
    if not os.path.isfile(source_file):
        print("Could not find file " + source_file)
        sys.exit()
    else:
        dest_file = os.path.join(dest_directory, filename)
        shutil.copy(source_file, dest_file)
        return dest_file


# ##################################
# Create the file structure for a book in Islandora
# ##################################
def create_file_structure(row, source_directory, output_directory, extension):
    # base file name
    base_filename = row[33]

    print("filename = " + base_filename)
    xml_file = os.path.join(output_directory, base_filename + ".xml")
    xmlrow.create_xml_file(row, xml_file)
    new_file = add_obj(source_directory, output_directory, base_filename, extension)
    return new_file


# ########################################
# Main Program
# ########################################
def main():
    # get the csv file input
    aFile = input("Please enter csv file name: ")
    if not os.path.isfile(aFile):
        print("Could not find file " + aFile)
        sys.exit()
    else:
        print("found file ")

    # check for source file pad level
    pad_level = 1
    source_file_pad = input(
        "Please indicate source file page name pad level default is 1 meaning no 0's in front of page: ")
    if source_file_pad:
        pad_level = int(source_file_pad)

    # base directory of files to import
    base_directory = input("Please enter directory of files to import: ")
    if not os.path.isdir(base_directory):
        print("Directory " + base_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + base_directory)

    # output directory for processing
    output_directory = input("Please enter output directory: ")
    if not os.path.isdir(output_directory):
        print("Directory " + output_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + output_directory)

    # open the csv and start iterating through the rows
    with open(aFile, 'r') as csv_file:
        file_reader = csv.reader(csv_file)
        counter = 1

        for row in file_reader:
            print("processing row " + counter )
            create_file_structure(row, base_directory, output_directory)
            counter += 1

if __name__ == '__main__':
    main()
