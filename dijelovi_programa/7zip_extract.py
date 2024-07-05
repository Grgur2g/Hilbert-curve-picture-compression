from sys import getsizeof
from PIL import Image

import os
import time

import gzip
import py7zr
import bz2

# with py7zr.SevenZipFile('C:\\Users\\Tron\\Desktop\\hilbert\\7z_hilberto.7z', mode='r') as f:
#     # file_content = f.read()
#     f.extractall()
# # f.close()
# print(f)

archive = py7zr.SevenZipFile('C:\\Users\\Tron\\Desktop\\hilbert\\7z_hilberto.7z', mode='r')
archive.extractall(path="'C:\\Users\\Tron\\Desktop\\hilbert\\tmp.txt'")
archive.close()


