from PIL import Image

import base64 #za enkodiranje slike
import sys #za zlib
import zlib #za zlib

#   https://www.codespeedy.com/convert-rgb-to-hex-color-code-in-python/
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
# print(rgb_to_hex((255, 255, 255)))


########################################################################################################
#   https://www.geeksforgeeks.org/python-convert-image-to-string-and-vice-versa/

# with open("C:\\Users\\Tron\\Desktop\\hilbert\\8x8_custom.png", "rb") as image2string:
#     converted_string = base64.b64encode(image2string.read())
# print(converted_string)
# print(len(converted_string))
  
# with open('encode.bin', "wb") as file:
#     file.write(converted_string)

# print(sys.getsizeof(converted_string))

# print(base64.b64decode(converted_string))
# KAKO VRATIT STRING U OBLIK U KOJEM JE PRIJE BIO
########################################################################################################


im = Image.open(r"C:\\Users\\Tron\\Desktop\\hilbert\\test1.jpg")
px = im.load()

#   https://www.geeksforgeeks.org/python-pil-getpixel-method/
# print(rgb_to_hex(px[3, 3]))
# print (im.getpixel(coordinate));


#po redovima i stupcima
convertedPic_rows = ""
convertedPic_col = ""
for i in range(im.height):
    for j in range(im.width):
        convertedPic_rows += rgb_to_hex(px[i, j])
        # convertedPic_col += rgb_to_hex(px[j, i])

# print(convertedPic_rows)
# print(convertedPic_col)

#hex to bin
# import binascii
# binary_string = binascii.unhexlify(convertedPic_rows)
# print(binary_string)
#encoding and decoding
# print("\n______________________________________________\n")
# gfg = base64.b16encode(binary_string)
# print(gfg)
# fgf = base64.b16decode(gfg, casefold=True)
# print("\n______________________________________________\n")
# print(fgf)
## kompresija texta u sliku, ali na nacin da slova idu samo do f tako da se ostala mogu iskoristiti za dekodiranje kompresije 

#zlib
print("Size of convertedPic_rows:   ")
print(sys.getsizeof(convertedPic_rows))
zlib_comp = zlib.compress(convertedPic_rows.encode())
#33 je razlika izmedu duljine i koliko bi zauzimala datoteka
print("\nSize of 8x8_custom.png:  " )
print(sys.getsizeof("C:\\Users\\Tron\\Desktop\\hilbert\\test1.jpg"))
# print("\nZlib comprasani zlib stringa: ")
# print(zlib_comp)
print("\nlen of compresanog zlib stringa: ")
print(len(zlib_comp))
print("\nSize of compresanog zlib stringa: ")
print(sys.getsizeof(zlib_comp))
# print("\ndekodirani string od zliba: ")
# print(zlib.decompress(zlib_comp).decode())