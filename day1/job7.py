class Player:
    def __init__ (self, name, posx, posy):
        self.name = name
        self.posx = posx
        self.posy = posy

    def move_up(self):
        self.posy += 1
        return self.posy
    def move_down(self):
        self.posy -= 1
        return self.posy
    def move_right(self):
        self.posx += 1
        return self.posx
    def move_left(self):
        self.posx -= 1
        return self.posx
    
    def matrix(self):
        return self.posx, self.posy
player1 = Player("John", 0, 0)

for i in range(5):
    
    print(player1.move_up())
    print(player1.move_down()) 
    print(player1.move_right())
    print(player1.move_left())
    print(player1.move_up())
    print(player1.move_up())
    print(player1.move_right())
    print(player1.matrix())



