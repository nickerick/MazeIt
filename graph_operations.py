import networkx as nx

mazeGraph = nx.Graph()

# Import array from photoprocessing
# import(mazeArray) from photoprocessesing
         
# Test array
mazeArray = [[2, 1, 0, 3, 0, 0, 0, 0, 0, 0],
             [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                       
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]                                                      


def processColor(mazeBlockValue):
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

for i in range(10):
    for j in range(10):
        blockColor = processColor(mazeArray[i][j])
        mazeGraph.add_node(currIndex, color=blockColor)
        currIndex += 1


# Initializing the edges between each non-black node (0 == black). Only looks for the 4 directly 
# touching neighbors instead of all 8 surrounding neighbors. Uses try catch statements to work 
# around making a bigger array. Otherwise, I'd have to worry about catching IndexOutOfBounds exceptions.
currIndex = 0

for i in range(10):
    for j in range(10):
        try:
            if (mazeArray[i][j-1] != 0 and mazeArray[i][j] != 0):
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
            if (mazeArray[i+1][j] != 0 and mazeArray[i][j] != 0):
                mazeGraph.add_edge(currIndex + 10, currIndex)
        except:
            0    

        currIndex += 1


mazePath = nx.shortest_path(mazeGraph, 0, 3)
print(mazePath)


# print(type(nx.get_node_attributes(mazeGraph, "color")))

# colorValueArray[10]
# for colorValue in nx.get_node_attributes(mazeGraph, "color").items:
#     if (colorValue == "green" | "red"):
#         colorValueArray.add(colorValue)

# Error Handling
# mazeHasPath = nx.has_path(mazeGraph, )

