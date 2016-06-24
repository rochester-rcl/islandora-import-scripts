
import os
import logging
import datetime
import sys


#logging info
dateTimeInfo = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")


logger1 = logging.getLogger('1')
logger1.addHandler(logging.FileHandler("logs/aids_export_no_xml_file_" + dateTimeInfo + ".log"))
logger1.setLevel(logging.INFO)

logger2 = logging.getLogger('2')
logger2.addHandler(logging.FileHandler("logs/not_asset_file_" + dateTimeInfo + ".log"))
logger2.setLevel(logging.INFO)

logger3 = logging.getLogger('3')
logger3.addHandler(logging.FileHandler("logs/no_asset_file_found_" + dateTimeInfo + ".log"))
logger3.setLevel(logging.INFO)


class FileInfo:
	"""Holds basic file information """
	def __init__(self, name,  extension, path, size):
		self.name = name
		self.extension = extension
		self.path = path
		self.size = size
		self.asset = None


	def getFullPath(self):
		return os.path.join(self.path,(self.name + self.extension))

	def toString(self):
		return("name = " + self.name + " exension = " +  self.extension + " path = " +  self.path + " size = " + str(self.size))

	def toCsv(self):
		return(self.name + ", " + self.getFullPath() + ", " + str(self.size))

		

# #######################################################
# get a dictionary of xml files - this skips any file that
# does not have an .xml file extension
#
# 
#
# #######################################################
def getAssetFiles(assetDirectory, extensions, xmlFiles):
	for root, sub, files in os.walk(assetDirectory):
			for aFile in files:
				(baseFileName, ext) = os.path.splitext(aFile)
				fileSize = os.path.getsize(os.path.join(root,aFile))
				info = FileInfo(baseFileName, ext, root, fileSize)
				if(ext.lower() in extensions):
					if(baseFileName in xmlFiles):
						xmlFiles[baseFileName].asset = info
					else:
						logger1.info( info.toCsv() ) # file does not exist in xml file set
				else: 
					logger2.info(info.toCsv()) #file does not have correct extension

# #######################################################
# get a dictionary of xml files - this skips any file that
# does not have an .xml file extension
#
# 
#
# #######################################################
def getXmlFiles(xmlDirectory):
	fileList = {}
	for root, sub, files in os.walk(xmlDirectory):
			for aFile in files:
				(baseFileName, ext) = os.path.splitext(aFile)
				#we only want xml files
				if(ext ==  ".xml"):
					info = FileInfo(baseFileName, ext, root, 0)
					fileList[baseFileName] = info
				else: 
					print("skipping file " + aFile)
	return fileList

# #######################################################
# Processes the files int sets of a given size
#
# offset: offset in the list of xml files to start processing
# maxFilesToProcess: maximum number of files to process
# valid extensions: valid extensions that the asset files can have
# assetDirectorySet: set of asset directories where assets exist
# xmlFileDictionary: dictionary of xml files - base file 
#                    name should match the base asset file name
# #######################################################
def processSets(offset, maxFilesToProcess, validExtensions, assetDirectorySet, xmlFileDictionary):
	if(not offset):
		offset = 0

    
	for directory in assetDirectorySet:
		getAssetFiles(directory, validExtensions, xmlFileDictionary)

	processed = 0
	assetMissingCounter = 0
	total = 0

	xmlWithAsset = []
	for key, fileInfo in xmlFileDictionary.items():
		total = total + 1
		if( fileInfo.asset == None): 
			logger2.info((fileInfo.getFullPath())) #no asset file foound
			assetMissingCounter = assetMissingCounter + 1
		else:
			xmlWithAsset.append(fileInfo) #add the asset to list
			processed = processed + 1
	print("processed = " + str(processed) + " assetMissingCounter = " + str(assetMissingCounter) + " total = " + str(total))  

	#sort the list
	sortedWithAsset = sorted(xmlWithAsset, key=lambda data:data.asset.size)

	for data in sortedWithAsset:
		print( "file ")




	#extensions = ','.join(validExtensions)
	#print("process sets max files to proces = " + maxFilesToProcess + " offset = " + 
	#	str(offset) + " extensions = " + extensions)

############## Main program ####################
maxFilesToProcess = input("Please enter maximum number of files to process enter to process all: ")
offset = input("Please enter the offset position (inclusive) press enter to start from the beginning: ")
validExtensions = input("Please enter a comma seperated list of extensions e.g. tif, tiff: ")



xmlDirectory = input("Please enter the top directory where all the xml files exist: ")
if( not os.path.isdir(xmlDirectory) ):
	print("Directory " + xmlDirectory + " does not exist or is not a directory")
	sys.exit()
else:
	print("Directory found " + xmlDirectory) 

xmlFileDictionary = getXmlFiles(xmlDirectory)

numXmlFiles = len(xmlFileDictionary)
print("found " + str(numXmlFiles) + " xml files")

if( numXmlFiles <= 0 ):
	print("ERROR: no xml files found " )
	sys.exit()

assetDirectories = []

numDirectories = int(input("Please enter the total number of asset directories: "))

for n in range(0,numDirectories):
	assetDirectory = input("Please enter the " + str(n + 1) + " directory where all the assets exist: ")

	if( not os.path.isdir(assetDirectory) ):
		print("Directory " + assetDirectory + " does not exist or is not a directory")
		sys.exit()
	else:
		print("Directory found " + assetDirectory) 
		assetDirectories.append(assetDirectory)

#convert to set to gaurantee uniqueness
assetDirectorySet = set(assetDirectories)

for aDirectory in assetDirectorySet : 
	print("Set directory = " + aDirectory)



#split the extensions
myExtensions = validExtensions.split(",")
extLength = len(myExtensions) 
if( extLength == 0 ):
	print("One or more extensions must be listed")
	sys.exit()

for index in range(0 , extLength):
	print("altering value " + myExtensions[index] + " at index " + str(index))
	myExtensions[index] = "." + myExtensions[index].strip().lower()



processSets(offset, maxFilesToProcess, myExtensions, assetDirectorySet, xmlFileDictionary)