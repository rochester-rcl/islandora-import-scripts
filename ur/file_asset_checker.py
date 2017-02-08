import os
import csv
import sys
import datetime

# logging data
dateTimeInfo = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")


class FileInfo:
    """Holds basic file information """

    def __init__(self, name, extension, path):
        self.name = name
        self.extension = extension
        self.path = path

    def get_file_name(self):
        return self.name + self.extension

    def get_full_path(self):
        return os.path.join(self.path, (self.name + self.extension))

    def to_string(self):
        return "name = " + self.name + " extension = " + self.extension + " path = " + self.path

    def to_csv(self):
        return self.extension + ", " + self.get_full_path()


# #######################################################
# get a dictionary of asset files - this skips any file that
# does not have an extension set by the user
#
# #######################################################


def get_asset_files(asset_directory, extensions_to_ignore):
    file_list = {}
    for root, sub, files in os.walk(asset_directory):
        for a_file in files:
            (base_file_name, ext) = os.path.splitext(a_file)
            if ext.lower().strip() not in extensions_to_ignore:
                if base_file_name in file_list:
                    file_list[base_file_name].append(FileInfo(base_file_name, ext, root))
                else:
                    file_list[base_file_name] = [FileInfo(base_file_name, ext, root)]
    return file_list


def get_rows(all_files, xml_files):
    all_rows = []

    for key, value in sorted(all_files.items()):
        row = [None] * 4
        row[0] = key
        paths = ""
        has_xml = key in xml_files
        for a_file in list(value):
            paths += a_file.get_full_path() + "\n"
            if a_file.extension.lower() == '.xml':
                has_xml = True

        row[1] = paths
        row[2] = has_xml
        all_rows.append(row)
    return all_rows


def create_csv(rows):
    file_name = 'file_type_counter' + dateTimeInfo + ".csv"
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows)

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
            if ext.lower() in extensions:
                info = FileInfo(base_file_name, ext, root)
                file_list[base_file_name] = info

    return file_list


def main():
    ignore_extensions = input("Please enter a comma separated list of extensions to ignore PERIOD e.g. .txt, .pdf: ")
    # split the extensions
    my_extensions = [x.strip() for x in ignore_extensions.split(',')]

    xml_directory = input("Please enter the top directory where all the xml files exist: ")
    if not os.path.isdir(xml_directory):
        print("Directory " + xml_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + xml_directory)

    # get xml and asset files
    xml_extensions = ".xml".split(",")
    xml_files = get_files(xml_directory, xml_extensions)

    # base directory of files to import
    base_directory = input("Please enter directory where files are located: ")
    if not os.path.isdir(base_directory):
        print("Directory " + base_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + base_directory)

    print("Will ignore extensions: " + str(my_extensions))
    all_files = get_asset_files(base_directory, my_extensions)
    print("num file names " + str(len(all_files)))

    create_csv(get_rows(all_files, xml_files))


if __name__ == '__main__':
    main()
