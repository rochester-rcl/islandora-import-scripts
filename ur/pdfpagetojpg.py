
import subprocess
from wand.image import Image

def convert_pdf_page(sourcePdf,  baseheight, destination, pageNum = 0, quality = 75, colorspace="RGB"):
    # create format of  "DRIVE:\\dir1\\dir2\\file.pdf[pageNumber]"
    with Image(filename = sourcePdf + "[" + str(pageNum) + "]") as img:
       
        command = ["convert", 
        sourcePdf + "[" + str(pageNum) + "]", 
        "-quality", 
        str(quality), 
        "-resize", 
        "x{}".format(baseheight), 
        "-colorspace", 
        colorspace, 
        "-flatten", 
        destination]

        #run the command
        subprocess.run(command, shell=True)

def main():
    convert_pdf_page(sourcePdf = "F:\\ec-test\\junk\\2011_April.pdf", 
        baseheight = 400, 
        destination ="F:\\ec-test\\junk\\2011_April.jpg" )

if __name__ == '__main__':
    main()
