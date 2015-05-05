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

# #########################################################
# Represents all the metadata classes for import
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

#
# Buidl the xml file using the above classes
#
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

	# begin date
	if( row[9] ):
		beginDateInfoElement = OriginInfo().toModsElement(root)
		dateBegin = DateCreated()
		dateBegin.value = row[9]
		dateBegin.encoding = "marc"
		dateBegin.point = "start"

		dateBegin.toModsElement(beginDateInfoElement )

	# end date
	if( row[10] ):
		endDateInfoElement = OriginInfo().toModsElement(root)
		endBegin = DateCreated()
		endBegin.value = row[10]
		endBegin.encoding = "marc"
		endBegin.point = "end"

		endBegin.toModsElement(endDateInfoElement )

	#personal name element (Letter creator)
	if( row[11] ):
		name = Name()
		name.type = "personal"
 
		name1Element = name.toModsElement(root)
		namePart = NamePart()
		namePart.value = row[11]
	

		namePart.toModsElement(name1Element)
		roleElement = Role().toModsElement(name1Element)

		#role of the person
		if( row[12] ):
			roleTerm = RoleTerm()
			roleTerm.authority = "marcrelator"
			roleTerm.type = "text"
			roleTerm.value = row[12]
			roleTerm.toModsElement(roleElement)



	#abstract information
	if( row[13] ):
		abstract = Abstract()
		abstract.value = row[13]
		abstract.toModsElement(root)

	#geo location information
	if( row[14] ):
		geoLocationElement = OriginInfo().toModsElement(root)
		placeElement = Place().toModsElement(geoLocationElement)
		placeTerm = PlaceTerm()
		placeTerm.type = "text"
		placeTerm.value = row[14]
		placeTerm.toModsElement(placeElement)

	#language information
	if( row[15] ):
		languageElement = Language().toModsElement(root)
		languageTerm = LanguageTerm()
		languageTerm.type = "text"
		languageTerm.value = row[15]
		languageTerm.toModsElement(languageElement)

	#related name (Letter recipient)
	if( row[16] ):
		relatedName = Name().toModsElement(root)
		relatedNamePart = NamePart()
		relatedNamePart.value = row[16]
	
		relatedNamePart.toModsElement(relatedName)
		roleElement2 = Role().toModsElement(relatedName)

		if( row[17] ):
			roleTerm2 = RoleTerm()
			roleTerm2.authority = "marcrelator"
			roleTerm2.type = "text"
			roleTerm2.value = row[17]
			roleTerm2.toModsElement(roleElement2)

	#genre information
	if( row[18] ):
		genre = Genre()
		genre.authority = "gmgpc"
		genre.value = row[18]
		genre.toModsElement(root)

	#subject - topic information
	if( row[19] ):
		topicSubjectElement = Subject().toModsElement(root)
		topic = Topic()
		topic.value = row[19]
		topic.toModsElement(topicSubjectElement) 

	#subject - name information
	if( row[20] ):
		nameSubjectRootElement = Subject().toModsElement(root)
		nameSubject = Name()
		nameSubject.type = "personal"
		nameSubjectElement = nameSubject.toModsElement(nameSubjectRootElement)
		nameSubjectPart = NamePart()
		nameSubjectPart.value = row[20]
		nameSubjectPart.toModsElement(nameSubjectElement)

	#subject - corporation name information
	if( row[21] ):
		corpSubjectRootElement = Subject().toModsElement(root)
		corpSubject = Name()
		corpSubject.type = "corporate"
		corpSubjectElement = corpSubject.toModsElement(corpSubjectRootElement)
		corpSubjectPart = NamePart()
		corpSubjectPart.value = row[21]
		corpSubjectPart.toModsElement(corpSubjectElement)

	#subject geographic information
	if( row[22] ):
		geoSubjectRootElement = Subject().toModsElement(root)
		geo = Geographic()
		geo.value = row[22]
		geo.toModsElement(geoSubjectRootElement)


	# physical description/form
	if( row[23] or row[24] or row[25]):
		physicalDescriptionElement = PhysicalDescription().toModsElement(root)
		
		if( row[23] ):
			form = Form()
			form.authority = "marcform"
			form.value = row[23]
			form.toModsElement(physicalDescriptionElement)

		# media type e.g. image/tiff
		if( row[24] ):
			internetMediaType = InternetMediaType()
			internetMediaType.value = row[24]
			internetMediaType.toModsElement(physicalDescriptionElement)
	
		if( row[25] ):

			pageStr = " pages"

			if(int(row[25]) <= 1) :
				pageStr = " page"

			#extent
			extent = Extent()
			extent.value = row[25] + pageStr
			extent.toModsElement(physicalDescriptionElement)

	# note
	if( row[28] ):
		note = Note()
		note.value = row[28]
		note.toModsElement(root)

	#type of resource
	if( row[29] ):
		typeOfResource = TypeOfResource()
		typeOfResource.value = row[29]
		typeOfResource.toModsElement(root)

	#source and language of cataloging
	if( row[30] or row[31] ):
		recordInfoElement = RecordInfo().toModsElement(root)
		#source information
		if( row[30] ):
			recordSource = RecordContentSource()
			recordSource.value = row[30]
			recordSource.toModsElement(recordInfoElement)
		if( row[31] ):
			langOfCatElement = LanguageOfCataloging().toModsElement(recordInfoElement)
			recordLangauge = LanguageTerm()
			recordLangauge.value = row[31]
			recordLangauge.type = "code"
			recordLangauge.authority = "iso639-2b"
			recordLangauge.toModsElement(langOfCatElement)

	#rights access
	if( row[32] ):
		accessCondition = AccessCondition()
		accessCondition.value = row[32]
		accessCondition.toModsElement(root)

	#ET.dump(root)
	
	
	return root


