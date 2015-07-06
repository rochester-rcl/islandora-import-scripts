#!/usr/bin/python

import xml.etree.ElementTree as ET
from xml.dom.minidom import Node 

# #########################################################
# Represents all the MODS metadata classes for import 
# #########################################################
class RecordInfo:
	"""Holds record info information"""
	def __init__(self):
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'recordInfo')
		
		if(self.value):
			topLevel.text = self.value.strip()


		return topLevel

class RecordContentSource:
	"""Holds content source information"""
	def __init__(self):
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'recordContentSource')
		
		if(self.value):
			topLevel.text = self.value.strip()


		return topLevel

class LanguageOfCataloging:
	"""Holds language of cataloging information"""
	def __init__(self):
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'languageOfCataloging')
		
		if(self.value):
			topLevel.text = self.value.strip()


		return topLevel



class PhysicalDescription:
	"""Holds physical description information"""
	def __init__(self):
		self.type = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'physicalDescription')
		
		if(self.type):
			topLevel.set('type', self.type.strip())

		return topLevel

class TypeOfResource:
	"""Holds type of resource information"""
	def __init__(self):
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'typeOfResource')
		topLevel.text = self.value.strip()

		return topLevel

class Form:
	"""Holds form information"""
	def __init__(self):
		self.authority = ''
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'form')
		
		if(self.authority):
			topLevel.set('authority', self.authority.strip())

		topLevel.text = self.value.strip()
		return topLevel

class InternetMediaType:
	"""Holds internet media type information"""
	def __init__(self):
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'internetMediaType')
		
		topLevel.text = self.value.strip()
		return topLevel

class DigitalOrigin:
	"""Holds digital origin information"""
	def __init__(self):
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'digitalOrigin')
		
		topLevel.text = self.value.strip()
		return topLevel


class Extent:
	"""Holds extent information"""
	def __init__(self):
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'extent')
		
		topLevel.text = self.value.strip()
		return topLevel

class Abstract:
	"""Holds abstract information"""
	def __init__(self):
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'abstract')
		
		topLevel.text = self.value.strip()

		return topLevel

class Publisher:
	"""Holds publisher information"""
	def __init__(self):
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'publisher')
		
		topLevel.text = self.value.strip()

		return topLevel


class Subject:
	"""Holds subject information"""
	def __init__(self):
		self.type = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'subject')
		
		if(self.type):
			topLevel.set('type', self.type.strip())

		return topLevel

class Topic:
	"""Holds topic information"""
	def __init__(self):
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'topic')
		topLevel.text = self.value.strip()
		return topLevel

class Geographic:
	"""Holds geographic information"""
	def __init__(self):
		self.value = ''	

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'geographic')
		topLevel.text = self.value.strip()
		return topLevel

class Genre:
	"""Holds genre information"""
	def __init__(self):
		self.authority = ''
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'genre')
		
		if(self.authority):
			topLevel.set('authority', self.authority.strip())

		topLevel.text = self.value.strip()
		return topLevel

class Note:
	"""Holds note information"""
	def __init__(self):
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'note')
		
		topLevel.text = self.value.strip()
		return topLevel


class Role:
	"""Holds role information"""
	def __init__(self):
		self.type = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'role')
		
		if(self.type):
			topLevel.set('type', self.type.strip())

		return topLevel

class Language:
	"""Holds language information"""
	def __init__(self):
		self.type = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'language')
		
		if(self.type):
			topLevel.set('type', self.type.strip())

		return topLevel

class LanguageTerm:
	"""Holds language term information"""
	def __init__(self):
		self.type = ''
		self.value = ''
		self.authority = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'languageTerm')
		
		if(self.type):
			topLevel.set('type', self.type.strip())

		if(self.authority):
			topLevel.set('authority', self.authority.strip())

		topLevel.text = self.value.strip()
		return topLevel



class RoleTerm:
	"""Holds role term information"""
	def __init__(self):
		self.value = ''
		self.authority = ''
		self.type = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'roleTerm')
		
		if(self.type):
			topLevel.set('type', self.type.strip())

		if(self.authority):
			topLevel.set('authority', self.authority.strip())

		topLevel.text = self.value.strip()
		return topLevel



class Name:
	"""Holds name information"""
	def __init__(self):
		self.type = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'name')
		
		if(self.type):
			topLevel.set('type', self.type.strip())

		return topLevel

class NamePart:
	"""Holds name part information"""
	def __init__(self):
		self.value = ''
		

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'namePart')
		
		topLevel.text = self.value.strip()

		return topLevel



class DateCreated:
	"""Holds date created information"""
	def __init__(self):
		self.value = ''
		self.encoding = ''
		self.qualifier = ''
		self.keyDate = ''
		self.point = ''	

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'dateCreated')
		
		if(self.encoding):
			topLevel.set('encoding', self.encoding.strip())

		if(self.qualifier):
			topLevel.set('qualifier', self.qualifier.strip())	

		if(self.keyDate):
			topLevel.set('keyDate', self.keyDate.strip())

		if(self.point):
			topLevel.set('point', self.point.strip())

		topLevel.text = self.value.strip()

		return topLevel

class DateIssued:
	"""Holds date issued information"""
	def __init__(self):
		self.value = ''
		self.encoding = ''
		self.qualifier = ''
		self.keyDate = ''	

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'dateIssued')
		
		if(self.encoding):
			topLevel.set('encoding', self.encoding.strip())

		if(self.qualifier):
			topLevel.set('qualifier', self.qualifier.strip())	

		if(self.keyDate):
			topLevel.set('keyDate', self.keyDate.strip())

		topLevel.text = self.value.strip()

		return topLevel

class OriginInfo:
	"""Holds origin info information"""
	def __init__(self):
		self.value = ''	

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'originInfo')
		return topLevel

class Place:
	"""Holds place information"""
	def __init__(self):
		self.value = ''	

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'place')
		return topLevel

class PlaceTerm:
	"""Holds place term information"""
	def __init__(self):
		self.type = ''
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'placeTerm')
		
		if(self.type):
			topLevel.set('type', self.type.strip())

		topLevel.text = self.value.strip()

		return topLevel

class RelatedItem:
	"""Holds Releated Item information"""
	def __init__(self):
		self.type = ''
		self.value = ''	

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'relatedItem')
		if(self.type):
			topLevel.set('type', self.type.strip())
		 
		return topLevel

class TitleInfo:
	"""Holds identifier information"""
	def __init__(self):
		self.value = ''	

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'titleInfo')
		return topLevel

class Title:
	"""Holds title information"""
	def __init__(self):
		self.value = ''	

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'title')
		topLevel.text = self.value.strip()
		return topLevel


class Location:
	"""Holds identifier information"""
	def __init__(self):
		self.value = ''	

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'location')
		return topLevel

class PhysicalLocation:
	"""Holds physical location information"""
	def __init__(self):
		self.value = ''	

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'physicalLocation')
		topLevel.text = self.value.strip()
		return topLevel


class ShelfLocator:
	"""Holds shelf locator information"""
	def __init__(self):
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'shelfLocator')
		topLevel.text = self.value.strip()
		return topLevel

class AccessCondition:
	"""Holds access condition information"""
	def __init__(self):
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'accessCondition')
		topLevel.text = self.value.strip()
		return topLevel

class Identifier:
	"""Holds identifier information"""
	def __init__(self):
		self.type = ''
		self.value = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'identifier')
		if(self.type):
			topLevel.set('type', self.type.strip())
		 
		
		topLevel.text = self.value.strip()
		return topLevel


