# # # #http://graphics.stanford.edu/~seander/bithacks.html
# # # #https://stackoverflow.com/questions/12157685/z-order-curve-coordinates
# def calcZ(xPos,yPos):
#     masks = [0x55555555, 0x33333333, 0x0F0F0F0F, 0x00FF00FF]
#     shifts = [1, 2, 4, 8]
#     x = xPos
#     y = yPos

#     x = (x | (x << shifts[3])) & masks[3]
#     x = (x | (x << shifts[2])) & masks[2]
#     x = (x | (x << shifts[1])) & masks[1]
#     x = (x | (x << shifts[0])) & masks[0]

#     y = (y | (y << shifts[3])) & masks[3]
#     y = (y | (y << shifts[2])) & masks[2]
#     y = (y | (y << shifts[1])) & masks[1]
#     y = (y | (y << shifts[0])) & masks[0]

#     rez = x | (y << 1)
#     return rez

import time

def last2bits(x):
    return x & 3


def ztoxy(index, N):
    # Prvo se određuju pozicije točke za N = 2
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



# 

start = time.time()
N = 8
i=0
while i < N*N:
    print(ztoxy(i, N))
    ztoxy(i, N)
    i+=1

end =time.time()
current = end-start
print(current)

# N = 1024
# nizx= []
# nizy = []
# nizx, nizy = moserDeBruijn(N,nizx,nizy)

#https://www.wikiwand.com/en/Moser–de_Bruijn_sequence



# def gen(n):
 
#     # S(0) = 0
#     if n == 0:
#         return 0
 
#     # S(1) = 1
#     elif n ==1:
#         return 1
 
#     # S(2 * n) = 4 * S(n)
#     elif n % 2 ==0:
#         return 4 * gen(n // 2)
 
#     # S(2 * n + 1) = 4 * S(n) + 1
#     elif n % 2 == 1:
#         return 4 * gen(n // 2) +1
 
# # Generating the first 'n' terms
# # of Moser-de Bruijn Sequence
# def moserDeBruijn(n, nizx, nizy):
#     for i in range(n):
#         # print(gen(i), end = " ")
#         tmp = gen(i)
#         nizy.append(tmp)
#         nizx.append(tmp*2)
#     return nizx, nizy
 
# # Driver Program


