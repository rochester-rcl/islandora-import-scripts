#!/usr/bin/python

import mods
import csv
import xml.etree.ElementTree as ET


# ##########################################
# Build the xml file using the MODS classes
# ##########################################
def build_xml(row, current_page = None):
    print('build xml')
    root = ET.Element('mods', {"xmlns:xlink": "http://www.w3.org/1999/xlink",
                               "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                               "xmlns": "http://www.loc.gov/mods/v3",
                               "version": "3.5",
                               "xsi:schemaLocation": "http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd"})

    if row[0]:
        job_number = mods.Identifier()
        job_number.type = 'job'
        job_number.value = row[0]
        job_number.to_mods_element(root)

    # location information
    if row[1] or row[2] or row[3]:
        # create location element
        location = mods.Location()
        location_element = location.to_mods_element(root)

        # physical location
        if row[1]:
            physical_location = mods.PhysicalLocation()
            physical_location.value = row[1]
            physical_location.to_mods_element(location_element)

        # holdings information
        if row[2] or row[3]:
            holding_simple = mods.HoldingSimple()
            copy_information = mods.CopyInformation()
            holding_simple_element = holding_simple.to_mods_element(location_element)
            copy_information_element = copy_information.to_mods_element(holding_simple_element)

            # call number
            if row[2]:
                shelf_locator = mods.ShelfLocator()
                shelf_locator.value = row[2]
                shelf_locator.to_mods_element(copy_information_element)

            # box.folder number
            if row[3]:
                enumeration_and_chronology = mods.EnumerationAndChronology()
                enumeration_and_chronology.unit_type = 1
                enumeration_and_chronology.value = row[3]
                enumeration_and_chronology.to_mods_element(copy_information_element)

    # folder title
    if row[4]:
        related_item = mods.RelatedItem()
        related_item.display_label = 'Folder'
        related_item_element = related_item.to_mods_element(root)

        folder_title_info = mods.TitleInfo()
        folder_title_info_element = folder_title_info.to_mods_element(related_item_element)
        folder_title = mods.Title()
        folder_title.value = row[4]

        folder_title.to_mods_element(folder_title_info_element)

    # object title information
    if row[5]:
        title_info = mods.TitleInfo()
        title_info_element = title_info.to_mods_element(root)

        title = mods.Title()

        if current_page:
            title.value = 'p.' + str(current_page) + ' ' + row[5]
        else:
            title.value = row[5]

        title.to_mods_element(title_info_element)

    # collection title
    if row[6]:
        host_item = mods.RelatedItem()
        host_item.type = 'host'
        host_item.display_label = 'Collection'
        host_item_element = host_item.to_mods_element(root)

        collection_title_info = mods.TitleInfo()
        collection_title_info_element = collection_title_info.to_mods_element(host_item_element)
        collection_title = mods.Title()
        collection_title.value = row[6]

        collection_title.to_mods_element(collection_title_info_element)

    # series title
    if row[7]:
        series_host_item = mods.RelatedItem()
        series_host_item.type = 'series'
        series_host_item_element = series_host_item.to_mods_element(root)

        series_title_info = mods.TitleInfo()
        series_title_info_element = series_title_info.to_mods_element(series_host_item_element)
        series_title = mods.Title()
        series_title.value = row[7]

        series_title.to_mods_element(series_title_info_element)

    # origin information
    if row[8] or row[10] or row[19] or row[20]:
        origin_info_element = mods.OriginInfo().to_mods_element(root)

        if row[8]:

            # first date
            date_created1 = mods.DateCreated()
            date_created1.value = row[8]
            date_created1.encoding = "w3cdtf"
            date_created1.keyDate = "yes"

            # add date issued so it shows up in dublin core
            date_issued1 = mods.DateIssued()
            date_issued1.value = row[8]
            date_issued1.encoding = "w3cdtf"
            date_issued1.keyDate = "yes"

            # add qualifier if it exists
            if row[9]:
                date_created1.qualifier = row[9]
                date_issued1.qualifier = row[9]

            date_created1.to_mods_element(origin_info_element)
            date_issued1.to_mods_element(origin_info_element)

        # second date
        if row[10]:
            # second date
            date_created2 = mods.DateCreated()
            date_created2.value = row[10]
            date_created2.encoding = "w3cdtf"
            date_created2.keyDate = "yes"

            # add date issued so it shows up in dublin core
            date_issued2 = mods.DateIssued()
            date_issued2.value = row[10]
            date_issued2.encoding = "w3cdtf"
            date_issued2.keyDate = "yes"

            # add qualifier if it exists
            if row[11]:
                date_created2.qualifier = row[11]
                date_issued2.qualifier = row[11]

            date_created2.to_mods_element(origin_info_element)
            date_issued2.to_mods_element(origin_info_element)

        # publisher information
        if row[19]:
            publisher = mods.Publisher()
            publisher.value = row[19]
            publisher.to_mods_element(origin_info_element)

        # geo location information
        if row[20]:
            place_element = mods.Place().to_mods_element(origin_info_element)
            place_term = mods.PlaceTerm()
            place_term.type = "text"
            place_term.value = row[20]
            place_term.to_mods_element(place_element)

    # author name information
    if row[12]:
        name = mods.Name()

        # default name type
        name.type = "personal"

        # name type (personal/corporate)
        if row[13]:
            name.type = row[13]

        name1_element = name.to_mods_element(root)
        name_part = mods.NamePart()
        name_part.value = row[12]

        name_part.to_mods_element(name1_element)
        role_element = mods.Role().to_mods_element(name1_element)

        # role of the person
        if row[14]:
            role_term = mods.RoleTerm()
            role_term.authority = "marcrelator"
            role_term.type = "text"
            role_term.value = row[14]
            role_term.to_mods_element(role_element)

    # related name (Letter recipient)
    if row[15]:
        related_name = mods.Name()
        related_name.type = 'personal'

        if row[16]:
            related_name.type = row[16]

        related_name_element = related_name.to_mods_element(root)
        related_name_part = mods.NamePart()
        related_name_part.value = row[15]

        related_name_part.to_mods_element(related_name_element)
        role_element2 = mods.Role().to_mods_element(related_name_element)

        if row[17]:
            role_term2 = mods.RoleTerm()
            role_term2.authority = "marcrelator"
            role_term2.type = "text"
            role_term2.value = row[17]
            role_term2.to_mods_element(role_element2)

    # abstract information
    if row[18]:
            abstract = mods.Abstract()
            abstract.value = row[18]
            abstract.to_mods_element(root)

    # language information
    if row[21]:
        language_element = mods.Language().to_mods_element(root)
        language_term = mods.LanguageTerm()
        language_term.type = "text"
        language_term.value = row[21]
        language_term.to_mods_element(language_element)

    # genre information
    if row[22]:
        genre = mods.Genre()
        genre.authority = "gmgpc"
        genre.value = row[22]
        genre.to_mods_element(root)

    # subject - name information
    if row[23]:
        subject_root_element = mods.Subject().to_mods_element(root)
        if row[24]:
            subject_type = row[24]

            if subject_type == "personal name" or subject_type == "corporate name" or subject_type == "family name":
                name_subject = mods.Name()
                if subject_type == "personal name":
                    name_subject.type = "personal"
                elif subject_type == "corporate name":
                    name_subject.type = "corporate"
                elif subject_type == "family name":
                    name_subject.type = "family"
                name_subject_element = name_subject.to_mods_element(subject_root_element)
                name_subject_part = mods.NamePart()
                name_subject_part.value = row[23]
                name_subject_part.to_mods_element(name_subject_element)
            elif subject_type == "topic":
                topic = mods.Topic()
                topic.value = row[23]
                topic.to_mods_element(subject_root_element)
            elif subject_type == "geographic":
                geo = mods.Geographic()
                geo.value = row[23]
                geo.to_mods_element(subject_root_element)

    # subject - name information
    if row[25]:
        subject_root_element = mods.Subject().to_mods_element(root)
        if row[26]:
            subject_type = row[26]

            if subject_type == "personal name" or subject_type == "corporate name" or subject_type == "family name":
                name_subject = mods.Name()
                if subject_type == "personal name":
                    name_subject.type = "personal"
                elif subject_type == "corporate name":
                    name_subject.type = "corporate"
                elif subject_type == "family name":
                    name_subject.type = "family"
                name_subject_element = name_subject.to_mods_element(subject_root_element)
                name_subject_part = mods.NamePart()
                name_subject_part.value = row[25]
                name_subject_part.to_mods_element(name_subject_element)
            elif subject_type == "topic":
                topic = mods.Topic()
                topic.value = row[25]
                topic.to_mods_element(subject_root_element)
            elif subject_type == "geographic":
                geo = mods.Geographic()
                geo.value = row[25]
                geo.to_mods_element(subject_root_element)

    # note
    if row[27]:
        note = mods.Note()
        note.value = row[27]
        note.to_mods_element(root)

    # physical description/form
    if row[28] or row[29] or row[31]:
        physical_description_element = mods.PhysicalDescription().to_mods_element(root)

        if row[28]:
            form = mods.Form()
            form.authority = "marcform"
            form.value = row[28]
            form.to_mods_element(physical_description_element)

        # media type e.g. image/tiff
        if row[29]:
            internet_media_type = mods.InternetMediaType()
            internet_media_type.value = row[29]
            internet_media_type.to_mods_element(physical_description_element)

        # if it's a current page use that otherwise use book mods
        if current_page:
            extent = mods.Extent()
            extent.value = "p. " + str(current_page)
            extent.to_mods_element(physical_description_element)

        elif row[31]:
            # extent
            extent = mods.Extent()
            extent.value = str(row[31]) + " pages"
            extent.to_mods_element(physical_description_element)

        if row[32]:
            # number of files
            physical_note = mods.Note()
            physical_note.type = "number of files"
            physical_note.value = str(row[32])
            physical_note.to_mods_element(physical_description_element)

    # type of resource
    if row[30]:
        type_of_resource = mods.TypeOfResource()
        type_of_resource.value = row[30]
        type_of_resource.to_mods_element(root)

    # source and language of cataloging
    if row[34] or row[35]:
        record_info_element = mods.RecordInfo().to_mods_element(root)
        # source information
        if row[34]:
            record_source = mods.RecordContentSource()
            record_source.value = row[34]
            record_source.to_mods_element(record_info_element)
        if row[35]:
            lang_of_cat_element = mods.LanguageOfCataloging().to_mods_element(record_info_element)
            record_language = mods.LanguageTerm()
            record_language.value = row[35]
            record_language.type = "code"
            record_language.authority = "iso639-2b"
            record_language.to_mods_element(lang_of_cat_element)

    # rights access
    if row[36]:
        access_condition = mods.AccessCondition()
        access_condition.value = row[36]
        access_condition.to_mods_element(root)

    return root


# ##################################################
#  Create an xml with the data from the xml file
# ##################################################
def create_xml_file(row, file_name, current_page = None):

    print("XML file name will be = " + file_name)
    root_node = build_xml(row, current_page)
    tree = ET.ElementTree(root_node)

    if file_name:
        tree.write(file_name)


#
#  Use this to print out the fields of a csv file and allows programmer
#  to see the output
#
def print_csv_info(a_file, num_rows):
    with open(a_file, 'r') as csv_file:
        file_reader = csv.reader(csv_file)
        counter = 1
        for row in file_reader:
            print("************* " + str(counter) + " *********************")
            counter += 1
            for x in range(0, num_rows):
                print("row " + str(x) + " = " + row[x])
            print("*************  DONE - " + str(counter) + " *********************")
            print("")
