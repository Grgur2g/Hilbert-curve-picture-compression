def last2bits(x):
    return x & 3

# print(last2bits(7))

def hildex2xy(index, N):
    # Prvo se određuju pozicije točke za N = 2
    positions = [[0,0], #
                [0,1],  #
                [1,1],  #
                [1,0]]  #
    tmp = positions[last2bits(index)]
    index = (index >> 2)    #shiftanje u sljedeći kvadrant
    x = tmp[0]
    y = tmp[1]
    n = 4
    while n <= N:
        n2 = n/2

        if last2bits(index) == 0: #donji lijevi kvadrant
            old_x = x
            x = y
            y = old_x
        elif last2bits(index) == 1: #gornji lijevi kvadrant
            x = x
            y = y + n2
        elif last2bits(index) == 2: #gornji desni kvadrant
            x = x + n2
            y = y + n2
        else: #donji desni kvadrant last2bits(index) == 3:
            old_y = y
            y = (n2-1) - x
            x = (n2-1) - old_y
            x = x + n2
        index = index >> 2
        n = n*2
    return [x,y]


#MAIN
N = 8
prev = [0,0]

i=0
while i < N*N:
    curr = hildex2xy(i,N)
    print(curr)
    prev = curr
    i+=1
