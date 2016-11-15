import os
import sys
from xml.dom.minidom import parse
import xml.dom.minidom

# ##########################################################
# This iterates through the empty closet collection xml files
# and fixes the titles by adding the Month and year in parenthesis
# ##########################################################


month_dict = {'00': 'Unknown',
              '01': 'January',
              '02': 'February',
              '03': 'March',
              '04': 'April',
              '05': 'May',
              '06': 'June',
              '07': 'July',
              '08': 'August',
              '09': 'September',
              '10': 'October',
              '11': 'November',
              '12': 'December'}

# get the date information - return the new string


def get_date_info(name):
    parts = name.split('-')
    year = '0000'
    month = '00'
    if len(parts) > 1:
        year = parts[0]
        month = parts[1]
    return month_dict.get(month, 'Unknown') + ' ' + year

# create the list of files that need to be processed


def get_file_list(file_directory):
    file_list = []
    for root, sub, files in os.walk(file_directory):
        for item in files:
            if item.endswith(".xml"):
                print("adding file " + os.path.join(root, item))
                file_list.append(os.path.join(root, item))
            else:
                print("Skipping file " + item + " name pattern did not match")
    return file_list


# process each file
# read in - fix the element then write back out over the existing file

def process_file(file):
    print("process file " + file)
    dom_tree = xml.dom.minidom.parse(file)
    collection = dom_tree.documentElement
    date_created_element = collection.getElementsByTagName("dateCreated")[0]
    date_created = date_created_element.childNodes[0].data
    date_info = get_date_info(date_created)
    print(date_info)
    title_element = collection.getElementsByTagName("title")[0]
    title = title_element.childNodes[0].data
    new_title = title + " (" + date_info + ")"
    print(new_title)
    title_element.childNodes[0].replaceWholeText(new_title)
    file_handle = open(file, "w")
    collection.writexml(file_handle)
    file_handle.close()


# process the set of files


def process_files(directory):
    print("process files in directory " + directory)
    file_list = get_file_list(directory)
    for file in file_list:
        process_file(file)


# ########################################
# Main Program
# ########################################


def main():
    # base directory of files to import
    base_directory = input("Please enter directory of files to import: ")
    if not os.path.isdir(base_directory):
        print("Directory " + base_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + base_directory)
        process_files(base_directory)


if __name__ == '__main__':
    main()
