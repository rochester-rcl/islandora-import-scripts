#!/usr/bin/python

import csvtoxml as xmlrow
import os
import csv
import sys
import shutil


# ##################################
# find first file with the specified name
# in the base path - walks the directory tree
# ##################################
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    

# ##################################
# Create the file structure for a book in Islandora
# ##################################
def create_file_structure(counter, row, base_directory, output_directory):
    # base file name
    base_filename = row[33]
    source_file = find(base_filename, base_directory)
    if source_file is None or not os.path.isfile(source_file):
        print("Asset file NOT found " + base_filename)
    else:
        page_format = "{0:04d}"
        folder_name = page_format.format(counter)
        print("filename = " + base_filename)
        object_dir = os.path.join(output_directory, folder_name)
        print("creating directory " + object_dir)
        os.mkdir(object_dir)
        xml_file = os.path.join(object_dir, "MODS" + ".xml")
        xmlrow.create_xml_file(row, xml_file)
        filename, file_extension = os.path.splitext(source_file)
        dest_file = os.path.join(object_dir, "OBJ" + file_extension)
        print("source file = " + str(source_file) + " dest file = " + str(dest_file))
        shutil.copy(source_file, dest_file)
   
    return source_file


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
            if row[33]:
                print("Processing file " + row[33]  + " row = " + str(counter) )
                create_file_structure(counter, row, base_directory, output_directory)
            else:
                print("No file name found for row " + str(counter))
            counter += 1


if __name__ == '__main__':
    main()
