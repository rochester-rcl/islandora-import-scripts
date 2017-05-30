import os
import logging
import datetime
import sys

# logging info
dateTimeInfo = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

logger1 = logging.getLogger('1')
logger1.addHandler(logging.FileHandler("logs/aids_export_general_" + dateTimeInfo + ".log"))
logger1.setLevel(logging.INFO)

logger1 = logging.getLogger('2')
logger1.addHandler(logging.FileHandler("logs/aids_export_no_xml_file_" + dateTimeInfo + ".log"))
logger1.setLevel(logging.INFO)

logger2 = logging.getLogger('3')
logger2.addHandler(logging.FileHandler("logs/no_asset_file_" + dateTimeInfo + ".log"))
logger2.setLevel(logging.INFO)

logger3 = logging.getLogger('4')
logger3.addHandler(logging.FileHandler("logs/no_asset_file_found_" + dateTimeInfo + ".log"))
logger3.setLevel(logging.INFO)


class FileInfo:
    """Holds basic file information """

    def __init__(self, name, extension, path, size):
        self.name = name
        self.extension = extension
        self.path = path
        self.size = size
        self.asset = None

    def get_full_path(self):
        return os.path.join(self.path, (self.name + self.extension))

    def to_string(self):
        return "name = " + self.name + " exension = " + self.extension + " path = " + self.path + " size = " + str(
            self.size)

    def to_csv(self):
        return self.name + ", " + self.get_full_path() + ", " + str(self.size)


# #######################################################
# get a dictionary of asset files - this skips any file that
# does not have an extension set by the user
# #######################################################
def get_asset_files(asset_directory, extensions, xml_files):
    for root, sub, files in os.walk(asset_directory):
        for a_file in files:
            (base_file_name, ext) = os.path.splitext(a_file)
            file_size = os.path.getsize(os.path.join(root, a_file))
            info = FileInfo(base_file_name, ext, root, file_size)
            if ext.lower() in extensions:
                if base_file_name in xml_files:
                    xml_files[base_file_name].asset = info
                else:
                    logger2.info(info.to_csv())  # file does not exist in xml file set
            else:
                logger3.info(info.to_csv())  # file does not have correct extension


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
def process_files(offset, max_files_to_process, valid_extensions, asset_directory_set, xml_file_dictionary):
    if not offset:
        offset = 0

    for directory in asset_directory_set:
        get_asset_files(directory, valid_extensions, xml_file_dictionary)

    processed = 0
    asset_missing_counter = 0
    total = 0

    xml_with_asset = []
    for key, file_info in xml_file_dictionary.items():
        total = total + 1
        if file_info.asset is None:
            logger2.info((file_info.getFullPath()))  # no asset file foound
            asset_missing_counter = asset_missing_counter + 1
        else:
            xml_with_asset.append(file_info)  # add the asset to list
            processed = processed + 1
    print(
        "processed = " + str(processed) + " assetMissingCounter = " + str(asset_missing_counter) + " total = " + str(
            total))
    logger1.info(
        "processed = " + str(processed) + " assetMissingCounter = " + str(asset_missing_counter) + " total = " + str(
            total))

    num_items = len(xml_with_asset)
    if num_items > 0:
        print("total items found with asset " + num_items)

        # sort the list
        sorted_with_asset = sorted(xml_with_asset, key=lambda data: data.asset.size)

        end = offset + max_files_to_process
        if end > num_items:
            end = len(num_items)

    print("processing " + str(offset) + " to " + str(end))
    logger1.info("processing " + str(offset) + " to " + str(end))

    subset = sorted_with_asset[offset: end]

    for my_data in subset:
        print("file " + my_data.to_csv())
        logger1.info(my_data.to_csv())

    print("processed a total of " + len(subset))


# #######################################################
# get a dictionary of xml files - this skips any file that
# does not have an .xml file extension
# #######################################################
def get_xml_files(xml_directory):
    file_list = {}
    for root, sub, files in os.walk(xml_directory):
        for a_file in files:
            (base_file_name, ext) = os.path.splitext(a_file)
            # we only want xml files
            if ext == ".xml":
                info = FileInfo(base_file_name, ext, root, 0)
                file_list[base_file_name] = info
            else:
                print("skipping file " + a_file)
                logger1.info()
    return file_list


# ########################################
# Main Program
# ########################################
def main():
    max_files_to_process = input("Please enter maximum number of files to process enter to process all: ")
    offset = input("Please enter the offset position (inclusive) press enter to start from the beginning: ")
    valid_extensions = input("Please enter a comma separated list of extensions e.g. tif, tiff: ")

    xml_directory = input("Please enter the top directory where all the xml files exist: ")
    if not os.path.isdir(xml_directory):
        print("Directory " + xml_directory + " does not exist or is not a directory")
        logger1.info("Directory " + xml_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + xml_directory)
        logger1.info("Directory found " + xml_directory)

    xml_file_dictionary = get_xml_files(xml_directory)

    num_xml_files = len(xml_file_dictionary)
    print("found " + str(num_xml_files) + " xml files")
    logger1.info("found " + str(num_xml_files) + " xml files")

    if num_xml_files <= 0:
        print("ERROR: no xml files found ")
        logger1.info("ERROR: no xml files found")
        sys.exit()

    asset_directories = []

    num_directories = int(input("Please enter the total number of asset directories: "))

    for n in range(0, num_directories):
        asset_directory = input("Please enter the " + str(n + 1) + " directory where all the assets exist: ")

        if not os.path.isdir(asset_directory):
            print("Directory " + asset_directory + " does not exist or is not a directory")
            logger1.info("Directory " + asset_directory + " does not exist or is not a directory")
            sys.exit()
        else:
            print("Directory found " + asset_directory)
            logger1.info("Directory found " + asset_directory)
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
        logger1.info("One or more extensions must be listed")
        sys.exit()

    for index in range(0, ext_length):
        print("altering value " + my_extensions[index] + " at index " + str(index))
        logger1.info("altering value " + my_extensions[index] + " at index " + str(index))
        my_extensions[index] = "." + my_extensions[index].strip().lower()

    process_files(offset, max_files_to_process, my_extensions, asset_directory_set, xml_file_dictionary)

if __name__ == '__main__':
    main()
