import random

class Square:
    def __init__(self, pos, num, type):
        self.pos = pos
        self.num = num
        self.type = type
        self.x = self.pos % 4 * 180 + 100
        self.y = self.pos // 4 * 180 + 100
        self.pic = loadImage("demo.png")
        
    def draw(self):
        if self.type == 0:
            rectMode(CENTER)
            fill("#ECE0CA")
            rect(self.x, self.y, 160, 160, 20)
            imageMode(CENTER)
            image(self.pic, self.x, self.y, self.num * 10, self.num * 10)

def setup():
    size(740, 740)
    noStroke()
    
    global squares, boom
    squares = []
    for i in range(16):
        squares.append(Square(0, 0, 1))
    addNew()
    
def draw():
    global squares
    rectMode(CORNER)
    fill("#BAAEA0")
    rect(0, 0, 740, 740)
    fill("#CDC1B3")
    for i in range(4):
        for j in range(4):
            rect(i * 180 + 20, j * 180 + 20, 160, 160, 20)
    for i in squares:
        i.draw()
        
def addNew():
    global squares
    news = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
    rng = random.randint(0, 15)
    type = news[random.randint(0, 9)]
    if squares[rng].type == 1:
        squares[rng] = Square(rng, type, 0)
    else:
        addNew()
            
def keyPressed():
    global squares, boom
    if keyCode == UP:
        for a in range(4):
            for h in range(4):
                i = 3 - h
                for j in range(4):
                    if squares[4 * i + j].type == 0 and 4 * (i - 1) + j >= 0 and squares[4 * (i - 1) + j].num == squares[4 * i + j].num:
                        squares[4 * (i - 1) + j] = Square(4 * (i - 1) + j, squares[4 * i + j].num * 2, 0)
                        squares[4 * i + j] = Square(0, 0, 1)
                    elif squares[4 * i + j].type == 0 and not (4 * (i - 1) + j < 0 or squares[4 * (i - 1) + j].type == 0):
                        squares[4 * (i - 1) + j] = Square(4 * (i - 1) + j, squares[4 * i + j].num, 0)
                        squares[4 * i + j] = Square(0, 0, 1)
        addNew()
    elif keyCode == RIGHT:
        for a in range(4):
            for j in range(4):
                for i in range(4):
                    if squares[4 * i + j].type == 0 and 4 * i + j + 1 < 16 and squares[4 * i + j + 1].num == squares[4 * i + j].num:
                        squares[4 * i + j + 1] = Square(4 * i + j + 1, squares[4 * i + j].num * 2, 0)
                        squares[4 * i + j] = Square(0, 0, 1)
                    elif squares[4 * i + j].type == 0 and not ((4 * i + j + 1) % 4 == 0 or squares[4 * i + j + 1].type == 0):
                        squares[4 * i + j + 1] = Square(4 * i + j + 1, squares[4 * i + j].num, 0)
                        squares[4 * i + j] = Square(0, 0, 1)
        addNew()
    elif keyCode == DOWN:
        for a in range(4):
            for i in range(4):
                for j in range(4):
                    if squares[4 * i + j].type == 0 and 4 * (i + 1) + j < 16 and squares[4 * (i + 1) + j].num == squares[4 * i + j].num:
                        squares[4 * (i + 1) + j] = Square(4 * (i + 1) + j, squares[4 * i + j].num * 2, 0)
                        squares[4 * i + j] = Square(0, 0, 1)
                    elif squares[4 * i + j].type == 0 and not (4 * (i + 1) + j > 15 or squares[4 * (i + 1) + j].type == 0):
                        squares[4 * (i + 1) + j] = Square(4 * (i + 1) + j, squares[4 * i + j].num, 0)
                        squares[4 * i + j] = Square(0, 0, 1)
        addNew()
    elif keyCode == LEFT:
        for a in range(4):
            for k in range(4):
                j = 3 - k
                for i in range(4):
                    if squares[4 * i + j].type == 0 and 4 * i + j - 1 >= 0 and squares[4 * i + j - 1].num == squares[4 * i + j].num:
                        squares[4 * i + j - 1] = Square(4 * i + j - 1, squares[4 * i + j].num * 2, 0)
                        squares[4 * i + j] = Square(0, 0, 1)
                    elif squares[4 * i + j].type == 0 and not ((4 * i + j - 1) % 4 == 3 or squares[4 * i + j - 1].type == 0):
                        squares[4 * i + j - 1] = Square(4 * i + j - 1, squares[4 * i + j].num, 0)
                        squares[4 * i + j] = Square(0, 0, 1) 
        addNew()               
