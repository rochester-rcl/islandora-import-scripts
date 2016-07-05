#!/usr/bin/python

import csv
import xml.etree.ElementTree as ET
import os
import sys
import shutil


# #########################################################
# Represents all the metadata classes for import
# #########################################################
class RecordInfo:
    """Holds record info information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'recordInfo')

        if self.value:
            top_level.text = self.value.strip()

        return top_level


class RecordContentSource:
    """Holds content source information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'recordContentSource')

        if self.value:
            top_level.text = self.value.strip()

        return top_level


class LanguageOfCataloging:
    """Holds language of cataloging information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'languageOfCataloging')

        if self.value:
            top_level.text = self.value.strip()

        return top_level


class PhysicalDescription:
    """Holds physical description information"""

    def __init__(self):
        self.type = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'physicalDescription')

        if self.type:
            top_level.set('type', self.type.strip())

        return top_level


class TypeOfResource:
    """Holds type of resource information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'typeOfResource')
        top_level.text = self.value.strip()

        return top_level


class Form:
    """Holds form information"""

    def __init__(self):
        self.authority = ''
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'form')

        if self.authority:
            top_level.set('authority', self.authority.strip())

        top_level.text = self.value.strip()
        return top_level


class InternetMediaType:
    """Holds internet media type information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'internetMediaType')

        top_level.text = self.value.strip()
        return top_level


class DigitalOrigin:
    """Holds digital origin information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'digitalOrigin')

        top_level.text = self.value.strip()
        return top_level


class Extent:
    """Holds extent information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'extent')

        top_level.text = self.value.strip()
        return top_level


class Abstract:
    """Holds abstract information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'abstract')

        top_level.text = self.value.strip()

        return top_level


class Subject:
    """Holds subject information"""

    def __init__(self):
        self.type = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'subject')

        if self.type:
            top_level.set('type', self.type.strip())

        return top_level


class Topic:
    """Holds topic information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'topic')
        top_level.text = self.value.strip()
        return top_level


class Geographic:
    """Holds geographic information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'geographic')
        top_level.text = self.value.strip()
        return top_level


class Genre:
    """Holds genre information"""

    def __init__(self):
        self.authority = ''
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'genre')

        if self.authority:
            top_level.set('authority', self.authority.strip())

        top_level.text = self.value.strip()
        return top_level


class Note:
    """Holds note information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'note')

        top_level.text = self.value.strip()
        return top_level


class Role:
    """Holds role information"""

    def __init__(self):
        self.type = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'role')

        if self.type:
            top_level.set('type', self.type.strip())

        return top_level


class Language:
    """Holds language information"""

    def __init__(self):
        self.type = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'language')

        if self.type:
            top_level.set('type', self.type.strip())

        return top_level


class LanguageTerm:
    """Holds language term information"""

    def __init__(self):
        self.type = ''
        self.value = ''
        self.authority = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'languageTerm')

        if self.type:
            top_level.set('type', self.type.strip())

        if self.authority:
            top_level.set('authority', self.authority.strip())

        top_level.text = self.value.strip()
        return top_level


class RoleTerm:
    """Holds role term information"""

    def __init__(self):
        self.value = ''
        self.authority = ''
        self.type = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'roleTerm')

        if self.type:
            top_level.set('type', self.type.strip())

        if self.authority:
            top_level.set('authority', self.authority.strip())

        top_level.text = self.value.strip()
        return top_level


class Name:
    """Holds name information"""

    def __init__(self):
        self.type = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'name')

        if self.type:
            top_level.set('type', self.type.strip())

        return top_level


class NamePart:
    """Holds name part information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'namePart')

        top_level.text = self.value.strip()

        return top_level


