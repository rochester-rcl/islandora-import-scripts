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

	# date created information
	if( row[5] ):
		originInfoElement = mods.OriginInfo().toModsElement(root)
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
		dateApproxInfoElement = mods.OriginInfo().toModsElement(root)
		dateApproximate = mods.DateCreated()
		dateApproximate.value = row[6]
		dateApproximate.encoding = "w3cdtf"
		dateApproximate.qualifier = "approximate"
		dateApproximate.toModsElement(dateApproxInfoElement)

	# date inferred
	if( row[7] ):
		dateInferredInfoElement = mods.OriginInfo().toModsElement(root)
		dateInferred = mods.DateCreated()
		dateInferred.value = row[7]
		dateInferred.encoding = "w3cdtf"
		dateInferred.qualifier = "inferred"
		dateInferred.toModsElement(dateInferredInfoElement)

	# date questionable
	if( row[8] ):
		dateQuestionableInfoElement = mods.OriginInfo().toModsElement(root)
		dateQuestionable = DateCreated()
		dateQuestionable.value = row[8]
		dateQuestionable.encoding = "w3cdtf"
		dateQuestionable.qualifier = "questionable"

		dateQuestionable.toModsElement(dateQuestionableInfoElement)

	# begin date
	if( row[9] ):
		beginDateInfoElement = mods.OriginInfo().toModsElement(root)
		dateBegin = mods.DateCreated()
		dateBegin.value = row[9]
		dateBegin.encoding = "marc"
		dateBegin.point = "start"

		dateBegin.toModsElement(beginDateInfoElement )

	# end date
	if( row[10] ):
		endDateInfoElement = mods.OriginInfo().toModsElement(root)
		endBegin = mods.DateCreated()
		endBegin.value = row[10]
		endBegin.encoding = "marc"
		endBegin.point = "end"

		endBegin.toModsElement(endDateInfoElement )

	#personal name element (Letter creator)
	if( row[11] ):
		name = mods.Name()
		name.type = "personal"
 
		name1Element = name.toModsElement(root)
		namePart = mods.NamePart()
		namePart.value = row[11]
	

		namePart.toModsElement(name1Element)
		roleElement = mods.Role().toModsElement(name1Element)

		#role of the person
		if( row[12] ):
			roleTerm = mods.RoleTerm()
			roleTerm.authority = "marcrelator"
			roleTerm.type = "text"
			roleTerm.value = row[12]
			roleTerm.toModsElement(roleElement)



	#abstract information
	if( row[13] ):
		abstract = mods.Abstract()
		abstract.value = row[13]
		abstract.toModsElement(root)

	#geo location information
	if( row[14] ):
		geoLocationElement = mods.OriginInfo().toModsElement(root)
		placeElement = mods.Place().toModsElement(geoLocationElement)
		placeTerm = mods.PlaceTerm()
		placeTerm.type = "text"
		placeTerm.value = row[14]
		placeTerm.toModsElement(placeElement)

	#language information
	if( row[15] ):
		languageElement = mods.Language().toModsElement(root)
		languageTerm = mods.LanguageTerm()
		languageTerm.type = "text"
		languageTerm.value = row[15]
		languageTerm.toModsElement(languageElement)

	#related name (Letter recipient)
	if( row[16] ):
		relatedName = mods.Name().toModsElement(root)
		relatedNamePart = mods.NamePart()
		relatedNamePart.value = row[16]
	
		relatedNamePart.toModsElement(relatedName)
		roleElement2 = mods.Role().toModsElement(relatedName)

		if( row[17] ):
			roleTerm2 = mods.RoleTerm()
			roleTerm2.authority = "marcrelator"
			roleTerm2.type = "text"
			roleTerm2.value = row[17]
			roleTerm2.toModsElement(roleElement2)

	#genre information
	if( row[18] ):
		genre = mods.Genre()
		genre.authority = "gmgpc"
		genre.value = row[18]
		genre.toModsElement(root)

	#subject - topic information
	if( row[19] ):
		topicSubjectElement = mods.Subject().toModsElement(root)
		topic = mods.Topic()
		topic.value = row[19]
		topic.toModsElement(topicSubjectElement) 

	#subject - name information
	if( row[20] ):
		nameSubjectRootElement = mods.Subject().toModsElement(root)
		nameSubject = mods.Name()
		nameSubject.type = "personal"
		nameSubjectElement = nameSubject.toModsElement(nameSubjectRootElement)
		nameSubjectPart = mods.NamePart()
		nameSubjectPart.value = row[20]
		nameSubjectPart.toModsElement(nameSubjectElement)

	#subject - corporation name information
	if( row[21] ):
		corpSubjectRootElement = mods.Subject().toModsElement(root)
		corpSubject = mods.Name()
		corpSubject.type = "corporate"
		corpSubjectElement = corpSubject.toModsElement(corpSubjectRootElement)
		corpSubjectPart = mods.NamePart()
		corpSubjectPart.value = row[21]
		corpSubjectPart.toModsElement(corpSubjectElement)

	#subject geographic information
	if( row[22] ):
		geoSubjectRootElement = mods.Subject().toModsElement(root)
		geo = mods.Geographic()
		geo.value = row[22]
		geo.toModsElement(geoSubjectRootElement)


	# physical description/form
	if( row[23] or row[24] or row[25]):
		physicalDescriptionElement = mods.PhysicalDescription().toModsElement(root)
		
		if( row[23] ):
			form = mods.Form()
			form.authority = "marcform"
			form.value = row[23]
			form.toModsElement(physicalDescriptionElement)

		# media type e.g. image/tiff
		if( row[24] ):
			internetMediaType = mods.InternetMediaType()
			internetMediaType.value = row[24]
			internetMediaType.toModsElement(physicalDescriptionElement)
	
		if( row[25] ):

			pageStr = " pages"

			if(int(row[25]) <= 1) :
				pageStr = " page"

			#extent
			extent = mods.Extent()
			extent.value = row[25] + pageStr
			extent.toModsElement(physicalDescriptionElement)

	# note
	if( row[28] ):
		note = mods.Note()
		note.value = row[28]
		note.toModsElement(root)

	#type of resource
	if( row[29] ):
		typeOfResource = mods.TypeOfResource()
		typeOfResource.value = row[29]
		typeOfResource.toModsElement(root)

	#source and language of cataloging
	if( row[30] or row[31] ):
		recordInfoElement = mods.RecordInfo().toModsElement(root)
		#source information
		if( row[30] ):
			recordSource = mods.RecordContentSource()
			recordSource.value = row[30]
			recordSource.toModsElement(recordInfoElement)
		if( row[31] ):
			langOfCatElement = mods.LanguageOfCataloging().toModsElement(recordInfoElement)
			recordLangauge = mods.LanguageTerm()
			recordLangauge.value = row[31]
			recordLangauge.type = "code"
			recordLangauge.authority = "iso639-2b"
			recordLangauge.toModsElement(langOfCatElement)

	#rights access
	if( row[32] ):
		accessCondition = mods.AccessCondition()
		accessCondition.value = row[32]
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
			for x in range(0,33):
				print("row " + str(x) + " = " + row[x])
			print("*************  DONE - " + str(counter) + " *********************" )
			print("")

