from PIL import Image
from numpy import size
from py import process
import colorsys

unprocessed_image = Image.open("maze.png")
processed_image = unprocessed_image.convert("HSV")

#region HSV Values

# Row 1
hsv_value0 = processed_image.getpixel((70,70))
hsv_value1 = processed_image.getpixel((130,70))
hsv_value2 = processed_image.getpixel((190,70))
hsv_value3 = processed_image.getpixel((250,70))
hsv_value4 = processed_image.getpixel((310,70))
hsv_value5 = processed_image.getpixel((370,70))
hsv_value6 = processed_image.getpixel((430,70))
hsv_value7 = processed_image.getpixel((490,70))
hsv_value8 = processed_image.getpixel((555,70))
hsv_value9 = processed_image.getpixel((615,70))

# Row 2
hsv_value10 = processed_image.getpixel((70,130))
hsv_value11 = processed_image.getpixel((130,130))
hsv_value12 = processed_image.getpixel((190,130))
hsv_value13 = processed_image.getpixel((250,130))
hsv_value14 = processed_image.getpixel((310,130))
hsv_value15 = processed_image.getpixel((370,130))
hsv_value16 = processed_image.getpixel((430,130))
hsv_value17 = processed_image.getpixel((490,130))
hsv_value18 = processed_image.getpixel((555,130))
hsv_value19 = processed_image.getpixel((615,130))

# Row 3
hsv_value20 = processed_image.getpixel((70,190))
hsv_value21 = processed_image.getpixel((130,190))
hsv_value22 = processed_image.getpixel((190,190))
hsv_value23 = processed_image.getpixel((250,190))
hsv_value24 = processed_image.getpixel((310,190))
hsv_value25 = processed_image.getpixel((370,190))
hsv_value26 = processed_image.getpixel((430,190))
hsv_value27 = processed_image.getpixel((490,190))
hsv_value28 = processed_image.getpixel((555,190))
hsv_value29 = processed_image.getpixel((615,190))

# Row 4
hsv_value30 = processed_image.getpixel((70,250))
hsv_value31 = processed_image.getpixel((130,250))
hsv_value32 = processed_image.getpixel((190,250))
hsv_value33 = processed_image.getpixel((250,250))
hsv_value34 = processed_image.getpixel((310,250))
hsv_value35 = processed_image.getpixel((370,250))
hsv_value36 = processed_image.getpixel((430,250))
hsv_value37 = processed_image.getpixel((490,250))
hsv_value38 = processed_image.getpixel((555,250))
hsv_value39 = processed_image.getpixel((615,250))

# Row 5
hsv_value40 = processed_image.getpixel((70,310))
hsv_value41 = processed_image.getpixel((130,310))
hsv_value42 = processed_image.getpixel((190,310))
hsv_value43 = processed_image.getpixel((250,310))
hsv_value44 = processed_image.getpixel((310,310))
hsv_value45 = processed_image.getpixel((370,310))
hsv_value46 = processed_image.getpixel((430,310))
hsv_value47 = processed_image.getpixel((490,310))
hsv_value48 = processed_image.getpixel((555,310))
hsv_value49 = processed_image.getpixel((615,310))

# Row 6
hsv_value50 = processed_image.getpixel((70,370))
hsv_value51 = processed_image.getpixel((130,370))
hsv_value52 = processed_image.getpixel((190,370))
hsv_value53 = processed_image.getpixel((250,370))
hsv_value54 = processed_image.getpixel((310,370))
hsv_value55 = processed_image.getpixel((370,370))
hsv_value56 = processed_image.getpixel((430,370))
hsv_value57 = processed_image.getpixel((490,370))
hsv_value58 = processed_image.getpixel((555,370))
hsv_value59 = processed_image.getpixel((615,370))

# Row 7
hsv_value60 = processed_image.getpixel((70,430))
hsv_value61 = processed_image.getpixel((130,430))
hsv_value62 = processed_image.getpixel((190,430))
hsv_value63 = processed_image.getpixel((250,430))
hsv_value64 = processed_image.getpixel((310,430))
hsv_value65 = processed_image.getpixel((370,430))
hsv_value66 = processed_image.getpixel((430,430))
hsv_value67 = processed_image.getpixel((490,430))
hsv_value68 = processed_image.getpixel((555,430))
hsv_value69 = processed_image.getpixel((615,430))