class DateCreated:
    """Holds date created information"""

    def __init__(self):
        self.value = ''
        self.encoding = ''
        self.qualifier = ''
        self.keyDate = ''
        self.point = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'dateCreated')

        if self.encoding:
            top_level.set('encoding', self.encoding.strip())

        if self.qualifier:
            top_level.set('qualifier', self.qualifier.strip())

        if self.keyDate:
            top_level.set('keyDate', self.keyDate.strip())

        if self.point:
            top_level.set('point', self.point.strip())

        top_level.text = self.value.strip()

        return top_level


class DateIssued:
    """Holds date issued information"""

    def __init__(self):
        self.value = ''
        self.encoding = ''
        self.qualifier = ''
        self.keyDate = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'dateIssued')

        if self.encoding:
            top_level.set('encoding', self.encoding.strip())

        if self.qualifier:
            top_level.set('qualifier', self.qualifier.strip())

        if self.keyDate:
            top_level.set('keyDate', self.keyDate.strip())

        top_level.text = self.value.strip()

        return top_level


class OriginInfo:
    """Holds origin info information"""

    def __init__(self):
        self.value = ''

    @staticmethod
    def to_mods_element(parent_element):
        top_level = ET.SubElement(parent_element, 'originInfo')
        return top_level


class Place:
    """Holds place information"""

    def __init__(self):
        self.value = ''

    @staticmethod
    def to_mods_element(parent_element):
        top_level = ET.SubElement(parent_element, 'place')
        return top_level


class PlaceTerm:
    """Holds place term information"""

    def __init__(self):
        self.type = ''
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'placeTerm')

        if self.type:
            top_level.set('type', self.type.strip())

        top_level.text = self.value.strip()

        return top_level


class RelatedItem:
    """Holds Releated Item information"""

    def __init__(self):
        self.type = ''
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'relatedItem')
        if self.type:
            top_level.set('type', self.type.strip())

        return top_level


class TitleInfo:
    """Holds identifier information"""

    def __init__(self):
        self.value = ''

    @staticmethod
    def to_mods_element(parent_element):
        top_level = ET.SubElement(parent_element, 'titleInfo')
        return top_level


class Title:
    """Holds title information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'title')
        top_level.text = self.value.strip()
        return top_level


class Location:
    """Holds identifier information"""

    def __init__(self):
        self.value = ''

    @staticmethod
    def to_mods_element(parent_element):
        top_level = ET.SubElement(parent_element, 'location')
        return top_level


class PhysicalLocation:
    """Holds physical location information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'physicalLocation')
        top_level.text = self.value.strip()
        return top_level


class ShelfLocator:
    """Holds shelf locator information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'shelfLocator')
        top_level.text = self.value.strip()
        return top_level


class AccessCondition:
    """Holds access condition information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'accessCondition')
        top_level.text = self.value.strip()
        return top_level


class Identifier:
    """Holds identifier information"""

    def __init__(self):
        self.type = ''
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'identifier')
        if self.type:
            top_level.set('type', self.type.strip())

        top_level.text = self.value.strip()
        return top_level


