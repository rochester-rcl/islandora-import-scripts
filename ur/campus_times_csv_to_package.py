#!/usr/bin/python

import csv
import xml.etree.ElementTree as elementTree
import os
import sys
import shutil
import subprocess
import pdfpagetojpg

# ##########################################
# Build the xml file using the MODS classes
# ##########################################


def build_page_xml(row, template, output_dir):
    print('build page xml')

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

    # number of pages is one for the page template
    physical_description = root.find("physicalDescription")
    extent = physical_description.find('extent')
    extent.text = "1"

    note = root.find("note")
    note_text = note.text
    note.text = note_text.replace("[Title]", row[1])

    new_tree = elementTree.ElementTree(root)
    mods_file = os.path.join(output_dir, "MODS.xml")
    new_tree.write(mods_file)


# ##########################################
# Create the ingestion package
# ##########################################


def create_page_package(page_counter, output_directory, tiff_file, template, row):
    print("create ingest package")
    # page level output
    dir_format = "{0:04d}"
    page_dir = os.path.join(output_directory, dir_format.format(page_counter))
    print("CREATING PAGE: " + page_dir)
    os.mkdir(page_dir)

    print("tiff file = " + tiff_file)

    dest_file = os.path.join(page_dir, "OBJ.tif")
    print("dest file = " + dest_file)
    shutil.copy(tiff_file, dest_file)

    create_medium_jpg(dest_file, os.path.join(page_dir, "JPG.jpg"))
    create_tn_jpg(dest_file,  os.path.join(page_dir, "TN.jpg"))

    build_page_xml(row, template, page_dir)


def create_medium_jpg(source_file, dest_file):
    print("Creating medium JPG")
    params_for_to_jpg = ["convert"]
    params_for_to_jpg.append(source_file)
    params_for_to_jpg.append("-resize")
    params_for_to_jpg.append("600 x 800")
    params_for_to_jpg.append("-quality")
    params_for_to_jpg.append("75")
    params_for_to_jpg.append(dest_file)
    p1 = subprocess.Popen(params_for_to_jpg)
    print(p1.communicate())


def create_tn_jpg(source_file, dest_file):

    print("Creating Thumbnail")
    params_for_to_jpg = ["convert"]
    params_for_to_jpg.append(source_file)
    params_for_to_jpg.append("-resize")
    params_for_to_jpg.append("200 x 200")
    params_for_to_jpg.append("-quality")
    params_for_to_jpg.append("75")
    params_for_to_jpg.append(dest_file)
    p1 = subprocess.Popen(params_for_to_jpg)
    print(p1.communicate())

# ##########################################
# Build the xml file using the MODS classes
# ##########################################
def build_package_xml(row, template, output_dir):
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
    mods_file = os.path.join(output_dir, "MODS.xml")
    new_tree.write(mods_file)


def get_tiff_files(key, tiff_dir):
    tiff_files = []
    path = os.path.join(tiff_dir, key)
    print("Checking for tiffs for key " + key + "path = " + path)
    for (root, sub, files) in os.walk(path):
        for a_file in files:
            if a_file.lower().endswith(('.tiff', '.tif')):
                tiff_files.append(os.path.join(root, a_file))
    return tiff_files


def build_package(object_counter, row, template, output_dir, tiff_dir):
    print("build package")

    dir_format = "{0:04d}"
    object_dir = os.path.join(output_dir, dir_format.format(object_counter))
    print("CREATING OBJECT DIR: " + object_dir)
    os.mkdir(object_dir)
    build_package_xml(row, template, object_dir)

    folder_path = str(row[7])
    print("processing " + folder_path)
    print("key " + str(row[0]))

    tiff_files = get_tiff_files(str(row[0]), tiff_dir)
    counter = 1
    for tiff_file in tiff_files:
        print(tiff_file)
        create_page_package(counter, object_dir, tiff_file, template, row)
        counter += 1

    # copy pdf file
    pdf_file = str(row[7])
    pdf_dest_file = os.path.join(object_dir, "OBJ.pdf")
    print(" copying " + pdf_file + " to " + pdf_dest_file)
    shutil.copy(pdf_file, pdf_dest_file)
    tn_dest_file = os.path.join(object_dir, "TN.jpg")
    pdfpagetojpg.convert_pdf_page(pdf_dest_file, 400, tn_dest_file)


def process_csv(csv_file, template, output_dir, tiff_dir):
    with open(csv_file, 'r') as csv_file:
        file_reader = csv.reader(csv_file)
        next(file_reader, None)  # skip the headers
        counter = 1
        for row in file_reader:
            build_package(counter, row, template, output_dir, tiff_dir)
            counter += 1


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
    csv_file = '/Users/ndsarr/rcl/campus-times-data/csv-reports/tcw_back.csv'

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

    # tiff_directory = input("Please enter tiff directory: ")
    tiff_directory = '/Volumes/msm-8tb-drive-cts/TIFF'
    if not os.path.isdir(tiff_directory):
        print("Directory " + tiff_directory + " does not exist or is not a directory")
        sys.exit()

    print("Print directory found " + tiff_directory)

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
            process_csv(csv_file, template_file, output_directory, tiff_directory)


if __name__ == '__main__':
    main()
