import os
import re
import sys
import logging
from collections import OrderedDict
from operator import itemgetter
import csv
from PyPDF2 import PdfFileReader

# file name matching patterns
tur_file_match = "T_U_R_(.*)"
tur_file_dict = {}
tur_pub_name = "University Record"

ttnc_file_match = "T_T_N_C_(.*)" 
ttnc_file_dict = {}
ttnc_pub_name = "Tower Times News Comicle"

ttff_file_match = "T_T_F_F_(.*)"
ttff_file_dict = {}
ttff_pub_name = ""

tt_file_match = "T_T_(.*)"
tt_file_dict = {}
tt_pub_name = "Tower Times"

trc_file_match = "T_R_C_(.*)"
trc_file_dict = {}
trc_pub_name = "Rochester Campus"

tcw_file_match = "T_C_W_(.*)"
tcw_file_dict = {}
tcw_pub_name = "Cloister Window"

tcsm_file_match = "T_C_S_M_(.*)"
tcsm_file_dict = {}
tcsm_pub_name = "Campus Scampus Mirror"

tctr_file_match = "T_C_T_R_(.*)"
tctr_file_dict = {}
tctr_pub_name = "Campus The Rumpus"

tct_file_match = "T_C_T_(.*)"
tct_file_dict = {}
tct_pub_name = "Campus Times  1943"

ct_file_match = "C_T_(.*)"
ct_file_dict = {}
ct_pub_name = "Campus Times"

tc_file_match = "T_C_(.*)"
tc_file_dict = {}
tc_pub_name = "Campus"

cw_file_match = "C_W_(.*)"
cw_file_dict = {}
cw_pub_name = "Cloister Window"

tr_file_match = "T_R_(.*)"
tr_file_dict = {}
tr_pub_name = "Rumpus"

ts_file_match = "T_S_(.*)"
ts_file_dict = {}
ts_pub_name = "Scampus"

to_file_match = "T_O_(.*)"
to_file_dict = {}
to_pub_name = "Oister"


#date matching patterns
basic_date_match = "(\d+)_(\d+)_(\d+)"
year_month_match = "(\d+)_(\d+)"

monthDict = {'00': 'Unknown',
              '01': 'January',
              '02': 'February',
              '03': 'March',
              '04': 'April',
              '05': 'May',
              '06': 'June',
              '07': 'July',
              '08': 'August',
              '09': 'September',
              '10': 'October',
              '11': 'November',
              '12': 'December'}


# ########################################
# Get a count of pages in each pdf file
# ########################################
class PdfFileInfo:
    """Holds pdf file information"""

    def __init__(self):
        self.hasTiffs = True
        self.publication = ''
        self.value = ''
        self.month = ''
        self.year = ''
        self.day = ''
        self.date = ''

    def getTitle(self):
        self.parseDate()
        # Campus Times, January 15, 1955
        title = self.publication
        dateTitle = ""

        if(self.month):
            month = monthDict.get(self.month, 'Unknown')
            dateTitle =  month 

            if(self.day):
                dateTitle = dateTitle  + " " + str(self.day) + ","
            
            if(self.year):
                dateTitle = dateTitle + " " + str(self.year)
        elif(self.year):
            dateTitle = str(self.year)
        
        if(dateTitle):
            title = title + " (" + dateTitle + ")"

        print("Title = " + title)
        return title


    def getIsoDate(self):
        if (re.match(basic_date_match, self.date)):
            matchInfo = re.match(basic_date_match, self.date)
            #YYYY-MM-DD
            return matchInfo.group(1) + "-" + matchInfo.group(2) + "-" + matchInfo.group(3)
        elif(re.match(year_month_match, self.date)):
            matchInfo = re.match(year_month_match, self.date)
            #YYYY-MM
            return matchInfo.group(1) + "-" + matchInfo.group(2) 
        else:
            return self.date     

    # ########################################
    # Parse the date information and store it
    # ########################################
    def parseDate(self):
        
        if (re.match(basic_date_match, self.date)):
            matchInfo = re.match(basic_date_match, self.date)
            self.day = matchInfo.group(3)
            self.month = matchInfo.group(2)
            self.year =  matchInfo.group(1)
        elif(re.match(year_month_match, self.date)):
            matchInfo = re.match(year_month_match, self.date)
            self.month = matchInfo.group(2)
            self.year =  matchInfo.group(1)    
        else:
            print("match not found for " + self.date)   
       
