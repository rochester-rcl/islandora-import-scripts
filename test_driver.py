
import ur.xmlrow as xmlrow
import os
import csv
import sys
import xml.etree.ElementTree as ET





# ########################################
# Main Program for testing output
# ########################################

#get the csv file input
aFile = input("Please enter csv file name: ")
if( not os.path.isfile(aFile) ):
	print("Could not find file " + aFile)
	sys.exit()
else:
	print ("found file ")

print("testing csv file")
xmlrow.printCsvInfo(aFile)

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
				if( row[30] ):
					pages = int(row[30])
					if( pages > 0):
						print("processing " + str(pages) + " pages")
						xmlFile = os.path.join(outputDirectory, "MODS_" + str(counter) + ".xml")
						xmlrow.createXmlFile(row, xmlFile)			
				else:
					print ("Skipping row " + str(counter) + " pages found were " + row[30] )
				counter += 1


