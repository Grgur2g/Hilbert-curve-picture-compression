from PIL import Image

import os
import time

import gzip
import py7zr
import bz2


putanja="C:\\Users\\Tron\\Desktop\\hilbert"
im = Image.open(r""+putanja+"\\pics\\boat.png")
print("\nOriginalna velicina slike: ",round((os.path.getsize(putanja+'\\pics\\boat.png')/1024),4),"KB")
slika_size = os.path.getsize(putanja+'\\pics\\boat.png')
rgb_im = im.convert('RGB')
rgb_im.save(putanja+"\\boat_remake.png",optimize = True)
print("Nova velicina slike: ",round((os.path.getsize(putanja+'\\boat_remake.png')/1024),4),"KB\n")