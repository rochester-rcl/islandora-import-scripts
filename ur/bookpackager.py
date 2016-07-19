import csvtoxml as xmlrow
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
def create_page_structure(pages, base_directory, row, base_filename, book_dir, source_file_pad, name_separator):
    # default format - no leading zeros
    page_format = "{0:01d}"

    if 9 < pages < 99:
        # one leading zero
        page_format = "{0:02d}"
    elif 99 < pages < 999:
        # two leading zeros
        page_format = "{0:03d}"
    elif 9999 < pages < 9999:
        # three leading zeros
        page_format = "{0:04d}"

    # exclusive by one so increase by 1
    for page in range(1, pages + 1):
        page_name = page_format.format(page)
        # create the padding format for source file
        source_file_pad_format = "{0:0" + str(source_file_pad) + "d}"
        # source file name
        filename = base_filename + name_separator + source_file_pad_format.format(page) + ".tif"

        print("trying to find filename " + filename + " in directory " + base_directory)
        source_file = find(filename, base_directory)
        if not os.path.isfile(source_file):
            print("Could not find file " + source_file)
            sys.exit()
        else:
            page_dir = os.path.join(book_dir, page_name)
            dest_file = os.path.join(page_dir, "OBJ.tif")
            print("source  = " + source_file + " dest = " + dest_file)
            print("creating directory " + page_dir)
            os.mkdir(page_dir)
            shutil.copy(source_file, dest_file)

            # add page xml data
            xml_file = os.path.join(page_dir, "MODS" + ".xml")
            xmlrow.create_xml_file(row, xml_file, page)


# ##################################
# Add a pdf file to the directory
# ##################################
def add_pdf(pdf_directory, base_filename, book_dir, book_num):
    # source file name
    filename = filename = base_filename + ".pdf"
    print("trying to find filename " + filename + " in directory " + pdf_directory)
    source_file = find(filename, pdf_directory)
    if not os.path.isfile(source_file):
        print("Could not find file " + filename)
        sys.exit()
    else:
        dest_file = os.path.join(book_dir, "PDF")
        shutil.copy(source_file, dest_file)
        print("source  = " + source_file + " dest = " + dest_file)


# ##################################
# Create the file structure for a book in Islandora
# ##################################
def create_file_structure(pages, counter, row, base_directory, output_directory, source_file_pad_level, name_separator):
    # base file name
    base_filename = row[33]

    print("filename = " + base_filename)
    book_dir = os.path.join(output_directory, str(counter))
    print("creating directory " + book_dir)
    os.mkdir(book_dir)
    xml_file = os.path.join(book_dir, "MODS" + ".xml")
    xmlrow.create_xml_file(row, xml_file)
    create_page_structure(pages, base_directory, row, base_filename, book_dir, source_file_pad_level, name_separator)
    return book_dir


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
    source_file_pad = input("Please indicate source file page name pad level default is 1 meaning no 0's in front of page: ")
    if source_file_pad:
        pad_level = int(source_file_pad)

    name_separator = "_"
    source_name_separator = input("Please set filename seperator default is '_': ")
    if source_name_separator:
        name_separator = source_name_separator

    # base directory of files to import
    base_directory = input("Please enter directory of files to import: ")
    if not os.path.isdir(base_directory):
        print("Directory " + base_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + base_directory)

    #pdf information if applicable
    pdf_directory = None
    has_pdf_files = input("Are there separate PDF files to import (Yes/No) default is No: ")
    if has_pdf_files.lower() == "yes":
        # base directory of files to import
        pdf_directory = input("Please enter PDF directory of files to import: ")
        if not os.path.isdir(pdf_directory):
            print("Directory " + pdf_directory + " does not exist or is not a directory")
            sys.exit()
        else:
            print("PDF directory found " + pdf_directory)

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
            if row[31] or row[32]:

                pages = 0
                #default to number of files first
                if row[32]:
                    pages = int(row[32])
                elif row[31]:
                    pages = int(row[31])

                if pages > 0:
                    print("processing " + str(pages) + " pages")
                    book_dir = create_file_structure(pages, counter, row, base_directory, output_directory, pad_level, name_separator)
                    if has_pdf_files:
                        print("adding pdf file ")
                        base_file_name = row[33]
                        add_pdf(pdf_directory, base_file_name, book_dir, counter)
                else: 
                    print("pages was 0")
            else:
                print("Skipping row " + str(counter) + " no pages found were found " + row[31])
            counter += 1

if __name__ == '__main__':
    main()