#
# Build the xml file using the above classes
#
def build_xml(row):
    print('build xml')
    root = ET.Element('mods', {"xmlns:xlink": "http://www.w3.org/1999/xlink",
                               "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                               "xmlns": "http://www.loc.gov/mods/v3",
                               "version": "3.5",
                               "xsi:schemaLocation": "http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd"})

    location_element = None
    if row[0]:
        job_number = Identifier()
        job_number.type = 'job'
        job_number.value = row[0]
        job_number.to_mods_element(root)

    # physical location information
    if row[1]:
        location = Location()
        location_element = location.to_mods_element(root)

        physical_location = PhysicalLocation()
        physical_location.value = row[1]
        physical_location.to_mods_element(location_element)

    # shelf location information
    if row[2]:
        shelf_locator = ShelfLocator()
        shelf_locator.value = row[2]
        shelf_locator.to_mods_element(location_element)

    # title information
    if row[3]:
        title_info = TitleInfo()
        title_info_element = title_info.to_mods_element(root)

        title = Title()
        title.value = row[3]

        title.to_mods_element(title_info_element)

    # related item information
    if row[4]:
        related_item = RelatedItem()
        related_item.type = 'host'
        related_item_element = related_item.to_mods_element(root)

        title_info2 = TitleInfo()
        title_info_element2 = title_info2.to_mods_element(related_item_element)
        title2 = Title()
        title2.value = row[4]

        title2.to_mods_element(title_info_element2)

    # date created information
    if row[5]:
        origin_info_element = OriginInfo().to_mods_element(root)
        date_created = DateCreated()
        date_created.value = row[5]
        date_created.encoding = "w3cdtf"
        date_created.keyDate = "yes"
        date_created.to_mods_element(origin_info_element)

        # add date issued so it shows up in dublin core
        date_issued = DateIssued()
        date_issued.value = row[5]
        date_issued.encoding = "w3cdtf"
        date_issued.keyDate = "yes"
        date_issued.to_mods_element(origin_info_element)

    # date approximate
    if row[6]:
        date_approx_info_element = OriginInfo().to_mods_element(root)
        date_approximate = DateCreated()
        date_approximate.value = row[6]
        date_approximate.encoding = "w3cdtf"
        date_approximate.qualifier = "approximate"
        date_approximate.to_mods_element(date_approx_info_element)

    # date inferred
    if row[7]:
        date_inferred_info_element = OriginInfo().to_mods_element(root)
        date_inferred = DateCreated()
        date_inferred.value = row[7]
        date_inferred.encoding = "w3cdtf"
        date_inferred.qualifier = "inferred"
        date_inferred.to_mods_element(date_inferred_info_element)

    # date questionable
    if row[8]:
        date_questionable_info_element = OriginInfo().to_mods_element(root)
        date_questionable = DateCreated()
        date_questionable.value = row[8]
        date_questionable.encoding = "w3cdtf"
        date_questionable.qualifier = "questionable"

        date_questionable.to_mods_element(date_questionable_info_element)

    # begin date
    if row[9]:
        begin_date_info_element = OriginInfo().to_mods_element(root)
        date_begin = DateCreated()
        date_begin.value = row[9]
        date_begin.encoding = "marc"
        date_begin.point = "start"

        date_begin.to_mods_element(begin_date_info_element)

    # end date
    if row[10]:
        end_date_info_element = OriginInfo().to_mods_element(root)
        end_begin = DateCreated()
        end_begin.value = row[10]
        end_begin.encoding = "marc"
        end_begin.point = "end"

        end_begin.to_mods_element(end_date_info_element)

    # personal name element (Letter creator)
    if row[11]:
        name = Name()
        name.type = "personal"

        name1_element = name.to_mods_element(root)
        name_part = NamePart()
        name_part.value = row[11]

        name_part.to_mods_element(name1_element)
        role_element = Role().to_mods_element(name1_element)

        # role of the person
        if row[12]:
            role_term = RoleTerm()
            role_term.authority = "marcrelator"
            role_term.type = "text"
            role_term.value = row[12]
            role_term.to_mods_element(role_element)

    # abstract information
    if row[13]:
        abstract = Abstract()
        abstract.value = row[13]
        abstract.to_mods_element(root)

    # geo location information
    if row[14]:
        geo_location_element = OriginInfo().to_mods_element(root)
        place_element = Place().to_mods_element(geo_location_element)
        place_term = PlaceTerm()
        place_term.type = "text"
        place_term.value = row[14]
        place_term.to_mods_element(place_element)

    # language information
    if row[15]:
        language_element = Language().to_mods_element(root)
        language_term = LanguageTerm()
        language_term.type = "text"
        language_term.value = row[15]
        language_term.to_mods_element(language_element)

    # related name (Letter recipient)
    if row[16]:
        related_name = Name().to_mods_element(root)
        related_name_part = NamePart()
        related_name_part.value = row[16]

        related_name_part.to_mods_element(related_name)
        role_element2 = Role().to_mods_element(related_name)

        if row[17]:
            role_term2 = RoleTerm()
            role_term2.authority = "marcrelator"
            role_term2.type = "text"
            role_term2.value = row[17]
            role_term2.to_mods_element(role_element2)

    # genre information
    if row[18]:
        genre = Genre()
        genre.authority = "gmgpc"
        genre.value = row[18]
        genre.to_mods_element(root)

    # subject - topic information
    if row[19]:
        topic_subject_element = Subject().to_mods_element(root)
        topic = Topic()
        topic.value = row[19]
        topic.to_mods_element(topic_subject_element)

    # subject - name information
    if row[20]:
        topic_subject_root_element = Subject().to_mods_element(root)
        name_subject = Name()
        name_subject.type = "personal"
        name_subject_element = name_subject.to_mods_element(topic_subject_root_element)
        name_subject_part = NamePart()
        name_subject_part.value = row[20]
        name_subject_part.to_mods_element(name_subject_element)

    # subject - corporation name information
    if row[21]:
        corp_subject_root_element = Subject().to_mods_element(root)
        corp_subject = Name()
        corp_subject.type = "corporate"
        corp_subject_element = corp_subject.to_mods_element(corp_subject_root_element)
        corp_subject_part = NamePart()
        corp_subject_part.value = row[21]
        corp_subject_part.to_mods_element(corp_subject_element)

    # subject geographic information
    if row[22]:
        geo_subject_root_element = Subject().to_mods_element(root)
        geo = Geographic()
        geo.value = row[22]
        geo.to_mods_element(geo_subject_root_element)

    # physical description/form
    if row[23] or row[24] or row[25]:
        physical_description_element = PhysicalDescription().to_mods_element(root)

        if row[23]:
            form = Form()
            form.authority = "marcform"
            form.value = row[23]
            form.to_mods_element(physical_description_element)

        # media type e.g. image/tiff
        if row[24]:
            internet_media_type = InternetMediaType()
            internet_media_type.value = row[24]
            internet_media_type.to_mods_element(physical_description_element)

        if row[25]:

            page_str = " pages"

            if int(row[25]) <= 1:
                page_str = " page"

            # extent
            extent = Extent()
            extent.value = row[25] + page_str
            extent.to_mods_element(physical_description_element)

    # note
    if row[28]:
        note = Note()
        note.value = row[28]
        note.to_mods_element(root)

    # type of resource
    if row[29]:
        type_of_resource = TypeOfResource()
        type_of_resource.value = row[29]
        type_of_resource.to_mods_element(root)

    # source and language of cataloging
    if row[30] or row[31]:
        record_info_element = RecordInfo().to_mods_element(root)
        # source information
        if row[30]:
            record_source = RecordContentSource()
            record_source.value = row[30]
            record_source.to_mods_element(record_info_element)
        if row[31]:
            lang_of_cat_element = LanguageOfCataloging().to_mods_element(record_info_element)
            record_language = LanguageTerm()
            record_language.value = row[31]
            record_language.type = "code"
            record_language.authority = "iso639-2b"
            record_language.to_mods_element(lang_of_cat_element)

    # rights access
    if row[32]:
        access_condition = AccessCondition()
        access_condition.value = row[32]
        access_condition.to_mods_element(root)

    # ET.dump(root)
    return root


