import os
from PIL import Image


dirPath = '\\nefilesrv\\perf$\\a.portugal\\Escritorio\\Clo APITEST\\GitHub\\APITEST\\flaskr\\logo_arcalis.jpg'
dirList = os.listdir(dirPath)
outPath = '\\nefilesrv\\perf$\\a.portugal\\Escritorio\\Clo APITEST\\GitHub\\APITEST\\flaskr\\logo_arcalis.jpg'

for (dirname, dirs, files) in os.walk(dirPath):
   for filename in files:
       if filename.endswith('.png'):
            print("Opening:"+filename)
            thefile = os.path.join(dirname,filename)
            im = Image.open(thefile)
            #im.load()

            width, height = im.size

            im_rgb = im.convert('RGB')

            for x in range(0, width):
                for y in range(0,height):
                    r, g, b = im_rgb.getpixel((x, y))
                    im_rgb.putpixel((x, y), (b, g, r))

            print("Saving:"+filename)
            #outfile, ext = os.path.splitext(infile)
            outfile = os.path.join(outPath,filename)
            im_rgb.save(outfile, "PNG")


print("Ding!")