# ########################################
# Get a count of pages in each pdf file
# ########################################
def getPdfPages(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
 
    return number_of_pages

# ##################################
# pull list of SORTED item IDs from folder where XML files are stored
# (assumes Jeff will create one XML file / item and place them in a directory)
# ##################################
def getFileList(itemDirectory, extension):
    fileList = {}
    for root, sub, files in os.walk(itemDirectory):
            for item in files:
                if (item.endswith(".pdf")):
                    #print("adding item " + item)
                    path =  os.path.join(root,item)
                    fileList[item] = path
                else:
                    logging.info("Skipping file " + item + " name pattern did not match")
    itemIdList = {}
    for fileNameKey, fileSize in fileList.items():
        # print("Adding found file " + fileNameKey + " of size " + str(fileSize))
        itemIdList[fileNameKey.split('.')[0]] = fileSize #get the id only no extension

    # sorted based on keys - use file name
    sortedDict =  OrderedDict(sorted(itemIdList.items(), key=itemgetter(0)))
    return sortedDict

# ########################################
# print out dictionary info
# ########################################
def printDict(dict):
    for key, info in dict.items():
        print(" key = " + key +  "title = " + info.getTitle() + " value = " + info.value + " date = " + info.date + " parsed = " + info.getIsoDate() )
       

# ########################################
# Create csv from dictionary
# ########################################
def createCsv(dict, csv_file, tiffDirectory):
    print("Creating csv " + csv_file)
    rows = []
    for key, info in dict.items():
        #print(" found key " + key + " and value " + value)
        numPages = getPdfPages(info.value)
        tiffCount = 0

        if(info.hasTiffs):
            tiffCount = numTiffs(tiffDirectory, key)
            #number of pages should match number of TIFF files
            countMatch = (numPages == tiffCount)
            if(numPages ==  tiffCount):
                print("num pages "  + str(numPages) + " equals " + str(tiffCount))
            else:
                print("num pages "  + str(numPages) + " NOT equals " + str(tiffCount))

        row = [None] * 8
        row[0] = key
        row[1] = info.getTitle()
        row[2] = numPages
        row[3] = info.hasTiffs
        row[4] = tiffCount
        row[5] = countMatch
        row[6] = info.getIsoDate()
        row[7] = info.value
        rows.append(row)
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Title","Pages", "has tiffs", "TIFFS", "Count Match", "Date", "Path"])
        writer.writerows(rows)

# ########################################
# determine if this pdf has diffs 
# ########################################
def numTiffs(tiffDirectory, key):
    numTiffs = 0
    path = os.path.join(tiffDirectory, key)
    print("Checking for tiffs for key " + key + "path = " + path)
    if os.path.isdir(path):
        numTiffs = len([name for name in os.listdir(path) if (os.path.isfile(os.path.join(path, name)) and name.endswith(".tif"))])
    print(numTiffs)
    return numTiffs

def getPdfs(processDirectory, hasTiffs):
    sortedDict = getFileList(processDirectory, 'pdf')
   
    for key, value in sortedDict.items():
        if (re.match(tur_file_match, key)):
            matchInfo = re.match(tur_file_match, key)
            pdfInfo = PdfFileInfo()
            pdfInfo.publication = tur_pub_name
            pdfInfo.hasTiffs = hasTiffs
            pdfInfo.value = value
            pdfInfo.date = matchInfo.group(1)
            tur_file_dict[key] = pdfInfo
            #print(matchInfo.group(1))
            #print(" found key " + key + " and value " + str(value))
        elif(re.match(tcw_file_match, key)):
            matchInfo = re.match(tcw_file_match, key)
            pdfInfo = PdfFileInfo()
            pdfInfo.publication = tcw_pub_name
            pdfInfo.hasTiffs = hasTiffs
            pdfInfo.value = value
            pdfInfo.date = matchInfo.group(1)
            tcw_file_dict[key] = pdfInfo
            #print(matchInfo.group(1))
            #print(" found key " + key + " and value " + str(value))
        elif(re.match(trc_file_match, key)):
            matchInfo = re.match(trc_file_match, key)
            pdfInfo = PdfFileInfo()
            pdfInfo.publication = trc_pub_name
            pdfInfo.hasTiffs = hasTiffs
            pdfInfo.value = value
            pdfInfo.date = matchInfo.group(1)
            trc_file_dict[key] = pdfInfo
            #print(matchInfo.group(1))
            #print(" found key " + key + " and value " + str(value))
        elif(re.match(tcsm_file_match, key)):
            matchInfo = re.match(tcsm_file_match, key)
            pdfInfo = PdfFileInfo()
            pdfInfo.publication = tcsm_pub_name
            pdfInfo.hasTiffs = hasTiffs
            pdfInfo.value = value
            pdfInfo.date = matchInfo.group(1)
            tcsm_file_dict[key] = pdfInfo
            #print(matchInfo.group(1))
            #print(" found key " + key + " and value " + str(value))
        elif(re.match(tctr_file_match, key)):
            matchInfo = re.match(tctr_file_match, key)
            pdfInfo = PdfFileInfo()
            pdfInfo.publication = tctr_pub_name
            pdfInfo.hasTiffs = hasTiffs
            pdfInfo.value = value
            pdfInfo.date = matchInfo.group(1)
            tctr_file_dict[key] = pdfInfo
            #print(matchInfo.group(1))
            #print(" found key " + key + " and value " + str(value))        
        elif(re.match(tct_file_match, key)):
            matchInfo = re.match(tct_file_match, key)
            pdfInfo = PdfFileInfo()
            pdfInfo.publication = tct_pub_name
            pdfInfo.hasTiffs = hasTiffs
            pdfInfo.value = value
            pdfInfo.date = matchInfo.group(1)
            tct_file_dict[key] = pdfInfo
            #print(matchInfo.group(1))
            #print(" found key " + key + " and value " + str(value))
        elif(re.match(ttnc_file_match, key)):
            matchInfo = re.match(ttnc_file_match, key)
            pdfInfo = PdfFileInfo()
            pdfInfo.publication = ttnc_pub_name
            pdfInfo.hasTiffs = hasTiffs
            pdfInfo.value = value
            pdfInfo.date = matchInfo.group(1)
            ttnc_file_dict[key] = pdfInfo
            #print(matchInfo.group(1))
            #print(" found key " + key + " and value " + str(value))     
        elif(re.match(ttff_file_match, key)):
            matchInfo = re.match(ttff_file_match, key)
            pdfInfo = PdfFileInfo()
            pdfInfo.publication = ttff_pub_name
            pdfInfo.hasTiffs = hasTiffs
            pdfInfo.value = value
            pdfInfo.date = matchInfo.group(1)
            ttff_file_dict[key] = pdfInfo
            #print(matchInfo.group(1))
            #print(" found key " + key + " and value " + str(value))         
        elif(re.match(tt_file_match, key)):
            matchInfo = re.match(tt_file_match, key)
            pdfInfo = PdfFileInfo()
            pdfInfo.publication = tt_pub_name
            pdfInfo.hasTiffs = hasTiffs
            pdfInfo.value = value
            pdfInfo.date = matchInfo.group(1)
            tt_file_dict[key] = pdfInfo
            #print(matchInfo.group(1))
            #print(" found key " + key + " and value " + str(value))
        elif(re.match(ct_file_match, key)):
            matchInfo = re.match(ct_file_match, key)
            pdfInfo = PdfFileInfo()
            pdfInfo.publication = ct_pub_name
            pdfInfo.hasTiffs = hasTiffs
            pdfInfo.value = value
            pdfInfo.date = matchInfo.group(1)
            ct_file_dict[key] = pdfInfo
            #print(matchInfo.group(1))
            #print(" found key " + key + " and value " + str(value))    
        # NOTE this one must be below the more exxplict TCW, TCSM, TCT match
        elif(re.match(tc_file_match, key)):
            matchInfo = re.match(tc_file_match, key)
            pdfInfo = PdfFileInfo()
            pdfInfo.publication = tc_pub_name
            pdfInfo.hasTiffs = hasTiffs
            pdfInfo.value = value
            pdfInfo.date = matchInfo.group(1)
            tc_file_dict[key] = pdfInfo
            #print(matchInfo.group(1))
            #print(" found key " + key + " and value " + str(value))    
        elif(re.match(cw_file_match, key)):
            matchInfo = re.match(cw_file_match, key)
            pdfInfo = PdfFileInfo()
            pdfInfo.publication = cw_pub_name
            pdfInfo.hasTiffs = hasTiffs
            pdfInfo.value = value
            pdfInfo.date = matchInfo.group(1)
            cw_file_dict[key] = pdfInfo
            #print(matchInfo.group(1))
            #print(" found key " + key + " and value " + str(value))
        elif(re.match(tr_file_match, key)):
            matchInfo = re.match(tr_file_match, key)
            pdfInfo = PdfFileInfo()
            pdfInfo.publication = tr_pub_name
            pdfInfo.hasTiffs = hasTiffs
            pdfInfo.value = value
            pdfInfo.date = matchInfo.group(1)
            tr_file_dict[key] = pdfInfo
            #print(matchInfo.group(1))
            #print(" found key " + key + " and value " + str(value))
        elif(re.match(ts_file_match, key)):
            matchInfo = re.match(ts_file_match, key)
            pdfInfo = PdfFileInfo()
            pdfInfo.publication = ts_pub_name
            pdfInfo.hasTiffs = hasTiffs
            pdfInfo.value = value
            pdfInfo.date = matchInfo.group(1)
            ts_file_dict[key] = pdfInfo
            #print(matchInfo.group(1))
            #print(" found key " + key + " and value " + str(value))
        elif(re.match(to_file_match, key)):
            matchInfo = re.match(to_file_match, key)
            pdfInfo = PdfFileInfo()
            pdfInfo.publication = to_pub_name
            pdfInfo.hasTiffs = hasTiffs
            pdfInfo.value = value
            pdfInfo.date = matchInfo.group(1)
            to_file_dict[key] = pdfInfo
            #print(matchInfo.group(1))
            #print(" found key " + key + " and value " + str(value))
        else:
            print("No match found for key" + key)
    return sortedDict

# ########################################
# Process all the files checking for 
# key matches
# ########################################
def processFiles(tiffDirectory):

    print("T_U_R_ = " + str(len(tur_file_dict)))
    print("T_T_F_N_ = " + str(len(ttff_file_dict)))
    print("T_T_N_C_ = " + str(len(ttnc_file_dict)))
    print("T_T_ = " + str(len(tt_file_dict)))
    print("T_R_C_ = " + str(len(trc_file_dict)))
    print("T_C_W_ = " + str(len(tcw_file_dict)))
    print("T_C_S_M_ = " + str(len(tcsm_file_dict)))
    print("T_C_T_R_ = " + str(len(tctr_file_dict)))
    print("T_C_T_ = " + str(len(tct_file_dict)))
    print("C_T_ = " + str(len(ct_file_dict)))
    print("T_C_ = " + str(len(tc_file_dict)))
    print("C_W_ = " + str(len(cw_file_dict)))
    print("T_R_ = " + str(len(tr_file_dict)))
    print("T_S_ = " + str(len(ts_file_dict)))
    print("T_O_ = " + str(len(to_file_dict)))

    total1 =  len(tur_file_dict) + len(tt_file_dict) + len(trc_file_dict) + len(tcw_file_dict) + len(tcsm_file_dict) + len(tctr_file_dict) + len(tct_file_dict) 
    total2 = len(ct_file_dict) + len(tc_file_dict) + len(cw_file_dict) + len(tr_file_dict) + len(ts_file_dict) + len(to_file_dict) + len(ttnc_file_dict) + len(ttff_file_dict)

    print("sum = " + str(total1 + total2))
    printDict(trc_file_dict)
    createCsv(tur_file_dict, "tur.csv", tiffDirectory)
    createCsv(ttff_file_dict, "ttff.csv", tiffDirectory)
    createCsv(ttnc_file_dict, "ttnc.csv", tiffDirectory)
    createCsv(tt_file_dict, "tt.csv", tiffDirectory)
    createCsv(trc_file_dict, "trc.csv", tiffDirectory)
    createCsv(tcw_file_dict, "tcw.csv", tiffDirectory)
    createCsv(tcsm_file_dict, "tcsm.csv", tiffDirectory)
    createCsv(tctr_file_dict, "tctr.csv", tiffDirectory)
    createCsv(tct_file_dict, "tct.csv", tiffDirectory)
    createCsv(ct_file_dict, "ct.csv", tiffDirectory)
    createCsv(tc_file_dict, "tc.csv", tiffDirectory)
    createCsv(cw_file_dict, "cw.csv", tiffDirectory)
    createCsv(tr_file_dict, "tr.csv", tiffDirectory)
    createCsv(ts_file_dict, "ts.csv", tiffDirectory)
    createCsv(to_file_dict, "to.csv", tiffDirectory)

# ########################################
# Main Program
# ########################################
def main():
    process_directory = input("Please enter PDF directory with tiffs to process: ")
    if not os.path.isdir(process_directory):
        print("Directory " + process_directory + " does not exist or is not a directory")
        sys.exit()
    
    print("Process directory found " + process_directory) 

    tiff_directory = input("Please enter tiff diectory: ")
    if not os.path.isdir(tiff_directory):
        print("Directory " + tiff_directory + " does not exist or is not a directory")
        sys.exit()
    
    print("Print directory found " + tiff_directory)
    
    no_tiff_process_directory = input("Please enter directory with PDF only files (NO TIFF files) to process: ")
    if not os.path.isdir(no_tiff_process_directory):
        print("Directory " + no_tiff_process_directory + " does not exist or is not a directory")
        sys.exit()
    
    
    
    getPdfs(process_directory, True)
    getPdfs(no_tiff_process_directory, False)
    # printDict(tur_file_dict)
    # printDict(ttff_file_dict)
    # printDict(ttnc_file_dict)
    # printDict(tt_file_dict)
    # printDict(trc_file_dict)
    # printDict(tcw_file_dict)
    # printDict(tcsm_file_dict)
    # printDict(tctr_file_dict)
    # printDict(tct_file_dict)
    # printDict(ct_file_dict)
    # printDict(tc_file_dict)
    # printDict(cw_file_dict)
    # printDict(tr_file_dict)
    # printDict(ts_file_dict)
    # printDict(to_file_dict)
    
    processFiles(tiff_directory)

if __name__ == '__main__':
    main()

 
