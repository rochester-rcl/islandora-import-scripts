import os
import sys
import csv
import logging
import datetime
import shutil
import subprocess

# logging info
dateTimeInfo = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

logger1 = logging.getLogger('1')
logger1.addHandler(logging.FileHandler("logs/rbscp_packager_with_mods_" + dateTimeInfo + ".log"))
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


def create_ingestion_package(page_counter, output_directory, file_list, orig_mods_file, generate_thumb, pdf_tif_files):
    print("create ingest package")
    # page level output
    dir_format = "{0:04d}"
    page_dir = os.path.join(output_directory, dir_format.format(page_counter))
    print("CREATING PAGE: " + page_dir)
    os.mkdir(page_dir)

    mods_file = os.path.join(page_dir, "MODS.xml")
    shutil.copy(orig_mods_file, mods_file)
    for key in file_list.keys():
        print("Key = " + key + " value " + file_list[key])
        file_name, file_extension = os.path.splitext(key)
        print("file name = " + file_name + " extension = " + file_extension)

        if file_name.endswith("_t"):
            if not generate_thumb:
                print("is thumbnail")
                dest_file = os.path.join(page_dir, "TN" + file_extension)
                print("dest file = " + dest_file)
                shutil.copy(file_list[key], dest_file)
            else:
                print("thumbnail must be generated")
        elif file_name.endswith("_PDF"):
            print("is tiff file for pdf")
            pdf_tif_files.append(file_list[key])
        else:
            print("not thumbnail")
            if file_extension.lower() == ".tif" or file_extension.lower() == ".tiff":
                dest_file = os.path.join(page_dir, "OBJ" + file_extension)
                print("dest file = " + dest_file)
                shutil.copy(file_list[key], dest_file)
            if file_extension.lower() == ".jp2":
                dest_file = os.path.join(page_dir, "JP2" + file_extension)
                print("dest file = " + dest_file)
                shutil.copy(file_list[key], dest_file)
            if file_extension.lower() == ".jpg":
                dest_file = os.path.join(page_dir, "JPG" + file_extension)
                print("dest file = " + dest_file)
                create_medium_jpg(file_list[key], dest_file)
                if generate_thumb:
                    dest_thumbnail = os.path.join(page_dir, "TN.jpg")
                else:
                    print("thumbnail not generated")
            else:
                print("")


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


def create_pdf(object_dir, pdf_tif_files):
    params_for_to_pdf = ["convert"]
    params_for_to_pdf.append("-density")
    params_for_to_pdf.append("72")
    params_for_to_pdf.append("-compress")
    params_for_to_pdf.append("LZW")
    pdf_temp_file = os.path.join(object_dir, "temp_PDF.pdf")

    for pdf_tif_file in pdf_tif_files:
        params_for_to_pdf.append(pdf_tif_file)

    pdf_final_file = os.path.join(object_dir, "PDF.pdf")
    params_for_to_pdf.append(pdf_temp_file)
    for val in params_for_to_pdf:
        print(val)
    p1 = subprocess.Popen(params_for_to_pdf)
    print(p1.communicate())

    # use gost script to make pdf smaller
    params_for_gs = ["gs"]
    params_for_gs.append("-sDEVICE=pdfwrite")
    params_for_gs.append("-dCompatibilityLevel=1.4")
    params_for_gs.append("-dPDFSETTINGS=/printer")
    params_for_gs.append("-dNOPAUSE")
    params_for_gs.append("-dQUIET")
    params_for_gs.append("-dBATCH")
    params_for_gs.append("-r300")
    params_for_gs.append("-sOutputFile=" + pdf_final_file)
    params_for_gs.append(pdf_temp_file)

    for val in params_for_gs:
        print(val)

    p2 = subprocess.Popen(params_for_gs)
    print(p2.communicate())
    os.remove(pdf_temp_file)


def package_files(object_counter,
                  base_directory_path,
                  base_folder_name,
                  start_range,
                  end_range,
                  output_directory,
                  orig_mods_file,
                  generate_thumb):
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
    shutil.copy(orig_mods_file, mods_file)
    page_counter = 1
    pdf_tif_files = []
    for file_name in range(start, end + 1):
        folder_path = base_directory_path + "/" + base_folder_name + str(file_name).zfill(3)
        print("processing " + folder_path)
        file_list = get_folder_files(folder_path)
        create_ingestion_package(page_counter, object_dir, file_list, orig_mods_file, generate_thumb, pdf_tif_files)
        page_counter = page_counter + 1

    create_pdf(object_dir, pdf_tif_files)


# parses files with the given format
# [BASE_NAME]-[range]
# example: D_129_Folder_1-004-006
def parse_file_info(object_counter, base_directory_path, folder_name, output_directory, orig_mods_file, generate_thumb):
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
                          orig_mods_file=orig_mods_file,
                          generate_thumb=generate_thumb)
        elif len(number_range) == 1:
            package_files(object_counter=object_counter,
                          base_directory_path=base_directory_path,
                          base_folder_name=base_folder_name,
                          start_range=number_range[0],
                          end_range=number_range[0],
                          output_directory=output_directory,
                          orig_mods_file=orig_mods_file,
                          generate_thumb=generate_thumb)
        else:
            print("Range incorrect for " + folder_name + " row " + object_counter)
    else:
        print("File format not correct for " + folder_name + " row " + object_counter)


def process_info(mods_dir, base_directory, output_directory, generate_thumb):
    print("processing mods " + mods_dir)
    object_counter = 0

    # open the csv and start iterating through the rows
    for root, sub, files in os.walk(mods_dir):
        for a_file in files:
            # the base file name of the mods file is also the folder name range
            (base_file_name, ext) = os.path.splitext(a_file)
            full_file_name = os.path.join(root, (base_file_name + ext))
            parse_file_info(object_counter, base_directory, base_file_name, output_directory, full_file_name,
                            generate_thumb)
            object_counter += 1


def main():
    # get the csv file input
    mods_dir = input("Please enter mods directory: ")
    if not os.path.isdir(mods_dir):
        print("Could not find directory " + mods_dir)
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

    generate_thumb = input("Generate thumbnail file (y/n) default is 'n': ")
    if generate_thumb and generate_thumb.lower() == 'y':
        generate_thumb = True
    else:
        generate_thumb = False

    process_info(mods_dir, base_directory, output_directory, generate_thumb)


if __name__ == '__main__':
    main()
