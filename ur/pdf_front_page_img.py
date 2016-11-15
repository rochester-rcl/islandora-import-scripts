#!/usr/bin/python

import os
import sys
import shutil
import re
import pdfpagetojpg


# pull list of SORTED item IDs from folder where XML files are stored
# (assumes Jeff will create one XML file / item and place them in a directory)
def get_file_list(file_directory):
    fileList = []
    for root, sub, files in os.walk(file_directory):
            for item in files:
                if item.endswith(".pdf"):
                    print("adding file " + os.path.join(root,item))
                    fileList.append(os.path.join(root,item))
                else: 
                    print("Skipping file " + item + " name pattern did not match")
    return fileList
    


# ##################################
# Create the file structure for a book in Islandora
# ##################################
def add_derivative(file, destination):
    print("add derivative")
    pdfpagetojpg.convert_pdf_page(file,  400, destination)

# ########################################
# Main Program
# ########################################
def main():
   
    # base directory of files to import
    base_directory = input("Please enter directory of files to create pdf front page image: ")
    if not os.path.isdir(base_directory):
        print("Directory " + base_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + base_directory)
        file_list = get_file_list(base_directory)
        print("processing " + str(len(file_list)))
        for my_file in file_list:
            print("found file " + my_file)
            dir_name = os.path.dirname(my_file)
            dest_file_name = dir_name + "\\" + "TN.jpg"
            add_derivative(my_file, dest_file_name)

if __name__ == '__main__':
    main()
