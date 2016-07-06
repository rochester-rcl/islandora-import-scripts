#!/usr/bin/python

import xml.etree.ElementTree as ET
import mods
import csv


# ##########################################
# Build the xml file using the MODS classes
# ##########################################
def build_xml(row, current):
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

    # physical location information
    if row[1]:
        location = mods.Location()
        location_element = location.to_mods_element(root)

        physical_location = mods.PhysicalLocation()
        physical_location.value = row[1]
        physical_location.to_mods_element(location_element)

    # shelf location information
    if row[2]:
        shelf_locator = mods.ShelfLocator()
        shelf_locator.value = row[2]
        shelf_locator.to_mods_element(location_element)

    # title information
    if row[3]:
        title_info = mods.TitleInfo()
        title_info_element = title_info.to_mods_element(root)

        title = mods.Title()
        title.value = row[3]

        title.to_mods_element(title_info_element)

    # related item information
    if row[4]:
        related_item = mods.RelatedItem()
        related_item.type = 'host'
        related_item_element = related_item.to_mods_element(root)

        title_info2 = mods.TitleInfo()
        title_info_element2 = title_info2.to_mods_element(related_item_element)
        title2 = mods.Title()
        title2.value = row[4]

        title2.to_mods_element(title_info_element2)

    if row[5] or row[6] or row[7] or row[8] or row[9] or row[10]:
        origin_info_element = mods.OriginInfo().to_mods_element(root)

        # date created information
        if row[5]:
            date_created = mods.DateCreated()
            date_created.value = row[5]
            date_created.encoding = "w3cdtf"
            date_created.keyDate = "yes"
            date_created.to_mods_element(origin_info_element)

            # add date issued so it shows up in dublin core
            date_issued = mods.DateIssued()
            date_issued.value = row[5]
            date_issued.encoding = "w3cdtf"
            date_issued.keyDate = "yes"
            date_issued.to_mods_element(origin_info_element)

        # date approximate
        if row[6]:
            date_approximate = mods.DateCreated()
            date_approximate.value = row[6]
            date_approximate.encoding = "w3cdtf"
            date_approximate.qualifier = "approximate"
            date_approximate.to_mods_element(origin_info_element)

        # date inferred
        if row[7]:
            date_inferred = mods.DateCreated()
            date_inferred.value = row[7]
            date_inferred.encoding = "w3cdtf"
            date_inferred.qualifier = "inferred"
            date_inferred.to_mods_element(origin_info_element)

        # date questionable
        if row[8]:
            date_questionable = mods.DateCreated()
            date_questionable.value = row[8]
            date_questionable.encoding = "w3cdtf"
            date_questionable.qualifier = "questionable"
            date_questionable.to_mods_element(origin_info_element)

        # begin date
        if row[9]:
            date_begin = mods.DateCreated()
            date_begin.value = row[9]
            date_begin.encoding = "marc"
            date_begin.point = "start"
            date_begin.to_mods_element(origin_info_element)

        # end date
        if row[10]:
            end_begin = mods.DateCreated()
            end_begin.value = row[10]
            end_begin.encoding = "marc"
            end_begin.point = "end"
            end_begin.to_mods_element(origin_info_element)

    # geo location information
    if row[16]:
        place_element = mods.Place().to_mods_element(origin_info_element)
        place_term = mods.PlaceTerm()
        place_term.type = "text"
        place_term.value = row[16]
        place_term.to_mods_element(place_element)

    if row[38]:
        publisher = mods.Publisher()
        publisher.value = row[38]
        publisher.to_mods_element(origin_info_element)

    # personal name element (Letter creator)
    if row[11]:
        name = mods.Name()

        name.type = "personal"

        # name type (personal/corporate)
        if row[12]:
            name.type = row[12]

        name1_element = name.to_mods_element(root)
        name_part = mods.NamePart()
        name_part.value = row[11]

        name_part.to_mods_element(name1_element)
        role_element = mods.Role().to_mods_element(name1_element)

        # role of the person
        if row[13]:
            role_term = mods.RoleTerm()
            role_term.authority = "marcrelator"
            role_term.type = "text"
            role_term.value = row[13]
            role_term.to_mods_element(role_element)

    # abstract information
    if row[15]:
        abstract = mods.Abstract()
        abstract.value = row[15]
        abstract.to_mods_element(root)

    # language information
    if row[17]:
        language_element = mods.Language().to_mods_element(root)
        language_term = mods.LanguageTerm()
        language_term.type = "text"
        language_term.value = row[17]
        language_term.to_mods_element(language_element)

    # related name (Letter recipient)
    if row[18]:
        related_name = mods.Name()
        related_name.type = 'personal'

        if row[19]:
            related_name.type = row[19]

        related_name_element = related_name.to_mods_element(root)
        related_name_part = mods.NamePart()
        related_name_part.value = row[18]

        related_name_part.to_mods_element(related_name_element)
        role_element2 = mods.Role().to_mods_element(related_name_element)

        if row[20]:
            role_term2 = mods.RoleTerm()
            role_term2.authority = "marcrelator"
            role_term2.type = "text"
            role_term2.value = row[20]
            role_term2.to_mods_element(role_element2)

    # genre information
    if row[22]:
        genre = mods.Genre()
        genre.authority = "gmgpc"
        genre.value = row[22]
        genre.to_mods_element(root)

    # subject - topic information
    if row[23]:
        topic_subject_element = mods.Subject().to_mods_element(root)
        topic = mods.Topic()
        topic.value = row[23]
        topic.to_mods_element(topic_subject_element)

    # subject - name information
    if row[24]:
        name_subject_root_element = mods.Subject().to_mods_element(root)
        name_subject = mods.Name()
        name_subject.type = "personal"
        name_subject_element = name_subject.to_mods_element(name_subject_root_element)
        name_subject_part = mods.NamePart()
        name_subject_part.value = row[24]
        name_subject_part.to_mods_element(name_subject_element)

    # subject - corporation name information
    if row[25]:
        corp_subject_root_element = mods.Subject().to_mods_element(root)
        corp_subject = mods.Name()
        corp_subject.type = "corporate"
        corp_subject_element = corp_subject.to_mods_element(corp_subject_root_element)
        corp_subject_part = mods.NamePart()
        corp_subject_part.value = row[25]
        corp_subject_part.to_mods_element(corp_subject_element)

    # subject geographic information
    if row[26]:
        geo_subject_root_element = mods.Subject().to_mods_element(root)
        geo = mods.Geographic()
        geo.value = row[26]
        geo.to_mods_element(geo_subject_root_element)

    # physical description/form
    if row[27] or row[28] or row[29]:
        physical_description_element = mods.PhysicalDescription().to_mods_element(root)

        if row[27]:
            form = mods.Form()
            form.authority = "marcform"
            form.value = row[27]
            form.to_mods_element(physical_description_element)

        # media type e.g. image/tiff
        if row[28]:
            internet_media_type = mods.InternetMediaType()
            internet_media_type.value = row[28]
            internet_media_type.to_mods_element(physical_description_element)

        if row[29]:
            # extent
            extent = mods.Extent()
            extent.value = row[29] + " pages"
            extent.to_mods_element(physical_description_element)

    # note
    if row[33]:
        note = mods.Note()
        note.value = row[33]
        note.to_mods_element(root)

    # type of resource
    if row[34]:
        type_of_resource = mods.TypeOfResource()
        type_of_resource.value = row[34]
        type_of_resource.to_mods_element(root)

    # source and language of cataloging
    if row[35] or row[36]:
        record_info_element = mods.RecordInfo().to_mods_element(root)
        # source information
        if row[35]:
            record_source = mods.RecordContentSource()
            record_source.value = row[35]
            record_source.to_mods_element(record_info_element)
        if row[36]:
            lang_of_cat_element = mods.LanguageOfCataloging().to_mods_element(record_info_element)
            record_language = mods.LanguageTerm()
            record_language.value = row[36]
            record_language.type = "code"
            record_language.authority = "iso639-2b"
            record_language.to_mods_element(lang_of_cat_element)

    # rights access
    if row[37]:
        access_condition = mods.AccessCondition()
        access_condition.value = row[37]
        access_condition.to_mods_element(root)

    # ET.dump(root)
    return root


# ##################################################
#  Create an xml with the data from the xml file
# ##################################################
def create_xml_file(row, file_name, page_number = None):
    print("XML file name will be = " + file_name)
    root_node = build_xml(row)
    tree = ET.ElementTree(root_node)

    if file_name:
        tree.write(file_name)


#
#  Use this to print out the fields of a csv file and allows programmer
#  to see the output
#
def print_csv_info(a_file):
    with open(a_file, 'r') as csv_file:
        file_reader = csv.reader(csv_file)
        counter = 1
        for row in file_reader:
            print("************* " + str(counter) + " *********************")
            counter += 1
            for x in range(0, 39):
                print("row " + str(x) + " = " + row[x])
            print("*************  DONE - " + str(counter) + " *********************")
            print("")
