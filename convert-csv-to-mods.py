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

	def toModsElement(self, parentElement):
		topLevel = ET.SubElement(parentElement, 'dateCreated')
		
		if(self.encoding):
			topLevel.set('encoding', self.encoding.strip())

		if(self.qualifier):
			topLevel.set('qualifier', self.qualifier.strip())	

		if(self.keyDate):
			topLevel.set('keyDate', self.keyDate.strip())

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
		dateCreated.keyDate = "yes"
		dateCreated.toModsElement(originInfoElement)

		#add date issued so it shows up in dublin core
		dateIssued = DateIssued()
		dateIssued.value = row[5]
		dateIssued.encoding = "w3cdtf"
		dateIssued.keyDate = "yes"
		dateIssued.toModsElement(originInfoElement)


	# date approximate
	if( row[6] ):
		dateApproxInfoElement = OriginInfo().toModsElement(root)
		dateApproximate = DateCreated()
		dateApproximate.value = row[6]
		dateApproximate.encoding = "w3cdtf"
		dateApproximate.qualifier = "approximate"
		dateApproximate.toModsElement(dateApproxInfoElement)

	# date inferred
	if( row[7] ):
		dateInferredInfoElement = OriginInfo().toModsElement(root)
		dateInferred = DateCreated()
		dateInferred.value = row[7]
		dateInferred.encoding = "w3cdtf"
		dateInferred.qualifier = "inferred"
		dateInferred.toModsElement(dateInferredInfoElement)

	# date questionable
	if( row[8] ):
		dateQuestionableInfoElement = OriginInfo().toModsElement(root)
		dateQuestionable = DateCreated()
		dateQuestionable.value = row[8]
		dateQuestionable.encoding = "w3cdtf"
		dateQuestionable.qualifier = "questionable"

		dateQuestionable.toModsElement(dateQuestionableInfoElement)

	#personal name element (Letter creator)
	if( row[9] ):
		name = Name()
		name.type = "personal"
 
		name1Element = name.toModsElement(root)
		namePart = NamePart()
		namePart.value = row[9]
	

		namePart.toModsElement(name1Element)
		roleElement = Role().toModsElement(name1Element)

		#role of the person
		if( row[10] ):
			roleTerm = RoleTerm()
			roleTerm.authority = "marcrelator"
			roleTerm.type = "text"
			roleTerm.value = row[10]
			roleTerm.toModsElement(roleElement)



	#abstract information
	if( row[11] ):
		abstract = Abstract()
		abstract.value = row[11]
		abstract.toModsElement(root)

	#geo location information
	if( row[12] ):
		geoLocationElement = OriginInfo().toModsElement(root)
		placeElement = Place().toModsElement(geoLocationElement)
		placeTerm = PlaceTerm()
		placeTerm.type = "text"
		placeTerm.value = row[12]
		placeTerm.toModsElement(placeElement)

	#language information
	if( row[13] ):
		languageElement = Language().toModsElement(root)
		languageTerm = LanguageTerm()
		languageTerm.type = "text"
		languageTerm.value = row[13]
		languageTerm.toModsElement(languageElement)

	#related name (Letter recipient)
	if( row[14] ):
		relatedName = Name().toModsElement(root)
		relatedNamePart = NamePart()
		relatedNamePart.value = row[14]
	
		relatedNamePart.toModsElement(relatedName)
		roleElement2 = Role().toModsElement(relatedName)

		if( row[15] ):
			roleTerm2 = RoleTerm()
			roleTerm2.authority = "marcrelator"
			roleTerm2.type = "text"
			roleTerm2.value = row[15]
			roleTerm2.toModsElement(roleElement2)

	#genre information
	if( row[16] ):
		genre = Genre()
		genre.authority = "gmgpc"
		genre.value = row[16]
		genre.toModsElement(root)

	#subject - topic information
	if( row[17] ):
		topicSubjectElement = Subject().toModsElement(root)
		topic = Topic()
		topic.value = row[17]
		topic.toModsElement(topicSubjectElement) 

	#subject - name information
	if( row[18] ):
		nameSubjectRootElement = Subject().toModsElement(root)
		nameSubject = Name()
		nameSubject.type = "personal"
		nameSubjectElement = nameSubject.toModsElement(nameSubjectRootElement)
		nameSubjectPart = NamePart()
		nameSubjectPart.value = row[18]
		nameSubjectPart.toModsElement(nameSubjectElement)

	#subject - corporation name information
	if( row[19] ):
		corpSubjectRootElement = Subject().toModsElement(root)
		corpSubject = Name()
		corpSubject.type = "corporate"
		corpSubjectElement = corpSubject.toModsElement(corpSubjectRootElement)
		corpSubjectPart = NamePart()
		corpSubjectPart.value = row[19]
		corpSubjectPart.toModsElement(corpSubjectElement)

	#subject geographic information
	if( row[20] ):
		geoSubjectRootElement = Subject().toModsElement(root)
		geo = Geographic()
		geo.value = row[20]
		geo.toModsElement(geoSubjectRootElement)


	# physical description/form
	if( row[21] or row[22] or row[23]):
		physicalDescriptionElement = PhysicalDescription().toModsElement(root)
		
		if( row[21] ):
			form = Form()
			form.authority = "marcform"
			form.value = row[21]
			form.toModsElement(physicalDescriptionElement)

		# media type e.g. image/tiff
		if( row[22] ):
			internetMediaType = InternetMediaType()
			internetMediaType.value = row[22]
			internetMediaType.toModsElement(physicalDescriptionElement)
	
		if( row[23] ):

			pageStr = " pages"

			if(int(row[23]) <= 1) :
				pageStr = " page"

			#extent
			extent = Extent()
			extent.value = row[23] + pageStr
			extent.toModsElement(physicalDescriptionElement)

	# note
	if( row[26] ):
		note = Note()
		note.value = row[26]
		note.toModsElement(root)

	#type of resource
	if( row[27] ):
		typeOfResource = TypeOfResource()
		typeOfResource.value = row[27]
		typeOfResource.toModsElement(root)

	#source and language of cataloging
	if( row[28] or row[29] ):
		recordInfoElement = RecordInfo().toModsElement(root)
		#source information
		if( row[28] ):
			recordSource = RecordContentSource()
			recordSource.value = row[28]
			recordSource.toModsElement(recordInfoElement)
		if( row[29] ):
			langOfCatElement = LanguageOfCataloging().toModsElement(recordInfoElement)
			recordLangauge = LanguageTerm()
			recordLangauge.value = row[29]
			recordLangauge.type = "code"
			recordLangauge.authority = "iso639-2b"
			recordLangauge.toModsElement(langOfCatElement)

	#rights access
	if( row[30] ):
		accessCondition = AccessCondition()
		accessCondition.value = row[30]
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


