import os
import sys
from fileinfo import FileInfo
import logging
import datetime
import mods
import xml.etree.ElementTree as ET

# logging data
dateTimeInfo = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

logger1 = logging.getLogger('1')
logger1.addHandler(logging.FileHandler("logs/single_file_asset_to_mods_" + dateTimeInfo + ".log"))
logger1.setLevel(logging.INFO)

# ##########################################
# Build the xml file using the MODS classes
# ##########################################


def build_xml(base_file_name):
    print('build xml')
    root = ET.Element('mods', {"xmlns:xlink": "http://www.w3.org/1999/xlink",
                               "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                               "xmlns": "http://www.loc.gov/mods/v3",
                               "version": "3.5",
                               "xsi:schemaLocation": "http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd"})

    title_info = mods.TitleInfo()
    title_info_element = title_info.to_mods_element(root)
    title = mods.Title()
    title.value = base_file_name
    title.to_mods_element(title_info_element)

    mods_file_identifier = mods.Identifier()
    mods_file_identifier.value = base_file_name
    mods_file_identifier.type = 'local'
    mods_file_identifier.display_label = 'AP number'
    mods_file_identifier.to_mods_element(root)

    return root

# #######################################################
# get a dictionary of asset files - this skips any file that
# does not have an extension set by the user
#
# #######################################################


def get_files(asset_directory, extensions):
    file_list = {}
    for root, sub, files in os.walk(asset_directory):
        for a_file in files:
            (base_file_name, ext) = os.path.splitext(a_file)
            logger1.info("checking " + base_file_name + " ext " + ext)
            if ext.lower() in extensions:
                logger1.info("found file: " + base_file_name + ext)
                info = FileInfo(base_file_name, ext, root, 0)
                file_list[base_file_name] = info

    return file_list


# ########################################
# Process the files - creating an xml file
# and build xml file
# ########################################

def process_files(asset_directory, output_directory, extensions):
    print("processing")
    asset_list = get_files(asset_directory, extensions)

    for key, file_info in asset_list.items():
        print("key = " + key + " info = " + file_info.to_string())
        root_node = build_xml(key)
        tree = ET.ElementTree(root_node)
        xml_file = os.path.join(output_directory, key + ".xml")
        print(xml_file)
        tree.write(xml_file)


# ########################################
# Main Program
# ########################################


def main():

    print("main program")

    valid_extensions = input("Please enter a comma separated list of extensions including PERIOD e.g. .tif, .tiff: ")
    # split the extensions
    my_extensions = valid_extensions.split(",")
    ext_length = len(my_extensions)
    if ext_length == 0:
        print("One or more extensions must be listed")
        sys.exit()

    print("valid extensions = " + valid_extensions)

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

    process_files(base_directory, output_directory, my_extensions)


if __name__ == '__main__':
    main()