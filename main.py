

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
        
    
def condenseList(inputlist):
    clist = []
    toSkip = []
    print("\n\nIn condenlist, got list", inputlist,  "\nand len of list is ",  len(inputlist))
    for x in range(0,  len(inputlist)):
        if x in toSkip:
            print("Skipping from top")
            continue
        matched = 0;   
        for y in range(x+1, len(inputlist)):
            print("x is: ",  x,  " and y is ",  y, " values: ",  inputlist[x],  inputlist[y])
            if y in toSkip:
                print("Skipping")
                continue
            if set(inputlist[x][0]) == set(inputlist[y][0]):
                print("in first condition")
                tmpTuple = inputlist[x][0],  list(set(inputlist[x][1]).union(set(inputlist[y][1])))
                print("Appending to clist: ",  tmpTuple)
                clist.append(tmpTuple)
                toSkip.append(y)
                matched = 1
                break
            elif set(inputlist[x][1]) == set(inputlist[y][1]):
                print("in second condition")
                tmpTuple = list( set(inputlist[x][0]).union(set(inputlist[y][0])) ),  inputlist[x][1]
                print("Appending to clist: ",  tmpTuple)
                clist.append(tmpTuple)
                toSkip.append(y)
                matched = 1;
                break
        if matched == 0:
            print("Appending to clist: ",  inputlist[x])
            clist.append(inputlist[x])
            
    return clist
    


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
#print(bCliques)



bCListSize = len(bCliques)
bCListSizeCondensed = -1

while bCListSize != bCListSizeCondensed:
        bCListSize = len(bCliques)
        bCliques = condenseList(bCliques)
        bCListSizeCondensed = len(bCliques)
        print("Clist size is ",  bCListSizeCondensed)
               


print("\nDone\n",  bCliques)











