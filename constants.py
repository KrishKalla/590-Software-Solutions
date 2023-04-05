#Color Constants

R1=255
G1=0
B1=0

R2=0
G2=0
B2=255

RB=10
GB=10
BB=10

RED = (255,0,0)
BLUE = (0,0, 255)
YELLOW = (0, 255, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
BACKGROUND = (RB, GB, BB)
CUSTOM1 = (R1,G1,B1)
CUSTOM2 = (R2,G2,B2)

#Dimensions
rowCount = 6
colCount = 7

#Positions
empty = 0
p1 = 1
p2 = 2

#Rendering Size
SIZE = 100
RADIUS = int(SIZE/2 - 8)

#Window Sizes
width = colCount * SIZE
height = rowCount * SIZE + SIZE *2
windowSize = (width, height)

#Historical Size
HSIZE = 25
HRADIUS = int(HSIZE/2 - 2)

#Historical Score
score1 = 0
score2 = 0