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
    # default format - no leading zeros
    pageFormat = "{0:01d}"

    if (pages > 9 and pages < 99):
        # one leading zero
        pageFormat = "{0:02d}"
    elif (pages > 99 and pages < 999):
        # two leading zeros
        pageFormat = "{0:03d}"
    elif (pages > 999 and pages < 9999):
        # three leading zeros
        pageFormat = "{0:04d}"

    for page in range(1, pages):
        pageName = pageFormat.format(page)
        # create the padding format for source file
        sourceFilePaddFormat = "{0:0" + sourceFilePadd + "d}"
        # source file name
        filename = baseFilename + "_" + sourceFilePaddFormat.format(page) + ".tif"

        sourceFile = find(filename, baseDirectory)
        if (not os.path.isfile(sourceFile)):
            print("Could not find file " + sourceFile)
            sys.exit()
        else:
            pageDir = os.path.join(bookDir, pageName)
            destFile = os.path.join(pageDir, "OBJ.tif")
            print("source  = " + sourceFile + " dest = " + destFile)
            print("creating directory " + pageDir)
            os.mkdir(pageDir)
            shutil.copy(sourceFile, destFile)


# ##################################
# Add a pdf file to the directory
# ##################################
def addPdf(pdfDirectory, baseFilename, bookDir, sourceFilePaddLevel):
    # create the padding format for source file
    sourceFilePaddFormat = "{0:0" + sourceFilePadd + "d}"
    # source file name
    filename = baseFilename + ".pdf"
    sourceFile = find(filename, pdfDirectory)
    if (not os.path.isfile(sourceFile)):
        print("Could not find file " + filename)
        sys.exit()
    else:
        destFile = os.path.join(bookDir, "PDF")
        shutil.copy(sourceFile, destFile)
        print("source  = " + sourceFile + " dest = " + destFile)


# ##################################
# Create the file structure for a book in islandora
# ##################################
def createFileStructure(counter, row, baseDirectory, outputDirectory, sourceFilePaddLevel):
    # base file name
    baseFilename = row[31]
    # off by one so increase so it works correctly
    pages = int(row[30]) + 1
    print("filename = " + baseFilename)
    bookDir = os.path.join(outputDirectory, str(counter))
    print("creating directory " + bookDir)
    os.mkdir(bookDir)
    xmlFile = os.path.join(bookDir, "MODS" + ".xml")
    xmlrow.create_xml_file(row, xmlFile)
    createPageStructure(pages, baseDirectory, baseFilename, bookDir, sourceFilePaddLevel)
    return bookDir


# ########################################
# Main Program
# ########################################

# get the csv file input
aFile = input("Please enter csv file name: ")
if (not os.path.isfile(aFile)):
    print("Could not find file " + aFile)
    sys.exit()
else:
    print("found file ")

# check for source file padd level
paddLevel = 1
sourceFilePadd = input(
    "Please indicate source file page name padd level default is 1 meaning no 0's in front of page: ")
if (sourceFilePadd):
    paddLevel = int(sourceFilePadd)

# base directory of files to import
baseDirectory = input("Please enter directory of files to import: ")
if (not os.path.isdir(baseDirectory)):
    print("Directory " + baseDirectory + " does not exist or is not a directory")
    sys.exit()
else:
    print("Directory found " + baseDirectory)

hasPdfFiles = input("Are there seperate PDF files to import (Yes/No) default is No: ")
if hasPdfFiles.lower() == "yes":
    # base directory of files to import
    pdfDirectory = input("Please enter PDF directory of files to import: ")
    if not os.path.isdir(pdfDirectory):
        print("Directory " + pdfDirectory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("PDF directory found " + pdfDirectory)

# output directory for processing
outputDirectory = input("Please enter output directory: ")
if (not os.path.isdir(outputDirectory)):
    print("Directory " + outputDirectory + " does not exist or is not a directory")
    sys.exit()
else:
    print("Directory found " + outputDirectory)

# open the csv and start iterating through the rows
with open(aFile, 'r') as csvfile:
    fileReader = csv.reader(csvfile)
    counter = 1
    for row in fileReader:
        if (row[30]):
            pages = int(row[30])
            if (pages > 0):
                print("processing " + str(pages) + " pages")
                bookDir = createFileStructure(counter, row, baseDirectory, outputDirectory, paddLevel)
                if (hasPdfFiles):
                    print("adding pdf file ")
                    baseFilename = row[31]
                    addPdf(pdfDirectory, baseFilename, bookDir, paddLevel)
        else:
            print("Skipping row " + str(counter) + " pages found were " + row[30])
        counter += 1
