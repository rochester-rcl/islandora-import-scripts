import os
import csv
from PyPDF2 import PdfFileReader

month_dict = {'january': '01', 
	'february': '02', 
	'march': '03', 
	'april' : '04',
	'may': '05',
	'june': '06',
	'july': '07',
	'august': '08',
	'september': '09',
	'october' : '10',
	'november' : '11', 
	'december' : '12'}


# ##################################
# find first file with the specified name
# in the base path - walks the directory tree
# ##################################
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

# ##################################
# find first file with the specified name
# in the base path - walks the directory tree
# ##################################
def get_all_files(path):
	myFiles = []
	for root, dirs, files in os.walk(path):
		myFiles.extend(files)
	
	return myFiles

def get_rows(all_files, path):

	all_rows = []
	#create a list of lists
	counter = 1
	for a_file in all_files:
		row = [None] * 37
		# job number
		row[0] = None

		# location
		row[1] = 'University of Rochester River Campus Libraries, Department of Rare Books, Special Collections and Preservation'

		# call number
		row[2] = 'HQ76.5 .E4'

		# box folder number
		row[3] = None

		# folder title
		row[4] = None

		# object title
		row[5] = 'Empty Closet, no. ' + str(counter)

		# collection title
		row[6] = 'Empty Closet'

		# series title
		row[7] = None

		# item date
		row[8] = get_date_info(a_file)

		# item date type
		row[9] = 'exact'

		# item date (second)
		row[10] = None

		# item date type (if second date needed)
		row[11] = None

		# Author name
		row[12] = 'Empty Closet Collective'

		# Author name type
		row[13] = 'corporate'

		# Author role
		row[14] = 'Creator'

		# related name (e.g., Letter recipient)
		row[15] = 'Gay Alliance of the Genesee Valley'

		# Related name type
		row[16] = 'corporate'

		# Related name role
		row[17] = 'Creator'

		# Description of resource
		row[18] = 'Empty Closet is one of the oldest continually published LGBT newspapers in the United States, and the oldest LGBT newspaper in New York State. Empty Closet covers local, state, national, and international news, as well as issues pertaining to the LGBT community. It was begun at the University of Rochester by Bob Osborn and Larry Fine, the founders of the UR student group, Rochester Gay Liberation Front, and later transferred to the Gay Alliance of the Genesee Valley (GAGV).'

		# publisher
		row[19] = 'Empty Closet Collective'

		# Geo location (Place of publication)
		row[20] = 'Rochester, N.Y.'

		#Language
		row[21] = 'English'

		#Genre
		row[22] = 'Newspapers'

		#subject
		row[23] = 'Homosexuality'

		#subject type
		row[24] = 'topic'

		#subject
		row[25] = None

		# subject type
		row[26] = None

		# Notes
		row[27] = None

		#Form
		row[28] = 'electronic'

		# media type
		row[29] = 'application/pdf'

		#material type
		row[30] = 'text'
		
		#get number of pages
		full_file = find(a_file, path)
		print(full_file)
		pages = 0

		if os.path.isfile(full_file):
			try:
				pdf = PdfFileReader(open(full_file,'rb'))
				pages = pdf.getNumPages()
			except:
				print("pages could not be found for " + full_file + "setting pages to 0")
		else:
			print("could not find file " + full_file)

		#num pages
		row[31] = str(pages)

		#num files
		row[32] = 1

		#base file name
		row[33] = a_file

		# source
		row[34] = 'University of Rochester, River Campus Libraries'

		# language of cataloging
		row[35] = 'eng'

		row[36] = 'For reproduction and permission information, see http://www.gayalliance.org/'


		all_rows.append(row)
		counter = counter + 1
	return all_rows

def get_date_info(name):
	parts = name.split('_')
	print(parts)
	year = '00'
	month = '00'
	if(len(parts) > 1):
		year = parts[0]

		month_parts = parts[1].split('.')
		if(len(month_parts) > 0):
			month = month_parts[0]
	return year + '-' + month_dict.get(month.lower(), '00')



def create_csv(rows):
	with open('ec_closet.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(rows)


def main():

	 # base directory of files to import
    base_directory = input("Please enter directory where files are located: ")
    if not os.path.isdir(base_directory):
        print("Directory " + base_directory + " does not exist or is not a directory")
        sys.exit()
    else:
        print("Directory found " + base_directory)

    all_files = get_all_files(base_directory)
    print("num files " + str(len(all_files)))
    for aFile in all_files:
    	print(aFile)

    create_csv(get_rows(all_files, base_directory))

if __name__ == '__main__':
    main()
