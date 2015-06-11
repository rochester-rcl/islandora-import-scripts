import ur.xmlrow as xmlrow
import os
import csv
import sys
import xml.etree.ElementTree as ET
import shutil

# ##################################
# find first file with the specified name 
# in the base path - walks the directory tree
# ##################################
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

# ##################################1
# Creates a folder for every page based on the file name - this is a
# requirement of islandora
# ##################################
def createPageStructure(pages, baseDirectory, baseFilename, bookDir, sourceFilePaddLevel):
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
		#create the padding format for source file
		sourceFilePaddFormat = "{0:0" + sourceFilePadd + "d}"
		#source file name
		filename = baseFilename + "_" + sourceFilePaddFormat.format(page) + ".tif"

		sourceFile = find(filename, baseDirectory)
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
def createFileStructure(counter, row, baseDirectory, outputDirectory, sourceFilePaddLevel):
	#base file name
	baseFilename = row[27]
	#off by one so increase so it works correctly
	pages = int(row[25]) + 1
	print("filename = " + baseFilename)
	bookDir = os.path.join(outputDirectory, str(counter))
	print("creating directory " + bookDir)
	os.mkdir(bookDir)
	xmlFile = os.path.join(bookDir, "MODS" + ".xml")
	xmlrow.createXmlFile(row, xmlFile)
	createPageStructure(pages, baseDirectory, baseFilename, bookDir, sourceFilePaddLevel)

	


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


#check for source file padd level
paddLevel = 1
sourceFilePadd = input("Please indicate source file page name padd level default is 1 meaning no 0's in front of page: ")
if(sourceFilePadd):
	paddLevel = int(sourceFilePadd)

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
				createFileStructure(counter, row, baseDirectory, outputDirectory, paddLevel)
		else:
			print ("Skipping row " + str(counter) + " pages found were " + row[25] )
		counter += 1
		
		