#
#  Create an xml with the data from the xml file
#
def create_xml_file(row, file_name):
    print("XML file name will be = " + file_name)
    root_node = build_xml(row)
    tree = ET.ElementTree(root_node)

    if file_name:
        tree.write(file_name)


#
# Creates a folder for every page based on the file name - this is a
# requirement of islandora
#
def create_page_structure(pages, base_dir, base_filename, book_dir):
    # default format - no leading zeros
    page_format = "{0:01d}"

    if 9 < pages < 99:
        # one leading zero
        page_format = "{0:02d}"
    elif 99 < pages < 999:
        # two leading zeros
        page_format = "{0:03d}"
    elif 999 < pages < 9999:
        # three leading zeros
        page_format = "{0:04d}"

    for page in range(1, pages):
        page_name = page_format.format(page)
        filename = base_filename + "_" + str(page) + ".tif"
        source_file = os.path.join(base_dir, filename)
        if not os.path.isfile(source_file):
            print("Could not find file " + source_file)
            sys.exit()
        else:
            page_dir = os.path.join(book_dir, "page-" + page_name)
            dest_file = os.path.join(page_dir, "OBJ.tif")
            print("source  = " + source_file + " dest = " + dest_file)
            print("creating directory " + page_dir)
            os.mkdir(page_dir)
            shutil.copy(source_file, dest_file)


