#!/usr/bin/python

import csv
import xml.etree.ElementTree as ET
import xml.dom.minidom
import datetime
import os
import logging
import sys
import shutil


from xml.dom.minidom import Node 


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



class Subject:
	"""Holds subject information"""
	def __init__(self):
		self.type = ''

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'subject')
		
		if(self.type):
			topLevel.set('type', self.type.strip())

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
		self.qualifer = ''	

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'dateCreated')
		
		if(self.encoding):
			topLevel.set('encoding', self.encoding.strip())

		if(self.qualifer):
			topLevel.set('qualifer', self.qualifier.strip())	

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


def buildXml(row):
	print('build xml')
	root = ET.Element('mods', {"xmlns:xlink":"http://www.w3.org/1999/xlink", 
		"xmlns:xsi":"http://www.w3.org/2001/XMLSchema-instance",
	    "xmlns":"http://www.loc.gov/mods/v3",
	    "version":"3.5",
	    "xsi:schemaLocation":"http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd"})


	if( row[0] ):
		jobNumber = Identifier()
		jobNumber.type = 'job'
		jobNumber.value = row[0]
		jobNumber.toModsElement(root)

	#physical location information
	if( row[1] ):
		location = Location()
		locationElement = location.toModsElement(root)


		physicalLocation = PhysicalLocation()
		physicalLocation.value = row[1]
		physicalLocation.toModsElement(locationElement)

	#shelf location information
	if( row[2] ):
		shelfLocator = ShelfLocator()
		shelfLocator.value = row[2]
		shelfLocator.toModsElement(locationElement)

	#title information
	if( row[3] ): 
		titleInfo = TitleInfo()
		titleInfoElement = titleInfo.toModsElement(root)

		title = Title()
		title.value = row[3]

		title.toModsElement(titleInfoElement)

	#related item information
	if( row[4] ):
		relatedItem = RelatedItem()
		relatedItem.type = 'host'
		relatedItemElement = relatedItem.toModsElement(root)


		titleInfo2 = TitleInfo()
		titleInfoElement2 = titleInfo2.toModsElement(relatedItemElement)
		title2 = Title()
		title2.value = row[4]

		title2.toModsElement(titleInfoElement2)

	# date created information
	if( row[5] ):
		originInfoElement = OriginInfo().toModsElement(root)
		dateCreated = DateCreated()
		dateCreated.value = row[5]
		dateCreated.encoding = "w3cdtf"
		dateCreated.toModsElement(originInfoElement)

	#personal name element (Letter creator)
	if( row[6] ):
		name = Name()
		name.type = "personal"
 
		name1Element = name.toModsElement(root)
		namePart = NamePart()
		namePart.value = row[6]
	

		namePart.toModsElement(name1Element)
		roleElement = Role().toModsElement(name1Element)

		#role of the person
		if( row[7] ):
			roleTerm = RoleTerm()
			roleTerm.authority = "marcrelator"
			roleTerm.type = "text"
			roleTerm.value = row[7]
			roleTerm.toModsElement(roleElement)



	#abstract information
	if( row[8] ):
		abstract = Abstract()
		abstract.value = row[8]
		abstract.toModsElement(root)

	#geo location information
	if( row[9] ):
		geoLocationElement = OriginInfo().toModsElement(root)
		placeElement = Place().toModsElement(geoLocationElement)
		placeTerm = PlaceTerm()
		placeTerm.type = "text"
		placeTerm.value = row[9]
		placeTerm.toModsElement(placeElement)

	#related name (Letter recipient)
	if( row[10] ):
		relatedName = Name().toModsElement(root)
		relatedNamePart = NamePart()
		relatedNamePart.value = row[10]
	
		relatedNamePart.toModsElement(relatedName)
		roleElement2 = Role().toModsElement(relatedName)

		if( row[11] ):
			roleTerm2 = RoleTerm()
			roleTerm2.authority = "marcrelator"
			roleTerm2.type = "text"
			roleTerm2.value = row[11]
			roleTerm2.toModsElement(roleElement2)

	#genre information
	if( row[12] ):
		genre = Genre()
		genre.authority = "gmgpc"
		genre.value = row[12]
		genre.toModsElement(root)

	# physical description/form
	if( row[13] or row[14] or row[15]):
		physicalDescriptionElement = PhysicalDescription().toModsElement(root)
		
		if( row[13] ):
			form = Form()
			form.authority = "marcform"
			form.value = row[13]
			form.toModsElement(physicalDescriptionElement)

		# media type e.g. image/tiff
		if( row[14] ):
			internetMediaType = InternetMediaType()
			internetMediaType.value = row[14]
			internetMediaType.toModsElement(physicalDescriptionElement)
	
		if( row[15] ):
			#extent
			extent = Extent()
			extent.value = row[15]
			extent.toModsElement(physicalDescriptionElement)

	# note
	if( row[18] ):
		note = Note()
		note.value = row[18]
		note.toModsElement(root)

	#type of resource
	if( row[19] ):
		typeOfResource = TypeOfResource()
		typeOfResource.value = row[19]
		typeOfResource.toModsElement(root)

	
	if( row[20] or row[21] ):
		recordInfoElement = RecordInfo().toModsElement(root)
		#source information
		if( row[20] ):
			recordSource = RecordContentSource()
			recordSource.value = row[20]
			recordSource.toModsElement(recordInfoElement)
		if( row[21] ):
			langOfCatElement = LanguageOfCataloging().toModsElement(recordInfoElement)
			recordLangauge = LanguageTerm()
			recordLangauge.value = row[21]
			recordLangauge.type = "code"
			recordLangauge.authority = "iso639-2b"
			recordLangauge.toModsElement(langOfCatElement)


	accessCondition = AccessCondition()
	accessCondition.value = "This image may be protected by the U.S. Copyright Law (Title 17, U.S.C.). It is displayed here only for the purposes of research. The written permission of the copyright owners may be required for distribution or reproduction beyond that allowed by fair use. All responsibility for obtaining permissions, and for any use rests exclusively with the user. Also see: http://www.library.rochester.edu/copyright"
	accessCondition.toModsElement(root)

	#ET.dump(root)
	
	
	return root


