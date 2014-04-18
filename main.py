

#numObj = input("Enter the number of objects.. ")
#numAttr = input("Enter the number of attributes.. ")

def printMat(Mat):
    print("Print matrix\n")
    for x in range(0, len(Mat)):
        for y in range(0,  len(Mat[0])):
            print(Mat[x][y])
        print("\n")


def getBipartiteCliques(aMat):
    print("In getBC\n")
    cList = []
    aLen = len(aMat)
    bLen = len(aMat[0])
    printMat(aMat)
    print(aLen, bLen,  " are aLen and bLen\n\n")
    for x in range(0,  aLen):
        tmpList = []
        tmpObj = [obj[x]]
        
        for y in range(0,  bLen):
            if aMat[x][y]=='1':
                tmpList.append(attr[y])
                
        tmp = tmpObj,  tmpList
        cList.append(tmp)
        
    for x in range(0,  bLen):
        tmpList = []
        tmpattr = [attr[x]]
        
        for y in range(0,  aLen):
            if aMat[y][x]=='1':
                tmpList.append(obj[y])
                
        tmp = tmpList,  tmpattr
        cList.append(tmp)
        
    return cList
        
    
def condenseList(list):
    return []
    


obj = input("Input objects seperated by space\n").split()
numObj = len(obj)

attr = input("Input attributes seperated by space\n").split()
numAttr = len(attr)


aMat = [[ 0 for i in range(numAttr)] for j in range(numObj)]

print("Enter the adjecency matrix in row major order\n")
for x in range(0, len(obj)):
    for y in range(0,  len(attr)):
        aMat[x][y] = input()


bCliques = getBipartiteCliques(aMat)

bCListSize = len(bCliques)
bCListSizeCondensed = -1

while bCListSize != bCListSizeCondensed:
        bCliques = condenseList(bCliques)
        bCListSizeCondensed = len(bCliques)
               


print(bCliques)