# Row 8
hsv_value70 = processed_image.getpixel((70,490))
hsv_value71 = processed_image.getpixel((130,490))
hsv_value72 = processed_image.getpixel((190,490))
hsv_value73 = processed_image.getpixel((250,490))
hsv_value74 = processed_image.getpixel((310,490))
hsv_value75 = processed_image.getpixel((370,490))
hsv_value76 = processed_image.getpixel((430,490))
hsv_value77 = processed_image.getpixel((490,490))
hsv_value78 = processed_image.getpixel((555,490))
hsv_value79 = processed_image.getpixel((615,490))

# Row 9
hsv_value80 = processed_image.getpixel((70,550))
hsv_value81 = processed_image.getpixel((130,550))
hsv_value82 = processed_image.getpixel((190,550))
hsv_value83 = processed_image.getpixel((250,550))
hsv_value84 = processed_image.getpixel((310,550))
hsv_value85 = processed_image.getpixel((370,550))
hsv_value86 = processed_image.getpixel((430,550))
hsv_value87 = processed_image.getpixel((490,550))
hsv_value88 = processed_image.getpixel((555,550))
hsv_value89 = processed_image.getpixel((615,550))

# Row 10
hsv_value90 = processed_image.getpixel((70,610))
hsv_value91 = processed_image.getpixel((130,610))
hsv_value92 = processed_image.getpixel((190,610))
hsv_value93 = processed_image.getpixel((250,610))
hsv_value94 = processed_image.getpixel((310,610))
hsv_value95 = processed_image.getpixel((370,610))
hsv_value96 = processed_image.getpixel((430,610))
hsv_value97 = processed_image.getpixel((490,610))
hsv_value98 = processed_image.getpixel((555,610))
hsv_value99 = processed_image.getpixel((615,610))

#endregion

hsv_value_list = []
hsv_value_list.extend([hsv_value0, hsv_value1, hsv_value2, hsv_value3, hsv_value4, hsv_value5, hsv_value6, hsv_value7, hsv_value8, hsv_value9,
                    hsv_value10, hsv_value11, hsv_value12, hsv_value13, hsv_value14, hsv_value15, hsv_value16, hsv_value17, hsv_value18, hsv_value19,
                    hsv_value20, hsv_value21, hsv_value22, hsv_value23, hsv_value24, hsv_value25, hsv_value26, hsv_value27, hsv_value28, hsv_value29,
                    hsv_value30, hsv_value31, hsv_value32, hsv_value33, hsv_value34, hsv_value35, hsv_value36, hsv_value37, hsv_value38, hsv_value39,
                    hsv_value40, hsv_value41, hsv_value42, hsv_value43, hsv_value44, hsv_value45, hsv_value46, hsv_value47, hsv_value48, hsv_value49,
                    hsv_value50, hsv_value51, hsv_value52, hsv_value53, hsv_value54, hsv_value55, hsv_value56, hsv_value57, hsv_value58, hsv_value59,
                    hsv_value60, hsv_value61, hsv_value62, hsv_value63, hsv_value64, hsv_value65, hsv_value66, hsv_value67, hsv_value68, hsv_value69,
                    hsv_value70, hsv_value71, hsv_value72, hsv_value73, hsv_value74, hsv_value75, hsv_value76, hsv_value77, hsv_value78, hsv_value79,
                    hsv_value80, hsv_value81, hsv_value82, hsv_value83, hsv_value84, hsv_value85, hsv_value86, hsv_value87, hsv_value88, hsv_value89,
                    hsv_value90, hsv_value91, hsv_value92, hsv_value93, hsv_value94, hsv_value95, hsv_value96, hsv_value97, hsv_value98, hsv_value99])

maze_array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                       
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  

currBlockIndex = 0
for hsv_value in hsv_value_list:
    i = ((int)(currBlockIndex / 10)) % 10
    j = currBlockIndex % 10
    color_value = 0

    if (hsv_value[0] == 0 and hsv_value[2] == 255):
        color_value = 1
    elif (hsv_value[0] == 97):
        color_value = 2
    elif (hsv_value[0] == 253):
        color_value = 3

    maze_array[i][j] = color_value
    currBlockIndex += 1

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

