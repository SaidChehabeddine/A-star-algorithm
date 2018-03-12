import numpy
from heapq import *


def heuristic(start, end):
    x = (end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2
    return x

def astar(map, start, goal):

    

    Visited = set()
    Available = {}
    pathScore = {start:0}
    HeurScore = {start:heuristic(start, goal)}
    Heap = []

    heappush(Heap, (HeurScore[start], start))
    neighbors = [(0,1),(1,1),(1,0),(-1,0),(-1,-1),(0,-1),(1,-1),(-1,1)]
    while Heap:

        currNode = heappop(Heap)[1]

        if currNode == goal:
            data = []
            while currNode in Available:
                data.append(currNode)
                currNode = Available[currNode]
            return data

        Visited.add(currNode)
        
        for z in neighbors:
            x = z[0]
            y = z[1]
            
            neighbor = currNode[0] + x, currNode[1] + y            
            tempPscore = pathScore[currNode] + heuristic(currNode, neighbor)
            
            
            if map.shape[0]>neighbor[0] and neighbor[0] >=0:
                if map.shape[1]>neighbor[1] and neighbor[1] >=0:                
                    if map[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # map bound y walls
                    continue
            else:
                # map bound x walls
                continue
                
            if neighbor in Visited and tempPscore >= pathScore.get(neighbor, 0):
                continue
                
            if  tempPscore < pathScore.get(neighbor, 0) or neighbor not in [i[1]for i in Heap]:
                Available[neighbor] = currNode
                pathScore[neighbor] = tempPscore
                HeurScore[neighbor] = tempPscore + heuristic(neighbor, goal)
                heappush(Heap, (HeurScore[neighbor], neighbor))
                
    return False

'''Here is an example of using my algo with a numpy map,
   astar(map, start, destination)
   astar function returns a list of points (shortest path)'''

def printer(map,path):
    x= len(map)-1
    for i in range(len(map)):
        s =''
        for j in range(len(map[0])):
            if map[x-i][j] == 1:
                s += '#'
            elif (x-i,j) in path:
                s += '*'
            else:
                s += '.'
        print(s)
                
def levelclear():
    l = [0]*35
    return l
def obstacleLevel(l,x1,x2):
    for i in range(x2-x1 +1):
        l[x1+i] = 1
        
        
##define all levels

l0 = levelclear()
l1 = levelclear()
l2 = levelclear()
l3 = levelclear()
l4 = levelclear()
l5 = levelclear()
l6 = levelclear()
l7 = levelclear()
l8 = levelclear()
l9 = levelclear()
l10 = levelclear()
l11 = levelclear()
l12 = levelclear()
l13 = levelclear()
l14 = levelclear()
l15 = levelclear()
l16 = levelclear()
l17 = levelclear()
l18 = levelclear()
l19 = levelclear()
l20 = levelclear()
l21 = levelclear()
l22 = levelclear()
l23 = levelclear()
l24 = levelclear()
l25 = levelclear()
l26 = levelclear()
l27 = levelclear()
l28 = levelclear()
l29 = levelclear()
l30 = levelclear()
l31 = levelclear()
l32 = levelclear()
l33 = levelclear()
l34 = levelclear()


## object 1
obstacleLevel(l4,10,12)
obstacleLevel(l5,9,12)
obstacleLevel(l6,8,12)
obstacleLevel(l7,7,12)
obstacleLevel(l8,6,12)
obstacleLevel(l9,6,12)
obstacleLevel(l10,6,12)

##object 2
obstacleLevel(l6,20,28)
obstacleLevel(l7,21,28)
obstacleLevel(l8,21,28)
obstacleLevel(l9,22,28)
obstacleLevel(l10,22,28)
obstacleLevel(l11,23,28)
obstacleLevel(l12,23,28)
obstacleLevel(l13,24,28)
obstacleLevel(l14,24,28)
obstacleLevel(l15,25,28)
obstacleLevel(l16,26,28)
obstacleLevel(l17,26,28)
obstacleLevel(l18,27,28)
obstacleLevel(l19,28,28)

##object 3
obstacleLevel(l11,14,17)
obstacleLevel(l12,14,17)
obstacleLevel(l13,14,17)
obstacleLevel(l14,14,17)
obstacleLevel(l15,14,17)

##object 4
obstacleLevel(l16,9,12)
obstacleLevel(l17,9,12)
obstacleLevel(l18,9,12)
obstacleLevel(l19,9,12)
obstacleLevel(l20,9,12)

##object 5
obstacleLevel(l16,18,24)
obstacleLevel(l17,18,24)
obstacleLevel(l18,18,24)
obstacleLevel(l19,18,24)

##object 6
obstacleLevel(l28,12,28)
obstacleLevel(l27,12,28)
obstacleLevel(l26,12,28)
obstacleLevel(l25,12,28)
obstacleLevel(l24,25,28)
obstacleLevel(l23,25,28)
obstacleLevel(l22,25,28)


nmap = numpy.array([l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l23,l24,l25,l26,l27,l28,l29,l30,l31,l32,l33,l34
])

printer(nmap,astar(nmap, (2,2), (32,32)))