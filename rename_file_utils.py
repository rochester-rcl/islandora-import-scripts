#!/usr/bin/python
import os
import re

#date matching patterns
basic_date_match = "(\d{4,4})(\d{2,2})(\d{2,2})"

# ##################################
# pull list of SORTED item IDs from folder where XML files are stored
# (assumes Jeff will create one XML file / item and place them in a directory)
# ##################################
def get_folder_list(process_directory):
    dir_list = {}
    for root, sub, files in os.walk(process_directory):
        for item in sub:
            path =  os.path.join(root,item)
            x = item.split('_')
            matchInfo = re.match(basic_date_match, x[1])
            #YYYY-MM-DD
            new_file = "T_C_" + matchInfo.group(1) + "_" + matchInfo.group(2) + "_" + matchInfo.group(3)
            src = os.path.join(root, item)
            dest = os.path.join(root, new_file)
            print(src)
            print(dest)
            os.rename(src, dest)

# ########################################
# process the files
# ########################################
def rename_files(process_directory):
    print("directory = " + process_directory)
    get_folder_list(process_directory)
    

    
# ########################################
# Main Program - if needed
# ########################################

def main():
    process_directory = input("Please enter directory of files to rename : ")
    if not os.path.isdir(process_directory):
        print("Directory " + process_directory + " does not exist or is not a directory")
        sys.exit()

    rename_files(process_directory)

if __name__ == '__main__':
    main()

