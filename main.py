import networkx as nx
import matplotlib.pyplot as plt


def printMat(Mat):
    print("Print matrix\n")
    for x in range(0, len(Mat)):
        for y in range(0,  len(Mat[0])):
            print(Mat[x][y])
        print("\n")
        
 ###########################################################  

def getBipartiteCliques(aMat):
    cList = []
    aLen = len(aMat)
    bLen = len(aMat[0])
#    printMat(aMat)
#   print(aLen, bLen,  " are aLen and bLen\n\n")
    for x in range(0,  aLen):
        tmpList = []
        tmpObj = [obj[x]]
        
        for y in range(0,  bLen):
            if aMat[x][y]=='1':
                tmpList.append(attr[y])
                
        tmp = tmpObj,  tmpList
        dictBC[obj[x]] = tmpList
        cList.append(tmp)
        
    for x in range(0,  bLen):
        tmpList = []
        tmpattr = [attr[x]]
        
        for y in range(0,  aLen):
            if aMat[y][x]=='1':
                tmpList.append(obj[y])
                
        tmp = tmpList,  tmpattr
        dictBC[attr[x]] = tmpList
        cList.append(tmp)
        
    return cList
        
 ###########################################################   
 
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
    
###########################################################  
     
def removeUnclosed(clist):
    flist = []
    listo = []
    lista = []
    for x in range(0,  len(clist)):
        lista = []
        listo = []
        for y in range(0,  len(clist[x][0])):
            if lista == []:
                lista = dictBC[clist[x][0][y]]
            else:    
                lista = list( set(lista).intersection( set(dictBC[clist[x][0][y]] )))
                
        for z in range(0,  len(clist[x][1])):
            if listo == []:
                listo = dictBC[clist[x][1][z]]
            else:
                listo = list( set(listo).intersection(set(dictBC[clist[x][1][z]] )))
 #       print ("printing both list for ",  x,  lista,  listo)
        if set(lista) == set(clist[x][1]) and set(listo) == set(clist[x][0]):
            flist.append(clist[x])
    return flist

 ###########################################################
 
def printLattice(bCList):
    G=nx.Graph()
    for x in range(0, len(bCList)):
        nodeName = "".join(str(m) for m in bCList[x][0]) + ", " + "".join(str(m) for m in bCList[x][1])
        G.add_node(nodeName )
     
    for x in range(0, len(bCList)):
        for y in range(x+1, len(bCList)):
            if set(bCList[x][0]).issubset(set(bCList[y][0])):
                nodeName1 = "".join(str(m) for m in bCList[x][0]) + ", " + "".join(str(m) for m in bCList[x][1]) 
                nodeName2 = "".join(str(m) for m in bCList[y][0]) + ", " + "".join(str(m) for m in bCList[y][1])
                G.add_edge(nodeName1 , nodeName2)
                hasSuccessor.append(x)
                hasPredecessor.append(y)
                
    #Creating top most and bottom most node            
    listo = []
    lista = []
    for x in range(0, len(attr)):
        if listo == []:
            listo = dictBC[attr[x]]
        else:
            listo = list( set(listo).intersection(set(attr[x] )))
            
    for x in range(0, len(obj)):
        if lista == []:
            lista = dictBC[obj[x]]
        else:
            lista = list( set(lista).intersection(set(obj[x] )))
    if lista == []:
        lista = ["null"]
    if listo == []:
        listo = ["null"]
    
    #adding them to graph
    firstNode = "".join(str(m) for m in listo) + ", " + "".join(str(m) for m in attr)
    G.add_node(firstNode )
    lastNode = "".join(str(m) for m in obj) + ", " + "".join(str(m) for m in lista)
    G.add_node(lastNode )
    
    #adding edges to them
    for x in range(0, len(bCList)):
        if x not in hasSuccessor:
            nodeName = "".join(str(m) for m in bCList[x][0]) + ", " + "".join(str(m) for m in bCList[x][1])
            G.add_edge(nodeName,  lastNode )
            
    for x in range(0, len(bCList)):
        if x not in hasPredecessor:
            nodeName = "".join(str(m) for m in bCList[x][0]) + ", " + "".join(str(m) for m in bCList[x][1])
            G.add_edge(nodeName,  firstNode )
    nx.draw(G)
    plt.savefig("lattice.png")


###########################################################
 
######################## starts here ###########################



dictBC = {}
hasSuccessor = []
hasPredecessor = []


obj = input("Input objects seperated by space:\n").split()
numObj = len(obj)

attr = input("\nInput attributes seperated by space:\n").split()
numAttr = len(attr)

aMat = [[ 0 for i in range(numAttr)] for j in range(numObj)]

print("\nEnter the adjecency matrix in row major order (0 or 1, one element per line):\n")
for x in range(0, len(obj)):
    for y in range(0,  len(attr)):
        aMat[x][y] = input()

#Get Bipartite Cliques
bCliques = getBipartiteCliques(aMat)
bCliquesStore = bCliques

bCListSize = len(bCliques)
bCListSizeCondensed = -1

#Condense bipartite cliques until no change
while bCListSize != bCListSizeCondensed:
        bCListSize = len(bCliques)
        bCliques = condenseList(bCliques)
        bCListSizeCondensed = len(bCliques)
               


#filter concepts
bCliques = removeUnclosed(bCliques)
print("\nNodes of Concept Lattice:\n")
for x in range(0,  len(bCliques)):
        extent = "".join(str(m) for m in sorted(bCliques[x][0]))
        intent = "".join(str(m) for m in sorted(bCliques[x][1]))
        print ("(", extent,  ",", intent,  ")")

conceptDict = {}
for x in range(0,  len(bCliques)):
    object = "".join(str(m) for m in sorted(bCliques[x][0]))
    attribute = "".join(str(m) for m in sorted(bCliques[x][1]))
    conceptDict[object ] = set(bCliques[x][1])
    conceptDict[attribute ] = set(bCliques[x][0])

#sort the concepts based on intent length
bCliques.sort(key=lambda x: len(x[0]))

#generate the image file containing the lattice

printLattice(bCliques)
print("\nLattice has been generated in file 'lattice.png'\n")

#Queries
while True:
    qin = input("Enter the query. Intent or Extent seperated by space, Ex- 2 3 4 OR a b\nEnter 'Q' to exit.\n")
    if qin == "Q":
        exit(0)
    key = "".join(str(m) for m in sorted(qin.split()))
    if key in conceptDict:
        print(', '.join(conceptDict[key]),  "\n")
    else:
        print("Not present in Concept lattice\n")