def createXmlFile(row, counter, bookDir):
	aFileName = os.path.join(bookDir, "MODS" + ".xml")
	print("XML file name will be = " + aFileName )
	rootNode = buildXml(row)
	tree = ET.ElementTree(rootNode)

	if( aFileName ):
		tree.write(aFileName)


def createFileStructure(counter, row, baseDirectory, outputDirectory):
	#base file name
	baseFilename = row[17]
	#off by one so increase so it works correctly
	pages = int(row[15]) + 1
	print("filename = " + baseFilename)
	bookDir = os.path.join(outputDirectory, str(counter))
	print("creating directory " + bookDir)
	os.mkdir(bookDir)
	createXmlFile(row, counter, bookDir)
	for page in range(1, pages):
		filename = baseFilename + "-" + str(page) + ".tif"
		sourceFile = os.path.join(baseDirectory, filename)
		if( not os.path.isfile(sourceFile) ):
			print("Could not find file " + sourceFile)
			sys.exit()
		else:
			pageDir = os.path.join(bookDir, "page-" + str(page))
			destFile = os.path.join(pageDir, "OBJ.tif")
			print("source  = " + sourceFile + " dest = " + destFile)
			print ("creating directory " + pageDir)
			os.mkdir(pageDir)
			shutil.copy(sourceFile, destFile)

				






# ########################################
# Main Program
# ########################################

#get the csv file input
aFile = input("Please enter csv file name: ")
if( not os.path.isfile(aFile) ):
	print("Could not find file " + aFile)
	sys.exit()
else:
	print ("found file ")

#base directory of files to import
baseDirectory = input("Please enter directory of files to import: ")
if( not os.path.isdir(baseDirectory) ):
	print("Directory " + baseDirectory + " does not exist or is not a directory")
	sys.exit()
else:
	print("Directory found " + baseDirectory) 

#output directory for processing
outputDirectory = input("Please enter output directory: ")
if( not os.path.isdir(baseDirectory) ):
	print("Directory " + baseDirectory + " does not exist or is not a directory")
	sys.exit()
else:
	print("Directory found " + baseDirectory) 


#open the csv and start iterating through the rows
with open(aFile, 'r') as csvfile:
	fileReader = csv.reader(csvfile)
	counter = 1
	for row in fileReader:
		if( row[15] ):
			pages = int(row[15])
			if( pages > 0):
				print("processing " + str(pages) + " pages")
				createFileStructure(counter, row, baseDirectory, outputDirectory)
				
			
		else:
			print ("Skipping row " + str(counter) + " pages found were " + row[15] )
		counter += 1
		
		