def createPageStructure(pages, baseDirectory, baseFilename, bookDir):
	#default format - no leading zeros
	pageFormat = "{0:01d}"

	if( pages > 9 and pages < 99):
		#one leading zero
		pageFormat = "{0:02d}"
	elif( pages > 99 and pages < 999):
		#two leading zeros
		pageFormat = "{0:03d}"
	elif( pages > 999 and pages < 9999):
		#three leading zeros
		pageFormat = "{0:04d}"

	for page in range(1, pages):
		pageName = pageFormat.format(page)
		filename = baseFilename + "-" + str(page) + ".tif"
		sourceFile = os.path.join(baseDirectory, filename)
		if( not os.path.isfile(sourceFile) ):
			print("Could not find file " + sourceFile)
			sys.exit()
		else:
			pageDir = os.path.join(bookDir, "page-" + pageName)
			destFile = os.path.join(pageDir, "OBJ.tif")
			print("source  = " + sourceFile + " dest = " + destFile)
			print ("creating directory " + pageDir)
			os.mkdir(pageDir)
			shutil.copy(sourceFile, destFile)


def createFileStructure(counter, row, baseDirectory, outputDirectory):
	#base file name
	baseFilename = row[25]
	#off by one so increase so it works correctly
	pages = int(row[23]) + 1
	print("filename = " + baseFilename)
	bookDir = os.path.join(outputDirectory, str(counter))
	print("creating directory " + bookDir)
	os.mkdir(bookDir)
	createXmlFile(row, counter, bookDir)
	createPageStructure(pages, baseDirectory, baseFilename, bookDir)

	


def printCsvInfo(aFile):
	with open(aFile, 'r') as csvfile:
		fileReader = csv.reader(csvfile)
		counter = 1
		for row in fileReader:
			print("************* " + str(counter) + " *********************" )
			counter = counter + 1
			for x in range(0,31):
				print("row " + str(x) + " = " + row[x])
			print("*************  DONE - " + str(counter) + " *********************" )
			print("")

				






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

test = input("Test csv file (yes) to test: ")
if( test == "yes"):
	print("testing csv file")
	printCsvInfo(aFile)
else:
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
			if( row[23] ):
				pages = int(row[23])
				if( pages > 0):
					print("processing " + str(pages) + " pages")
					createFileStructure(counter, row, baseDirectory, outputDirectory)
			
			else:
				print ("Skipping row " + str(counter) + " pages found were " + row[23] )
			counter += 1
		
		

