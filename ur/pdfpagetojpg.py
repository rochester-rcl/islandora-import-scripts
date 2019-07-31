
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
        print("HELLO")
        print("command = " + ' '.join(command))
        subprocess.run(command, shell=True)

def convert_pdf_page2(sourcePdf,  baseWidth, destination, pageNum = 0, quality = 60, colorspace="rgb", dpi = 72):
    

    # create format of  "DRIVE:\\dir1\\dir2\\file.pdf[pageNumber]"
    with Image(filename=sourcePdf + "[" + str(pageNum) + "]") as img:
       img.compression_quality = quality
       img.alpha_channel = False
       img.resolution = (dpi,dpi)
       img.transform_colorspace(colorspace)
       img.transform(resize="{}x".format(baseWidth))
       img.save(filename=destination)
        

def main():
    convert_pdf_page2(sourcePdf = "/Users/nsarr/git-projects/campus-times-reports/output/0001/OBJ.pdf", 
        baseWidth = 400, 
        quality = 60,
        destination ="/Users/nsarr/git-projects/campus-times-reports/output/0002.jpg" )

if __name__ == '__main__':
    main()
