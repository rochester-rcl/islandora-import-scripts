
#work in prgress - This creates a skelatal mods file for the givne set of files

templateFile = "C:\\python-scripts\\xml-file-output\\aids_skeletalmods.xml"

def createXmlFiles(idList):
    print("create xml file list")
    for id in idList:
        #print("processing id " + id )
        tree = ElementTree()
        tree.parse(templateFile)
        root = tree.getroot()
        nameElement = tree.find('titleInfo/title')
        nameElement.text = id
        apElement = tree.find('identifier')
        apElement.text = id
        root.attrib = {"xmlns:xlink":"http://www.w3.org/1999/xlink", 
            "xmlns:xsi":"http://www.w3.org/2001/XMLSchema-instance",
            "xmlns":"http://www.loc.gov/mods/v3",
            "version":"3.5",
            "xsi:schemaLocation":"http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd"}
        #print("writing file " + xmlOutputDir + id + ".xml")
        tree.write(xmlOutputDir + id + ".xml")


def createXmlFiles(idList):
    print("create xml file list")
    for id in idList:
        #print("processing id " + id )
        tree = ElementTree()
        tree.parse(templateFile)
        root = tree.getroot()
        nameElement = tree.find('titleInfo/title')
        nameElement.text = id
        apElement = tree.find('identifier')
        apElement.text = id
        root.attrib = {"xmlns:xlink":"http://www.w3.org/1999/xlink", 
            "xmlns:xsi":"http://www.w3.org/2001/XMLSchema-instance",
            "xmlns":"http://www.loc.gov/mods/v3",
            "version":"3.5",
            "xsi:schemaLocation":"http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd"}
        #print("writing file " + xmlOutputDir + id + ".xml")
        tree.write(xmlOutputDir + id + ".xml")

def processSets(offset, maxFilesToProcess):
    fileIdList = getFileList(itemDirectory, "tif")
    setSize = len(fileIdList)
    if(not maxFilesToProcess):
        maxFilesToProcess = setSize + 1

    if(not offset):
        offset = 0

    offset = int(offset)
    maxFilesToProcess = int(maxFilesToProcess)
    setSize = int(setSize)


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
            fileSet.append(fileName)
            counter = counter + 1

    if(len(fileSet) > 0):
        createXmlFiles(fileSet)




# maxFilesPerZip = input("Please enter maximum number of files per zip file: ")
maxFilesToProcess = input("Please enter maximum number of files to process enter to process all: ")
offset = input("Please enter the offset position (inclusive) press enter to start from the beginning: ")


processSets(offset, maxFilesToProcess)