#
#  Create the file structure for a book in islandora
#
def create_file_structure(a_counter, row, base_dir, output_dir):
    # base file name
    base_filename = row[27]
    # off by one so increase so it works correctly
    pages = int(row[25]) + 1
    print("filename = " + base_filename)
    assert isinstance(output_dir, object)
    book_dir = os.path.join(output_dir, str(a_counter))
    print("creating directory " + book_dir)
    os.mkdir(book_dir)
    my_xml_file = os.path.join(book_dir, "MODS" + ".xml")
    create_xml_file(row, a_counter, my_xml_file)
    create_page_structure(pages, base_dir, base_filename, book_dir)


# 
#  Use this to print out the fields of a csv file and allows programmer
#  to see the output
#
def print_csv_info(a_file):
    with open(a_file, 'r') as csvfile:
        file_reader = csv.reader(csvfile)
        my_counter = 1
        for row in file_reader:
            print("************* " + str(my_counter) + " *********************")
            my_counter += 1
            for x in range(0, 33):
                print("row " + str(x) + " = " + row[x])
            print("*************  DONE - " + str(my_counter) + " *********************")
            print("")


# ########################################
# Main Program
# ########################################

# get the csv file input
csv_file = input("Please enter csv file name: ")
if not os.path.isfile(csv_file):
    print("Could not find file " + csv_file)
    sys.exit()
else:
    print("found file ")

test = input("Test csv file (yes) to test: ")
if test.lower() == "yes":
    print("testing csv file")
    print_csv_info(csv_file)

    test_xml = input("Test xml output (yes) to test: ")
    if test_xml.lower() == "yes":
        output_directory = input("Please enter xml output directory: ")
        if not os.path.isdir(output_directory):
            print("Directory " + output_directory + " does not exist or is not a directory")
            sys.exit()
        else:
            print("Directory found " + output_directory)
            # open the csv and start iterating through the rows
            with open(csv_file, 'r') as the_csv_file:
                fileReader = csv.reader(the_csv_file)
                counter = 1
                for a_row in fileReader:
                    if a_row[25]:
                        num_pages = int(a_row[25])
                        if num_pages > 0:
                            print("processing " + str(num_pages) + " pages")
                            xml_file = os.path.join(output_directory, "MODS_" + str(counter) + ".xml")
                            create_xml_file(a_row, counter, xml_file)
                    else:
                        print("Skipping row " + str(counter) + " pages found were " + a_row[25])
                    counter += 1

else:
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

    # open the csv and start iterating through the rows
    with open(csv_file, 'r') as the_csv_file:
        fileReader = csv.reader(the_csv_file)
        counter = 1
        for a_row in fileReader:
            if a_row[25]:
                num_pages = int(a_row[25])
                if num_pages > 0:
                    print("processing " + str(num_pages) + " pages")
                    create_file_structure(counter, a_row, base_directory, output_directory)

            else:
                print("Skipping row " + str(counter) + " pages found were " + a_row[25])
            counter += 1
