from PIL import Image
import gzip
import time
import os


############################################################################################################################

####### Kod sa https://www.geeksforgeeks.org/how-to-manipulate-the-pixel-values-of-an-image-using-python/
####### RADIIIIIII

###############################     HILBERT PATTERN     ############################################# 
# 0   1  14   15
# 3   2  13   12
# 4   7   8   11
# 5   6   9   10

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

def last2bits(x):
    return x & 3


def hildex2xy(index, N):
    positions = [[0,0], #     0,0 ---- 1,0
                [1,0],  #           /
                [0,1],  #         /
                [1,1]]  #     0,1 ---- 1,1 
    tmp = positions[last2bits(index)]
    index = (index >> 2)
    x = tmp[0]
    y = tmp[1]
    n=4
    while n <= N:
        n2 = n/2
        if last2bits(index) == 1:
            x = x + n2
            y = y
        elif last2bits(index) == 2: 
            x = x 
            y = y + n2
        elif last2bits(index) == 3:  
            y = y + n2
            x = x + n2
        index = index >> 2
        n = n*2
    return [x,y]


def hex_to_rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

start = time.time()
with gzip.open('C:\\Users\\Tron\\Desktop\\hilbert\\gzip_z.txt.gz', 'rb') as f:
    file_content = f.read()
file_content = file_content.decode()
N = int((len(file_content)/6)**0.5)
print("duzina slike je = ", N)

input = Image.new(mode="RGB",size=(N, N),
                        color="blue")
input.save("input", format="png")
pixel_map = input.load()

i=0
ocitanje = 0
# ((N*(N/1.28))):
# ((N*(N/2))):
# ((N*(N/6))):
# ((N*(N/12))):
while i < ((N*(N/2))):
    curr = hildex2xy(i,N)
    pixel_map[curr[0],curr[1]] = hex_to_rgb(file_content[ocitanje:ocitanje+6])
    file_content[ocitanje:ocitanje+6]
    i+=1
    ocitanje+=6

end = time.time()
current = end - start
print("Vrijeme za hilberta:\t", round(current,4), "s")
input.save("C:\\Users\\Tron\\Desktop\\hilbert\\testiranje_opt.png",optimize=True) #compress lvl 9 