

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
        
    
def condenseList(inputlist):
    clist = []
    toSkip = []
    for x in range(0,  len(inputlist)):
        if x in toSkip:
            continue
        matched = 0;   
        for y in range(x+1, len(inputlist)):
            if y in toSkip:
                continue
            if set(inputlist[x][0]) == set(inputlist[y][0]):
                tmpTuple = inputlist[x][0],  list(set(inputlist[x][1]).union(set(inputlist[y][1])))
                clist.append(tmpTuple)
                toSkip.append(y)
                matched = 1
                break
            elif set(inputlist[x][1]) == set(inputlist[y][1]):
                tmpTuple = list( set(inputlist[x][0]).union(set(inputlist[y][0])) ),  inputlist[x][1]
                clist.append(tmpTuple)
                toSkip.append(y)
                matched = 1;
                break
        if matched == 0:
            clist.append(inputlist[x])
            
    return clist
    


obj = input("Input objects seperated by space\n").split()
numObj = len(obj)

attr = input("Input attributes seperated by space\n").split()
numAttr = len(attr)


aMat = [[ 0 for i in range(numAttr)] for j in range(numObj)]

print("Enter the adjecency matrix in row major order (0 or 1, one element per line)\n")
for x in range(0, len(obj)):
    for y in range(0,  len(attr)):
        aMat[x][y] = input()

#Get Bipartite Cliques
bCliques = getBipartiteCliques(aMat)


bCListSize = len(bCliques)
bCListSizeCondensed = -1

#Condense bipartite cliques until no change
while bCListSize != bCListSizeCondensed:
        bCListSize = len(bCliques)
        bCliques = condenseList(bCliques)
        bCListSizeCondensed = len(bCliques)
               
print("\nDone\n",  bCliques)











