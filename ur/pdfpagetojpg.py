
import subprocess
from wand.image import Image

def convert_pdf_page(sourcePdf,  baseWidth, destination, pageNum = 0, quality = 60, colorspace="RGB", dpi = 72):
    

    # create format of  "DRIVE:\\dir1\\dir2\\file.pdf[pageNumber]"
    with Image(filename=sourcePdf + "[" + str(pageNum) + "]") as img:
       
        command = ["convert",
        sourcePdf + "[" + str(pageNum) + "]", 
        "-quality", 
        str(quality), 
        "-resize", 
        "{}x".format(baseWidth), 
        "-colorspace", 
        colorspace, 
        "-flatten", 
        "-set",
        "units",
        "PixelsPerInch",
        "-density", 
        str(dpi),
        destination, 
       ]

        #run the command
        print("command = " + ' '.join(command))
        subprocess.run(command, shell=True)

def main():
    convert_pdf_page(sourcePdf = "F:\\test\\1981_APRIL.pdf", 
        baseWidth = 400, 
        quality = 60,
        destination ="F:\\test\\1981_APRIL.jpg" )

if __name__ == '__main__':
    main()
