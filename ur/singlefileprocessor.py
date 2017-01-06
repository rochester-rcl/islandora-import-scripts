import os
import sys
import datetime
import logging
import shutil

# logging data
dateTimeInfo = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

logger1 = logging.getLogger('1')
logger1.addHandler(logging.FileHandler("logs/single_file_processor_" + dateTimeInfo + ".log"))
logger1.setLevel(logging.INFO)

logger2 = logging.getLogger('2')
logger2.addHandler(logging.FileHandler("logs/single_file_processor_missing_asset_file_" + dateTimeInfo + ".log"))
logger2.setLevel(logging.INFO)

logger3 = logging.getLogger('3')
logger3.addHandler(logging.FileHandler("logs/single_file_processor_missing_xml_file_" + dateTimeInfo + ".log"))
logger3.setLevel(logging.INFO)


class FileInfo:
    """Holds basic file information """

    def __init__(self, name, extension, path, size):
        self.name = name
        self.extension = extension
        self.path = path
        self.size = size

    def get_file_name(self):
        return self.name + self.extension

    def get_full_path(self):
        return os.path.join(self.path, (self.name + self.extension))

    def to_string(self):
        return ("name = " + self.name + " extension = " + self.extension + " path = " +
                self.path + " size = " + str(self.size))

    def to_csv(self):
        return self.name + ", " + self.get_full_path() + ", " + str(self.size)

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
# Report missing files
# ########################################


def check_missing_files(xml_files, asset_files, stop_on_missing_files):
    xml_file_keys = set(xml_files.keys())
    asset_file_keys = set(asset_files.keys())

    missing_asset_file_keys = xml_file_keys - asset_file_keys
    for xml_key in missing_asset_file_keys:
        logger2.info("missing asset file " + xml_key)

    missing_xml_file_keys = asset_file_keys - xml_file_keys
    for asset_key in missing_xml_file_keys:
        logger3.info("missing xml file " + asset_key)

    if stop_on_missing_files and (len(missing_asset_file_keys) > 0 or len(missing_xml_file_keys) > 0):
        logger1.info("halting due to missing files")
        sys.exit()

# #######################################################
# Combine the assets and xml data into a single folder
#
# offset: offset in the list of xml files to start processing
# maxFilesToProcess: maximum number of files to process
# valid extensions: valid extensions that the asset files can have
# assetDirectorySet: set of asset directories where assets exist
# xmlFileDictionary: dictionary of xml files - base file
#                    name should match the base asset file name
# #######################################################


def create_ingestion_folder(destination_directory, xml_file_dict, asset_file_dict):

    logger1.info("building ingestion folder")
    logger1.info("destination directory " + destination_directory)
    for key, xml_file_info in xml_file_dict.items():
        asset_file_info = asset_file_dict.get(key, None)
        if asset_file_info:
            dest_xml = os.path.join(destination_directory, xml_file_info.get_file_name())
            dest_asset = os.path.join(destination_directory, asset_file_info.get_file_name())
            logger1.info("adding asset file: " + asset_file_info.get_full_path() + " to " + dest_asset)
            logger1.info("adding xml file: " + xml_file_info.get_full_path() + " to " + dest_xml)
            shutil.copy(asset_file_info.get_full_path(), dest_asset)
            shutil.copy(xml_file_info.get_full_path(), dest_xml)
        else:
            logger1.info("asset not processed" + key)

# ########################################
# Main Program
# ########################################


def main():
    valid_extensions = input("Please enter a comma separated list of extensions including PERIOD e.g. .tif, .tiff: ")
    # split the extensions
    my_extensions = valid_extensions.split(",")
    ext_length = len(my_extensions)
    if ext_length == 0:
        print("One or more extensions must be listed")
        sys.exit()

    print("valid extensions = " + valid_extensions)

    xml_directory = input("Please enter the top directory where all the xml files exist: ")
    if not os.path.isdir(xml_directory):
        print("Directory " + xml_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + xml_directory)

    asset_directory = input("Please enter the top directory where all the asset files exist: ")
    if not os.path.isdir(asset_directory):
        print("Directory " + asset_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + asset_directory)

    destination_directory = input("Please enter the directory where all assets will stored for ingestion: ")
    if not os.path.isdir(destination_directory):
        print("Directory " + destination_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + destination_directory)

    stop_on_missing_file = input("Stop on missing file (y/n) default is 'y': ")
    if stop_on_missing_file and stop_on_missing_file.lower() == 'n':
        stop_on_missing_file = False
    else:
        stop_on_missing_file = True

    print("stop on missing file = " + str(stop_on_missing_file))

    # get xml and asset files
    xml_extensions = ".xml".split(",")
    xml_files = get_files(xml_directory, xml_extensions)
    asset_files = get_files(asset_directory, my_extensions)

    logger1.info("xml files is " + str(len(xml_files)))
    logger1.info("asset files is " + str(len(asset_files)))
    check_missing_files(xml_files, asset_files, stop_on_missing_file)
    create_ingestion_folder(destination_directory, xml_files, asset_files)
    print("processing completed")


# ########################################
# Determine if main program should be run
# ########################################


if __name__ == '__main__':
    main()

