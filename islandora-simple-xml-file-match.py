import os, shutil
import glob, zipfile
import re
import pprint
from xml.etree.ElementTree import ElementTree
from collections import OrderedDict
from operator import itemgetter
import logging
import datetime

dateTimeInfo = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
loggingName = "aids_export" + dateTimeInfo + ".log"

logging.basicConfig(filename=loggingName,level=logging.INFO)

itemDirectory = "J:\\"
zipOutDir = "I:\\aids-meta-zip-out\\"
xmlOutputDir = "G:\\aids-drupal-xml\\"

fileMatch = "AP[0-9]+\.tif"


# pull list of SORTED item IDs from folder where XML files are stored
# (assumes Jeff will create one XML file / item and place them in a directory)
def getFileList(itemDirectory, extension):
    fileList = {}
    for root, sub, files in os.walk(itemDirectory):
            for item in files:
                if (re.match(fileMatch, item)):
                    print("adding item " + item)
                    myFileSize = os.path.getsize(os.path.join(root,item)) 
                    fileList[item] = myFileSize
                else: 
                    logging.info("Skipping file " + item + " name pattern did not match")
    itemIdList = {}
    for fileNameKey, fileSize in fileList.items():
        print("checking file " + fileNameKey)
        if fileNameKey.find(extension) != -1 :
            print("Adding found file " + fileNameKey + " of size " + str(fileSize))
            itemIdList[fileNameKey.split('.')[0]] = fileSize
        
    
    # sorted smallest to largest
    sortedDict =  OrderedDict(sorted(itemIdList.items(), key=itemgetter(1)))
    return sortedDict;


# walk through file tree, find all items matching an item ID, return list of files with paths  
def findMatchingItems(idStr, itemDirectoryStr):
    matchingItems = []
    for root, dirs, files in os.walk(itemDirectoryStr):
        for item in files:
            if (re.match(idStr + "\.", item)):
                matchingItems.append(os.path.join(root,item))
    return matchingItems;

#get the list of files that can be added to the zip
#if the data cannot be found it is logged
def getZipableFileSet(idList):
    print("create zipable file set called")
    filesToAdd = []    

    for id in idList:
        myFiles = findMatchingItems(id, itemDirectory)
        print("adding id " + id + " to current set" )
            
        if len(myFiles) == 1:
            fileName = id + ".xml"
            xmlFile = os.path.join(xmlOutputDir, fileName)
            if( os.path.isfile(xmlFile) ):
                filesToAdd.append(xmlFile)
                filesToAdd.append(myFiles[0])
                fileName = id + ".xml"
            else:
                 logging.info("skipping file  " +  id + " no xml file found")
            
        else:
            logging.info("Bad files had len of " + str(len(myFiles))  + " for id " +  id)

    print("done prcessing zip set")
    return filesToAdd 

#zip up the list of files into a zip archive
def createZipSet(files, zipFileName):
    print("create zip set called " + zipFileName)
    
    with zipfile.ZipFile(zipFileName, 'w', allowZip64=True) as myzip:
        for aFile in files:
            print("adding file " + os.path.basename(aFile))
            myzip.write(aFile, os.path.basename(aFile))

# generator that creates lists chunked up into a given size
def createListSets(list, maxSize):
    """ Yield successive max-sized chunks from l.
    """
    for i in range(0, len(list), maxSize):
        yield list[i:i+maxSize]


def processSets(offset, maxFilesToProcess):
    fileIdList = getFileList(itemDirectory, "tif")
    setSize = len(fileIdList)
    if(not maxFilesToProcess):
        maxFilesToProcess = setSize + 1

    if(not offset):
        offset = 0

    offset = int(offset)
#    maxFilesPerZip = int(maxFilesPerZip)
    maxFilesToProcess = int(maxFilesToProcess)
    setSize = int(setSize)


#    print ("Max files per zip file = " + str(maxFilesPerZip))
    print ("Max files to process = " + str(maxFilesToProcess))
    print ("Offset = " + str(offset))

    counter = 1
    totalBytes = 0
    fileSet = []
    startCount = 1
    for fileName, fileSize in fileIdList.items():
        if( (counter >= offset) and (counter <= maxFilesToProcess) ) :
            print("counter = " + str(counter) + " processing file " + fileName + " with size " + str(fileSize))
            nextFile = fileName
            if( (totalBytes + fileSize) < 2000000000):
                print("file size " + str(totalBytes + fileSize) + " less than 2Gb")
                totalBytes = totalBytes + fileSize
                fileSet.append(fileName)
                counter = counter + 1
            else:
                print("file size " + str(totalBytes + fileSize) + "  Larger than 2Gb adding file " + fileName + " to next set")
                zipFileSet = getZipableFileSet(fileSet)
                createZipSet(zipFileSet, zipOutDir +"aep_" + str(startCount) + "_to_" + str(counter) + ".zip")
                print("creating file set " + zipOutDir +"aep_" + str(startCount) + "_to_" + str(counter) + ".zip size = " + str(totalBytes))
                
                totalBytes = fileSize
                fileSet = [] 
                fileSet.append(fileName)
                counter = counter + 1
                startCount = counter
                print("resetting startCount " + str(startCount) + "offset = " + str(offset) + "")

    if(len(fileSet) > 0):
        zipFileSet = getZipableFileSet(fileSet)
        createZipSet(zipFileSet, zipOutDir +"aep_" + str(startCount) + "_to_" + str(counter - 1) + ".zip")
        print("creating file set " + zipOutDir + "aep_" + str(startCount) + "_to_" + str(counter -1) + ".zip size = " + str(totalBytes))




# maxFilesPerZip = input("Please enter maximum number of files per zip file: ")
maxFilesToProcess = input("Please enter maximum number of files to process enter to process all: ")
offset = input("Please enter the offset position (inclusive) press enter to start from the beginning: ")


processSets(offset, maxFilesToProcess)
