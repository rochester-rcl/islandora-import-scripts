
import os
import sys
import csv
import logging
import datetime
import csvtoxml as xmlrow
import shutil
import subprocess

# logging info
dateTimeInfo = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

logger1 = logging.getLogger('1')
logger1.addHandler(logging.FileHandler("logs/rbscp_packager_" + dateTimeInfo + ".log"))
logger1.setLevel(logging.INFO)


def get_folder_files(path):
    file_list = {}
    # ##################################
    # find all files
    # ##################################
    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_list[file_name] = os.path.join(root, file_name)

    return file_list


def create_ingestion_package(page_counter, output_directory, file_list, row, params_for_to_pdf):
    print("create ingest package")
    # page level output
    dir_format = "{0:04d}"
    page_dir = os.path.join(output_directory, dir_format.format(page_counter))
    print("CREATING PAGE: " + page_dir)
    os.mkdir(page_dir)

    mods_file = os.path.join(page_dir, "MODS.xml")
    xmlrow.create_xml_file(row, mods_file, page_counter)

    for key in file_list.keys():
        print("Key = " + key + " value " + file_list[key])
        file_name, file_extension = os.path.splitext(key)
        print("file name = " + file_name + " extension = " + file_extension)

        if file_name.endswith("_t"):
            print("is thumbnail")
            dest_file = os.path.join(page_dir, "TN" + file_extension)
            print("dest file = " + dest_file)
            shutil.copy(file_list[key], dest_file)
        else:
            print("not thumbnail")
            if file_extension.lower() == ".tif" or file_extension.lower() == ".tiff":
                dest_file = os.path.join(page_dir, "OBJ" + file_extension)
                print("dest file = " + dest_file)
                shutil.copy(file_list[key], dest_file)
                params_for_to_pdf.append(dest_file + "[0]")
            if file_extension.lower() == ".jp2":
                dest_file = os.path.join(page_dir, "JP2" + file_extension)
                print("dest file = " + dest_file)
                shutil.copy(file_list[key], dest_file)
            if file_extension.lower() == ".jpg":
                dest_file = os.path.join(page_dir, "JPG" + file_extension)
                print("dest file = " + dest_file)
                shutil.copy(file_list[key], dest_file)
            else:
                print("")


def package_files(object_counter,
                  base_directory_path,
                  base_folder_name,
                  start_range,
                  end_range,
                  output_directory,
                  row):
    print(base_folder_name)
    print(start_range)
    print(end_range)

    start = int(start_range)
    end = int(end_range)

    dir_format = "{0:04d}"
    object_dir = os.path.join(output_directory, dir_format.format(object_counter))
    print("CREATING OBJECT DIR: " + object_dir)
    os.mkdir(object_dir)

    mods_file = os.path.join(object_dir, "MODS.xml")
    print("MODS file " + mods_file)
    xmlrow.create_xml_file(row, mods_file)
    page_counter = 1
    params_for_to_pdf = ["convert"]
    for file_name in range(start, end + 1):
        folder_path = base_directory_path + "/" + base_folder_name + str(file_name).zfill(3)
        print("processing " + folder_path)
        file_list = get_folder_files(folder_path)
        create_ingestion_package(page_counter, object_dir, file_list, row, params_for_to_pdf)
        page_counter = page_counter + 1

    pdf_file = os.path.join(object_dir, "PDF.pdf")
    params_for_to_pdf.append(pdf_file)
    for val in params_for_to_pdf:
        print(val)
    p1 = subprocess.Popen(params_for_to_pdf)
    print(p1.communicate())





# parses files with the given format
# [BASE_NAME]-[range]
# example: D_129_Folder_1-004-006
def parse_file_info(object_counter, base_directory_path, folder_name, output_directory, row):
    print(folder_name)
    print(folder_name.find("-"))
    position = folder_name.find("-")
    if position >= 0 and len(folder_name) > 0:
        folder_range = folder_name[position + 1:]
        base_folder_name = folder_name[:position + 1]
        print(base_folder_name)
        print(folder_range)
        number_range = folder_range.split("-")
        print(number_range)
        if len(number_range) == 2:
            package_files(object_counter=object_counter,
                          base_directory_path=base_directory_path,
                          base_folder_name=base_folder_name,
                          start_range=number_range[0],
                          end_range=number_range[1],
                          output_directory=output_directory,
                          row=row)
        elif len(number_range) == 1:
            package_files(object_counter=object_counter,
                          base_directory_path=base_directory_path,
                          base_folder_name=base_folder_name,
                          start_range=number_range[0],
                          end_range=number_range[0],
                          output_directory=output_directory,
                          row=row)
        else:
            print("Range incorrect for " + folder_name + " row " + object_counter)
    else:
        print("File format not correct for " + folder_name + " row " + object_counter)


def process_csv(csv_file, base_directory, output_directory):
    print("processing csv " + csv_file)
    # open the csv and start iterating through the rows
    with open(csv_file, 'r') as csv_file:
        file_reader = csv.reader(csv_file)
        object_counter = 1

        for row in file_reader:
            # xmlrow.print_row(counter, row, 37)
            parse_file_info(object_counter, base_directory, row[33], output_directory, row)
            object_counter += 1


def main():
    # get the csv file input
    csv_file = input("Please enter csv file name: ")
    if not os.path.isfile(csv_file):
        print("Could not find file " + csv_file)
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

    # base directory of files to import
    output_directory = input("Please enter output directory: ")
    if not os.path.isdir(output_directory):
        print("Directory " + output_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + output_directory)

    process_csv(csv_file, base_directory, output_directory)


if __name__ == '__main__':
    main()
