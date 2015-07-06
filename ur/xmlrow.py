#!/usr/bin/python

import xml.etree.ElementTree as ET
import ur.mods as mods
import csv

# ##########################################
# Buidl the xml file using the MODS classes
# ##########################################
def buildXml(row):
	print('build xml')
	root = ET.Element('mods', {"xmlns:xlink":"http://www.w3.org/1999/xlink", 
		"xmlns:xsi":"http://www.w3.org/2001/XMLSchema-instance",
	    "xmlns":"http://www.loc.gov/mods/v3",
	    "version":"3.5",
	    "xsi:schemaLocation":"http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd"})


	if( row[0] ):
		jobNumber = mods.Identifier()
		jobNumber.type = 'job'
		jobNumber.value = row[0]
		jobNumber.toModsElement(root)

	#physical location information
	if( row[1] ):
		location = mods.Location()
		locationElement = location.toModsElement(root)


		physicalLocation = mods.PhysicalLocation()
		physicalLocation.value = row[1]
		physicalLocation.toModsElement(locationElement)

	#shelf location information
	if( row[2] ):
		shelfLocator = mods.ShelfLocator()
		shelfLocator.value = row[2]
		shelfLocator.toModsElement(locationElement)

	#title information
	if( row[3] ): 
		titleInfo = mods.TitleInfo()
		titleInfoElement = titleInfo.toModsElement(root)

		title = mods.Title()
		title.value = row[3]

		title.toModsElement(titleInfoElement)

	#related item information
	if( row[4] ):
		relatedItem = mods.RelatedItem()
		relatedItem.type = 'host'
		relatedItemElement = relatedItem.toModsElement(root)


		titleInfo2 = mods.TitleInfo()
		titleInfoElement2 = titleInfo2.toModsElement(relatedItemElement)
		title2 = mods.Title()
		title2.value = row[4]

		title2.toModsElement(titleInfoElement2)

	if( row[5] or row[6] or row[7] or row[8] or row[9] or row[10]):
		originInfoElement = mods.OriginInfo().toModsElement(root)

		# date created information
		if( row[5]):
			dateCreated = mods.DateCreated()
			dateCreated.value = row[5]
			dateCreated.encoding = "w3cdtf"
			dateCreated.keyDate = "yes"
			dateCreated.toModsElement(originInfoElement)

			#add date issued so it shows up in dublin core
			dateIssued = mods.DateIssued()
			dateIssued.value = row[5]
			dateIssued.encoding = "w3cdtf"
			dateIssued.keyDate = "yes"
			dateIssued.toModsElement(originInfoElement)


		# date approximate
		if( row[6] ):
			dateApproximate = mods.DateCreated()
			dateApproximate.value = row[6]
			dateApproximate.encoding = "w3cdtf"
			dateApproximate.qualifier = "approximate"
			dateApproximate.toModsElement(originInfoElement)

		# date inferred
		if( row[7] ):
			dateInferred = mods.DateCreated()
			dateInferred.value = row[7]
			dateInferred.encoding = "w3cdtf"
			dateInferred.qualifier = "inferred"
			dateInferred.toModsElement(originInfoElement)

		# date questionable
		if( row[8] ):
			dateQuestionable = mods.DateCreated()
			dateQuestionable.value = row[8]
			dateQuestionable.encoding = "w3cdtf"
			dateQuestionable.qualifier = "questionable"
			dateQuestionable.toModsElement(originInfoElement)

		# begin date
		if( row[9] ):
			dateBegin = mods.DateCreated()
			dateBegin.value = row[9]
			dateBegin.encoding = "marc"
			dateBegin.point = "start"
			dateBegin.toModsElement(originInfoElement)

		# end date
		if( row[10] ):
			endBegin = mods.DateCreated()
			endBegin.value = row[10]
			endBegin.encoding = "marc"
			endBegin.point = "end"
			endBegin.toModsElement(originInfoElement)

		#geo location information
		if( row[16] ):
			placeElement = mods.Place().toModsElement(originInfoElement)
			placeTerm = mods.PlaceTerm()
			placeTerm.type = "text"
			placeTerm.value = row[16]
			placeTerm.toModsElement(placeElement)

		if( row[38] ):
			publisher = mods.Publisher()
			publisher.value = row[38]
			publisher.toModsElement(originInfoElement)

	#personal name element (Letter creator)
	if( row[11] ):
		name = mods.Name()

		name.type = "personal"

		#name type (personal/corporate)
		if(row[12]):
			name.type = row[12]

 
		name1Element = name.toModsElement(root)
		namePart = mods.NamePart()
		namePart.value = row[11]
	

		namePart.toModsElement(name1Element)
		roleElement = mods.Role().toModsElement(name1Element)

		#role of the person
		if( row[13] ):
			roleTerm = mods.RoleTerm()
			roleTerm.authority = "marcrelator"
			roleTerm.type = "text"
			roleTerm.value = row[13]
			roleTerm.toModsElement(roleElement)


	#abstract information
	if( row[15] ):
		abstract = mods.Abstract()
		abstract.value = row[15]
		abstract.toModsElement(root)

	

	#language information
	if( row[17] ):
		languageElement = mods.Language().toModsElement(root)
		languageTerm = mods.LanguageTerm()
		languageTerm.type = "text"
		languageTerm.value = row[17]
		languageTerm.toModsElement(languageElement)

	#related name (Letter recipient)
	if( row[18] ):
		relatedName = mods.Name()
		relatedName.type = 'personal'

		if(row[19]):
			relatedName.type = row[19]

		relatedNameElement = relatedName.toModsElement(root)
		relatedNamePart = mods.NamePart()
		relatedNamePart.value = row[18]
	
		relatedNamePart.toModsElement(relatedNameElement)
		roleElement2 = mods.Role().toModsElement(relatedNameElement)

		if( row[20] ):
			roleTerm2 = mods.RoleTerm()
			roleTerm2.authority = "marcrelator"
			roleTerm2.type = "text"
			roleTerm2.value = row[20]
			roleTerm2.toModsElement(roleElement2)

	#genre information
	if( row[22] ):
		genre = mods.Genre()
		genre.authority = "gmgpc"
		genre.value = row[22]
		genre.toModsElement(root)

	#subject - topic information
	if( row[23] ):
		topicSubjectElement = mods.Subject().toModsElement(root)
		topic = mods.Topic()
		topic.value = row[23]
		topic.toModsElement(topicSubjectElement) 

	#subject - name information
	if( row[24] ):
		nameSubjectRootElement = mods.Subject().toModsElement(root)
		nameSubject = mods.Name()
		nameSubject.type = "personal"
		nameSubjectElement = nameSubject.toModsElement(nameSubjectRootElement)
		nameSubjectPart = mods.NamePart()
		nameSubjectPart.value = row[24]
		nameSubjectPart.toModsElement(nameSubjectElement)

	#subject - corporation name information
	if( row[25] ):
		corpSubjectRootElement = mods.Subject().toModsElement(root)
		corpSubject = mods.Name()
		corpSubject.type = "corporate"
		corpSubjectElement = corpSubject.toModsElement(corpSubjectRootElement)
		corpSubjectPart = mods.NamePart()
		corpSubjectPart.value = row[25]
		corpSubjectPart.toModsElement(corpSubjectElement)

	#subject geographic information
	if( row[26] ):
		geoSubjectRootElement = mods.Subject().toModsElement(root)
		geo = mods.Geographic()
		geo.value = row[26]
		geo.toModsElement(geoSubjectRootElement)


	# physical description/form
	if( row[27] or row[28] or row[29]):
		physicalDescriptionElement = mods.PhysicalDescription().toModsElement(root)
		
		if( row[27] ):
			form = mods.Form()
			form.authority = "marcform"
			form.value = row[27]
			form.toModsElement(physicalDescriptionElement)

		# media type e.g. image/tiff
		if( row[28] ):
			internetMediaType = mods.InternetMediaType()
			internetMediaType.value = row[28]
			internetMediaType.toModsElement(physicalDescriptionElement)
	
		if( row[29] ):

			#extent
			extent = mods.Extent()
			extent.value = row[29] + " pages"
			extent.toModsElement(physicalDescriptionElement)

	# note
	if( row[33] ):
		note = mods.Note()
		note.value = row[33]
		note.toModsElement(root)

	#type of resource
	if( row[34] ):
		typeOfResource = mods.TypeOfResource()
		typeOfResource.value = row[34]
		typeOfResource.toModsElement(root)

	#source and language of cataloging
	if( row[35] or row[36] ):
		recordInfoElement = mods.RecordInfo().toModsElement(root)
		#source information
		if( row[35] ):
			recordSource = mods.RecordContentSource()
			recordSource.value = row[35]
			recordSource.toModsElement(recordInfoElement)
		if( row[36] ):
			langOfCatElement = mods.LanguageOfCataloging().toModsElement(recordInfoElement)
			recordLangauge = mods.LanguageTerm()
			recordLangauge.value = row[36]
			recordLangauge.type = "code"
			recordLangauge.authority = "iso639-2b"
			recordLangauge.toModsElement(langOfCatElement)

	#rights access
	if( row[37] ):
		accessCondition = mods.AccessCondition()
		accessCondition.value = row[37]
		accessCondition.toModsElement(root)

	#ET.dump(root)
	
	
	return root


# ##################################################
#  Create an xml with the data from the xml file
# ##################################################
def createXmlFile(row, fileName):
	print("XML file name will be = " + fileName )
	rootNode = buildXml(row)
	tree = ET.ElementTree(rootNode)

	if( fileName ):
		tree.write(fileName)

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
			for x in range(0,39):
				print("row " + str(x) + " = " + row[x])
			print("*************  DONE - " + str(counter) + " *********************" )
			print("")

