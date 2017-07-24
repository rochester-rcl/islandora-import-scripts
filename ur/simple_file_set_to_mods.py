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

    # title of the poster (file name in this case)
    title_info = mods.TitleInfo()
    title_info_element = title_info.to_mods_element(root)
    title = mods.Title()
    title.value = base_file_name
    title.to_mods_element(title_info_element)

    # set the mods file identifier
    mods_file_identifier = mods.Identifier()
    mods_file_identifier.value = base_file_name
    mods_file_identifier.type = 'local'
    mods_file_identifier.display_label = 'AP number'
    mods_file_identifier.to_mods_element(root)

    # related item series information
    related_item = mods.RelatedItem()
    related_item.type = 'series'
    related_item_element = related_item.to_mods_element(root)
    title_info2 = mods.TitleInfo()
    title_info_element = title_info2.to_mods_element(related_item_element)
    title2 = mods.Title()
    title2.value = "Outreach: Posters"
    title2.to_mods_element(title_info_element)

    # physical description information / internet media type
    physical_description_element = mods.PhysicalDescription().to_mods_element(root)

    form = mods.Form()
    form.authority = "marcform"
    form.value = "nonprojected graphic"
    form.to_mods_element(physical_description_element)

    internet_media_type = mods.InternetMediaType()
    internet_media_type.value = "image/tiff"
    internet_media_type.to_mods_element(physical_description_element)

    # type of resource
    type_of_resource = mods.TypeOfResource()
    type_of_resource.value = "still image"
    type_of_resource.to_mods_element(root)

    # genre
    genre = mods.Genre()
    genre.authority = "lctgm"
    genre.value = "Posters"
    genre.to_mods_element(root)

    # host information
    related_item2 = mods.RelatedItem()
    related_item2.type = 'host'
    related_item_element2 = related_item2.to_mods_element(root)

    title_info3 = mods.TitleInfo()
    title_info_element3 = title_info3.to_mods_element(related_item_element2)
    title3 = mods.Title()
    title3.value = "AIDS Education Collection"

    title3.to_mods_element(title_info_element3)

    location = mods.Location()
    location_element = location.to_mods_element(related_item_element2)

    url = mods.Url()
    url.display_label = "Finding aid to collection"
    url.value = "http://rbscp.lib.rochester.edu/aids-education-collection"
    url.to_mods_element(location_element)

    # location information

    location2 = mods.Location()
    location_element = location2.to_mods_element(root)

    physical_location = mods.PhysicalLocation()
    physical_location.type = "text"
    physical_location.value = "University of Rochester, River Campus Libraries, Department of " \
                              "Rare Books, Special Collections & Preservation"
    physical_location.to_mods_element(location_element)

    # access condition
    access_condition = mods.AccessCondition()
    access_condition.type = "use and reproduction"
    access_condition.xlink = "http://rightsstatements.org/page/CNE/1.0/"
    access_condition.value = "The copyright and related rights status of this Item has " \
                             "not been evaluated. Please refer to the organization that has made " \
                             "the Item available for more information. You are free to use this Item " \
                             "in any way that is permitted by the copyright and related rights legislation " \
                             "that applies to your use. " \
                             "See more here: http://rightsstatements.org/page/CNE/1.0/?language=en"
    access_condition.to_mods_element(root)

    # second access condition

    access_condition2 = mods.AccessCondition()
    access_condition2.type = "copyrightHolder"
    access_condition2.display_label = "Information for copyright holder"
    access_condition2.value = "If you are the copyright holder for materials in this collection and have " \
                              "suggestions for amending the  metadata, or would prefer that the image of " \
                              "the item(s) not appear on this website, please contact us: " \
                              "rarebks@library.rochester.edu. We ask that you consider the value your work " \
                              "has in adding to a comprehensive understanding of the efforts to educate and " \
                              "inform people of HIV and AIDS prevention as you make your decision regarding " \
                              "removal of your copyrighted image."

    access_condition2.to_mods_element(root)

    # note for preferred citation
    note = mods.Note()
    note.type = "preferred citation"
    note.value = "[Item title, item date], AIDS Education Collection; Department of Rare Books, Special " \
                 "Collections, and Preservation; River Campus Libraries, University of Rochester."
    note.to_mods_element(root)

    # record information

    record_info_element = mods.RecordInfo().to_mods_element(root)
    record_source = mods.RecordContentSource()
    record_source.value = "University of Rochester, River Campus Libraries"
    record_source.to_mods_element(record_info_element)

    lang_of_cat_element = mods.LanguageOfCataloging().to_mods_element(record_info_element)
    record_language = mods.LanguageTerm()
    record_language.value = "eng"
    record_language.type = "code"
    record_language.authority = "iso639-2b"
    record_language.to_mods_element(lang_of_cat_element)

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
                info = FileInfo(base_file_name, ext, root)
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

    valid_extensions = input("Please enter a comma separated list of extensions including "
                             "PERIOD e.g. .tif, .tiff: ")
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