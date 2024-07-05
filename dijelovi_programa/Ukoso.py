from PIL import Image

import os
import time

import gzip
import py7zr
import bz2

###############################     HILBERT PATTERN     ############################################# 
# 0   1  14   15
# 3   2  13   12
# 4   7   8   11
# 5   6   9   10

def hex_to_rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


putanja="C:\\Users\\Tron\\Desktop\\hilbert"
im = Image.open(r""+putanja+"\\pics\\nxm.png")
print("\nOriginalna velicina slike: ",round((os.path.getsize(putanja+'\\pics\\nxm.png')/1024),4),"KB\n")
slika_size = os.path.getsize(putanja+'\\pics\\nxm.png')
N = im.width
M = im.height
rgb_im = im.convert('RGB') #osigurava da svaki string ima samo rgb
px = rgb_im.load()
# px = im.load()


iterator = 0
i=0
j=0
string_diagonally = ""

start = time.time()

while (iterator < N*M ): 
    #kod za dolje
    if (j == 0 or j == N-1) and (i%2 == 0):
        string_diagonally += rgb_to_hex(px[i, j])
        i += 1
        iterator += 1

    #kod za potez u desno gore, prije iterator > 2N
    elif((j == 0) and (i%2 == 1)):
        while i > 0:
            string_diagonally += rgb_to_hex(px[i, j])
            i-=1
            j+=1
            iterator += 1

    elif (i==N-1 and j%2 == 0):
        while j < N-1:
            string_diagonally += rgb_to_hex(px[i, j])
            i-=1
            j+=1
            iterator += 1

    #kod za pomak u desno
    elif (i == 0 or i == N-1) and (j%2 == 1):
        
        string_diagonally += rgb_to_hex(px[i, j])
        j += 1
        iterator += 1


    #kod za pomak dolje lijevo
    elif (i == 0) and (j%2 == 0):
        while j > 0:
            string_diagonally += rgb_to_hex(px[i, j])
            i+=1
            j-=1 
            iterator += 1

    #kod za pomak dolje lijevo
    elif (j == N-1) and (i%2 == 1):
        while (i < N-1):
            string_diagonally += rgb_to_hex(px[i, j])
            j-=1
            i+=1
            iterator += 1

end = time.time()
current = end - start
print("Vrijeme za dijagnoalu:\t",round(current,4), "s")

diagonally_txt = open(putanja+"\\diagonally_pic.txt","w")
diagonally_txt.write(string_diagonally)
diagonally_txt.close()

def printaj(zip_name,current,string):
    zip_size = os.path.getsize(putanja+'\\'+zip_name)
    print(zip_name + " size: ", round((zip_size/1024),4),"KB\t\t", "for compression time of ",round(current,4), "s"," -> compression ratio: ", round(1 - (zip_size / len(string.encode())), 4), "\t\tcompression comparison: ",round(((zip_size - slika_size)/slika_size)*100,4),"%", " or ",round((zip_size - slika_size)/1024,4), "KB")


start = time.time()
with gzip.open(putanja+'\\gzip_diagonally.txt.gz', 'wb') as f:
    f.write(string_diagonally.encode())
end =time.time()
current = end-start
printaj("gzip_diagonally.txt.gz",current,string_diagonally)

start = time.time()
archive = py7zr.SevenZipFile(putanja+'\\7z_diagonally.7z', 'w')
archive.writeall(putanja+'\\diagonally_pic.txt', "diagonally_pic.txt")
archive.close()
end =time.time()
current = end-start
printaj("7z_diagonally.7z",current,string_diagonally)

start = time.time()
c = bz2.compress(string_diagonally.encode())
with bz2.open(putanja+"\\bz2_diagonally.bz2", "wb") as f:
    f.write(c)
end =time.time()
current = end-start
printaj("bz2_diagonally.bz2",current,string_diagonally)

print("_______________________________\n")



#######################################        DIAGONALLY      ###################################################
##################################################################################################################

start = time.time()
with gzip.open(putanja+'\\gzip_diagonally.txt.gz', 'rb') as f:
    file_content = f.read()
file_content = file_content.decode()
# N = int((len(file_content)/6)**0.5)


input = Image.new(mode="RGB",size=(N, M),
                        color="blue")
input.save("input", format="png")
pixel_map = input.load()
iterator = 0
i=0
j=0
ocitanje = 0
while (iterator < N*M ): 
    #kod za dolje
    if (j == 0 or j == N-1) and (i%2 == 0):
        pixel_map[i,j] = hex_to_rgb(file_content[ocitanje:ocitanje+6])
        i += 1
        iterator += 1
        ocitanje += 6

    #kod za potez u desno gore, prije iterator > 2N
    elif((j == 0) and (i%2 == 1)):
        while i > 0:
            pixel_map[i,j] = hex_to_rgb(file_content[ocitanje:ocitanje+6])
            i-=1
            j+=1
            iterator += 1
            ocitanje += 6

    elif (i==N-1 and j%2 == 0):
        while j < N-1:
            pixel_map[i,j] = hex_to_rgb(file_content[ocitanje:ocitanje+6])
            i-=1
            j+=1
            iterator += 1
            ocitanje += 6

    #kod za pomak u desno
    elif (i == 0 or i == N-1) and (j%2 == 1):
        
        pixel_map[i,j] = hex_to_rgb(file_content[ocitanje:ocitanje+6])
        j += 1
        iterator += 1
        ocitanje += 6


    #kod za pomak dolje lijevo
    elif (i == 0) and (j%2 == 0):
        while j > 0:
            pixel_map[i,j] = hex_to_rgb(file_content[ocitanje:ocitanje+6])
            i+=1
            j-=1 
            iterator += 1
            ocitanje += 6

    #kod za pomak dolje lijevo
    elif (j == N-1) and (i%2 == 1):
        while (i < N-1):
            pixel_map[i,j] = hex_to_rgb(file_content[ocitanje:ocitanje+6])
            j-=1
            i+=1
            iterator += 1
            ocitanje += 6

input.save(putanja+"\\remake_diagonally.png",optimize=True) #compress lvl 9 
end = time.time()
current = end - start
print("Vrijeme za dijagonalu:\t", round(current,4), "s\t", "veličina rekreirane slike: ",round(os.path.getsize(putanja+'\\remake_diagonally.png')/1024,4), "KB")
