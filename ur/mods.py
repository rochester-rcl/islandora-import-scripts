#!/usr/bin/python

import xml.etree.ElementTree as ET


# #########################################################
# Represents all the MODS metadata classes for import 
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


class Publisher:
    """Holds publisher information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'publisher')

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
        self.type = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'note')
        if self.type:
            top_level.set('type', self.type.strip())

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

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'originInfo')
        return top_level


class Place:
    """Holds place information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
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
        self.display_label = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'relatedItem')
        if self.type:
            top_level.set('type', self.type.strip())
        if self.display_label:
            top_level.set('displayLabel', self.display_label.strip())

        return top_level


class TitleInfo:
    """Holds identifier information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
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

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'location')
        return top_level


class PhysicalLocation:
    """Holds physical location information"""

    def __init__(self):
        self.value = ''
        self.type = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'physicalLocation')
        if self.type:
            top_level.set('type', self.type.strip())
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


class HoldingSimple:
    """Holdings information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'holdingSimple')
        top_level.text = self.value.strip()
        return top_level


class CopyInformation:
    """Holdings information"""

    def __init__(self):
        self.value = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'copyInformation')
        top_level.text = self.value.strip()
        return top_level


class EnumerationAndChronology:

    def __init__(self):
        self.value = ''
        self.unit_type = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'enumerationAndChronology')
        top_level.text = self.value.strip()

        if self.unit_type:
            top_level.set('qualifier', str(self.unit_type).strip())

        return top_level


class AccessCondition:
    """Holds access condition information"""

    def __init__(self):
        self.value = ''
        self.type = ''
        self.display_label = ''
        self.xlink = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'accessCondition')

        if self.type:
            top_level.set('type', self.type.strip())

        if self.display_label:
            top_level.set('displayLabel', self.display_label)

        if self.xlink:
            top_level.set('xlink:href', self.xlink)

        top_level.text = self.value.strip()
        return top_level


class Identifier:
    """Holds identifier information"""

    def __init__(self):
        self.type = ''
        self.value = ''
        self.display_label = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'identifier')
        if self.type:
            top_level.set('type', self.type.strip())

        if self.display_label:
            top_level.set('displayLabel', self.display_label)

        top_level.text = self.value.strip()
        return top_level


class Url:
    """Holds url information"""

    def __init__(self):
        self.value = ''
        self.display_label = ''

    def to_mods_element(self, parent_element):
        top_level = ET.SubElement(parent_element, 'url')

        if self.display_label:
            top_level.set('displayLabel', self.display_label)

        top_level.text = self.value.strip()
        return top_level