#
#  Create an xml with the data from the xml file
#
def createXmlFile(row, counter, fileName):
	print("XML file name will be = " + fileName )
	rootNode = buildXml(row)
	tree = ET.ElementTree(rootNode)

	if( fileName ):
		tree.write(fileName)


#
# Creates a folder for every page based on the file name - this is a
# requirement of islandora
#
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
		filename = baseFilename + "_" + str(page) + ".tif"
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


#
#  Create the file structure for a book in islandora
#
def createFileStructure(counter, row, baseDirectory, outputDirectory):
	#base file name
	baseFilename = row[27]
	#off by one so increase so it works correctly
	pages = int(row[25]) + 1
	print("filename = " + baseFilename)
	bookDir = os.path.join(outputDirectory, str(counter))
	print("creating directory " + bookDir)
	os.mkdir(bookDir)
	xmlFile = os.path.join(bookDir, "MODS" + ".xml")
	createXmlFile(row, counter, xmlFile)
	createPageStructure(pages, baseDirectory, baseFilename, bookDir)

	

# 
#  Use this to print out the fields of a csv file and allows programmer
#  to see the output
#
def printCsvInfo(aFile):
	with open(aFile, 'r') as csvfile:
		fileReader = csv.reader(csvfile)
		counter = 1
		for row in fileReader:
			print("************* " + str(counter) + " *********************" )
			counter = counter + 1
			for x in range(0,33):
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
if( test.lower() == "yes"):
	print("testing csv file")
	printCsvInfo(aFile)

	testXml = input("Test xml output (yes) to test: ")
	if(testXml.lower() == "yes" ):
		outputDirectory = input("Please enter xml output directory: ")
		if( not os.path.isdir(outputDirectory) ):
			print("Directory " + outputDirectory + " does not exist or is not a directory")
			sys.exit()
		else:
			print("Directory found " + outputDirectory)
			 #open the csv and start iterating through the rows
			with open(aFile, 'r') as csvfile:
				fileReader = csv.reader(csvfile)
				counter = 1
				for row in fileReader:
					if( row[25] ):
						pages = int(row[25])
						if( pages > 0):
							print("processing " + str(pages) + " pages")
							xmlFile = os.path.join(outputDirectory, "MODS_" + str(counter) + ".xml")
							createXmlFile(row, counter, xmlFile)			
					else:
						print ("Skipping row " + str(counter) + " pages found were " + row[25] )
					counter += 1

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
	if( not os.path.isdir(outputDirectory ) ):
		print("Directory " + outputDirectory  + " does not exist or is not a directory")
		sys.exit()
	else:
		print("Directory found " + outputDirectory ) 

	#open the csv and start iterating through the rows
	with open(aFile, 'r') as csvfile:
		fileReader = csv.reader(csvfile)
		counter = 1
		for row in fileReader:
			if( row[25] ):
				pages = int(row[25])
				if( pages > 0):
					print("processing " + str(pages) + " pages")
					createFileStructure(counter, row, baseDirectory, outputDirectory)
			
			else:
				print ("Skipping row " + str(counter) + " pages found were " + row[25] )
			counter += 1
		
		

