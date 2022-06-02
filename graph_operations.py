from tracemalloc import start
import networkx as nx
from photo_processing import maze_array as mazeArray

mazeGraph = nx.Graph()

# Import array from photoprocessing
# import(mazeArray) from photoprocessesing
         
# NOTE Python 2d array scuffed... exampleArray[i][j] = col x row   AND NOT   row x col

# Test array
# mazeArray = [[2, 1, 0, 3, 1, 1, 0, 0, 0, 0],
#              [1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
#              [1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
#              [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
#              [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],                       
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]                                                      

# # Test array 2
# mazeArray = [[2, 1, 0, 1, 1, 1, 0, 0, 0, 0],
#              [1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
#              [1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
#              [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
#              [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],                       
#              [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
#              [0, 1, 1, 1, 1, 0, 1, 0, 0, 0],
#              [0, 0, 0, 1, 0, 3, 1, 0, 0, 0],
#              [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
#              [0, 0, 0, 1, 1, 1, 0, 0, 0, 0]]

def printSolvedMaze(solvedMazeArray):
    print(solvedMazeArray[0])
    print(solvedMazeArray[1])
    print(solvedMazeArray[2])
    print(solvedMazeArray[3])
    print(solvedMazeArray[4])
    print(solvedMazeArray[5])
    print(solvedMazeArray[6])
    print(solvedMazeArray[7])
    print(solvedMazeArray[8])
    print(solvedMazeArray[9])


def processColor(mazeBlockValue, mazeBlockIndex):
    if (mazeBlockValue == 0):
        return "black"
    elif (mazeBlockValue == 1):
        return "white"
    elif (mazeBlockValue == 2):
        return "green"
    elif (mazeBlockValue == 3):
        return "red"


# Initializing each node in graph with its color value
currIndex = 0
startIndex = 0
endIndex = 0

for i in range(10):
    for j in range(10):
        blockColor = processColor(mazeArray[i][j], currIndex)
        mazeGraph.add_node(currIndex, color=blockColor)
        
        if blockColor == "green":
            startIndex = currIndex
        elif blockColor == "red":
            endIndex = currIndex

        currIndex += 1


# Initializing the edges between each non-black node (0 == black). Only looks for the 4 directly 
# touching neighbors instead of all 8 surrounding neighbors. Uses try catch statements to work 
# around making a bigger array. Otherwise, I'd have to worry about catching IndexOutOfBounds exceptions.
currIndex = 0

for i in range(10):
    for j in range(10):
        try:
            if (mazeArray[i][j-1] != 0 and mazeArray[i][j] != 0 and currIndex % 10 != 0):
                mazeGraph.add_edge(currIndex - 1, currIndex)
                
        except:
            print("error")

        try:
            if (mazeArray[i][j+1] != 0 and mazeArray[i][j] != 0):
                mazeGraph.add_edge(currIndex + 1, currIndex)
               
        except:
            0

        try:
            if (mazeArray[i-1][j] != 0 and mazeArray[i][j] != 0):
                mazeGraph.add_edge(currIndex - 10, currIndex)

        except:
            0

        try:
            if (mazeArray[i+1][j] != 0 and mazeArray[i][j] != 0 and currIndex % 10 != 9):
                mazeGraph.add_edge(currIndex + 10, currIndex)

        except:
            0    

        currIndex += 1



mazePath = nx.shortest_path(mazeGraph, startIndex, endIndex)
print(mazeGraph.edges)

solvedMazeArray = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                       
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  


currIndex = 0
for i in range(10):
    for j in range(10):
        if currIndex in mazePath:
            if (currIndex != startIndex and currIndex != endIndex):
                mazeArray[i][j] = 4

        currIndex += 1

# printSolvedMaze(mazeArray)