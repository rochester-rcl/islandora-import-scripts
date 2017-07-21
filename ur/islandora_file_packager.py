import os
import logging
import datetime
import sys
import shutil

# logging info
dateTimeInfo = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

logger1 = logging.getLogger('1')
logger1.addHandler(logging.FileHandler("logs/aids_export_general_" + dateTimeInfo + ".log"))
logger1.setLevel(logging.INFO)


logger2 = logging.getLogger('3')
logger2.addHandler(logging.FileHandler("logs/aids_export_csv_" + dateTimeInfo + ".csv"))
logger2.setLevel(logging.INFO)


# #######################################################
# get a dictionary of asset files - this skips any file that
# does not have an extension set by the user
# #######################################################
def get_files(dictionary, directory, extensions):
    for root, sub, files in os.walk(directory):
        for a_file in files:
            (base_file_name, ext) = os.path.splitext(a_file)
            if ext.lower() in extensions:
                dictionary[base_file_name] = os.path.join(root, (base_file_name + ext))


# #######################################################
# Processes the files int sets of a given size
#
# offset: offset in the list of xml files to start processing
# maxFilesToProcess: maximum number of files to process
# valid extensions: valid extensions that the asset files can have
# assetDirectorySet: set of asset directories where assets exist
# xmlFileDictionary: dictionary of xml files - base file
#                    name should match the base asset file name
# #######################################################
def process_files(offset, max_files_to_process, xml_file_dictionary, asset_file_dictionary, dest_directory):
    processed = 0
    asset_missing_counter = 0
    total = 0

    num_items = len(xml_file_dictionary)

    if not max_files_to_process:
        max_files_to_process = num_items
    else:
        max_files_to_process = int(max_files_to_process)

    print("max files to process = " + str(max_files_to_process))
    logger1.info("max files to process = " + str(max_files_to_process))

    if num_items > 0:
        print("total xml files " + str(num_items))
        logger1.info("total xml files " + str(num_items))

        # sort the keys
        sorted_keys = sorted(xml_file_dictionary)

        end = offset + max_files_to_process
        if end > num_items:
            end = len(num_items)

    print("processing " + str(offset) + " to " + str(end))
    logger1.info("processing (inclusive)" + str(offset) + " to (exclusive) " + str(end))
    subset = sorted_keys[offset: end]

    for key in subset:
        print("processing key " + key)
        logger1.info("processing key " + key)
        asset = asset_file_dictionary.get(key)
        xml = xml_file_dictionary.get(key)

        if xml is not None and asset is not None:
            print("found asset file " + asset)
            logger1.info("found asset file " + asset)
            dest_xml_file = os.path.join(dest_directory, key + ".xml")
            (base_file_name, ext) = os.path.splitext(asset)
            dest_asset_file = os.path.join(dest_directory, key + ext)
            print("dest xml file = " + dest_xml_file + "dest asset file " + dest_asset_file)
            logger1.info("dest xml file = " + dest_xml_file + "dest asset file " + dest_asset_file)
            logger2.info(key + ", " + xml + ", " + asset)
            shutil.copy(xml, dest_xml_file)
            shutil.copy(asset, dest_asset_file)
            processed = processed + 1
        else:
            if asset is None and xml is None:
                logger2.info(key + ",,")
            elif asset is None:
                logger2.info(key + ", " + xml + ",")
                print("asset file NOT found for key " + key)
                logger1.info("ERROR: asset file NOT found for key " + key)
            elif xml is None:
                logger2.info(key + ", , " + asset)
                print("xml file NOT found for key " + key)
                logger1.info("ERROR: asset file NOT found for key " + key)

    print(
        "processed = " + str(processed) + " asset_missing_counter = " + str(asset_missing_counter) + " total = " + str(
            total))
    logger1.info(
        "processed = " + str(processed) + " asset_missing_counter = " + str(asset_missing_counter) + " total = " + str(
            total))


# #######################################################
# get a dictionary of asset files - this skips any file that
# does not have an extension set by the user
# #######################################################
def get_all_asset_files(asset_directory_set, extensions):
    asset_dictionary = {}

    for directory in asset_directory_set:
        print("processing assets in " + directory)
        logger1.info("processing assets in " + directory)
        get_files(asset_dictionary, directory, extensions)

    return asset_dictionary


# ########################################
# Main Program
# ########################################
def main():
    max_files_to_process = input("Please enter maximum number of files to process enter to process all: ")
    offset = input("Please enter the offset position (inclusive) press enter to start from the beginning: ")

    if not offset:
        offset = 0
    else:
        offset = int(offset)

    valid_extensions = input("Please enter a comma separated list of extensions e.g. tif, tiff: ")

    # output directory for processing
    output_directory = input("Please enter output directory: ")
    if not os.path.isdir(output_directory):
        print("Directory " + output_directory + " does not exist or is not a directory")
        logger1.info("ERROR: Directory " + output_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + output_directory)

    num_files_in_output = len([name for name in os.listdir(output_directory) if os.path.isfile(os.path.join(output_directory, name))])
    if num_files_in_output > 0:
        print("output directory " + output_directory + " is not empty has " + str(num_files_in_output) + " files")
        logger1.info("ERROR: output directory " + output_directory + " is not empty has " + str(num_files_in_output) + " files")
        sys.exit()

    xml_directory = input("Please enter the top directory where all the xml files exist: ")
    if not os.path.isdir(xml_directory):
        print("Directory " + xml_directory + " does not exist or is not a directory")
        logger1.info("ERROR: Directory " + xml_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + xml_directory)
        logger1.info("Directory found " + xml_directory)

    xml_file_dictionary = {}
    get_files(xml_file_dictionary, xml_directory, [".xml"])

    num_xml_files = len(xml_file_dictionary)
    print("found " + str(num_xml_files) + " xml files")
    logger1.info("found " + str(num_xml_files) + " xml files")

    if num_xml_files <= 0:
        print("ERROR: no xml files found ")
        logger1.info("ERROR: no xml files found")
        sys.exit()

    for key, file in xml_file_dictionary.items():
        print("found key " + key + " file " + file)

    asset_directories = []

    num_directories = int(input("Please enter the total number of asset directories: "))

    for n in range(0, num_directories):
        asset_directory = input("Please enter the " + str(n + 1) + " directory where all the assets exist: ")

        if not os.path.isdir(asset_directory):
            print("Directory " + asset_directory + " does not exist or is not a directory")
            logger1.info("Directory " + asset_directory + " does not exist or is not a directory")
            sys.exit()
        else:
            print("Asset directory found " + asset_directory)
            logger1.info("Asset directory found " + asset_directory)
            asset_directories.append(asset_directory)

    # convert to set to guarantee uniqueness
    asset_directory_set = set(asset_directories)

    for a_directory in asset_directory_set:
        print("Set directory = " + a_directory)
        logger1.info("Set directory = " + a_directory)

    # split the extensions
    my_extensions = valid_extensions.split(",")
    ext_length = len(my_extensions)
    if ext_length == 0:
        print("One or more extensions must be listed")
        logger1.info("ERROR: One or more extensions must be listed")
        sys.exit()

    for index in range(0, ext_length):
        print("adding extension " + my_extensions[index])
        logger1.info("adding extension " + my_extensions[index])
        my_extensions[index] = "." + my_extensions[index].strip().lower()

    assets_dictionary = get_all_asset_files(asset_directory_set, my_extensions)
    for key, file in assets_dictionary.items():
        print("found key " + key + " file " + file)

    process_files(offset, max_files_to_process, xml_file_dictionary, assets_dictionary, output_directory)

if __name__ == '__main__':
    main()
