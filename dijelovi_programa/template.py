class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        tocke = []
        tocke.append([sr,sc])
        print(tocke)
        color = image[sr,sc]
        while tocke:
            newPositions(tocke, image)




def newPositions(tocke, image, color):
    x = tocke[0][0]
    y = tocke[0][1]
    niz = []
    if x == 0:
        niz.append(1)
    if y == len(image[[]]) - 1
    if x == len(image[]) - 1
        niz.append(3)
    if y== 0: niz. append(4)

