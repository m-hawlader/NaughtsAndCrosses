from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

player = ["X","O",(0.906, 0.298, 0.235, 1),(0.204, 0.596, 0.859, 1)]
turn = 0
grid = [[2,2,2],[2,2,2],[2,2,2]]
mutable = [[True, True, True],[True, True, True],[True, True, True]]
moves = 0
move = [[],[],[],[],[],[],[],[],[],[]]
mode = "PVP"
playing = True
coordinates = [2,0]
class MainWidget(FloatLayout):
    def check_win(self):
        global playing
        winner = 2
        counter = 0
        for r in range(3):
            for c in range(3):
                who = grid[r][c]
                if c == 0 and who != 2:
                    if who == grid[r][c+1] and who == grid[r][c+2]:
                        winner = who
                if r == 0 and who != 2:
                    if who == grid[r+1][c] and who == grid[r+2][c]:
                        winner = who
                if r == 0 and c == 0 and who != 2:
                    if who == grid[r+1][c+1] and who == grid[r+2][c+2]:
                        winner = who
                if r == 0 and c == 2 and who != 2:
                    if who == grid[r+1][c-1] and who == grid[r+2][c-2]:
                        winner = who
                if who == 0 or who == 1:
                    counter += 1
        if winner != 2:
            playing = False
            self.turn_label.text=f"{player[winner]} has won the game"
            self.turn_label.color = (0.180, 0.800, 0.443, 1)
        elif counter == 9:
            playing = False
            self.turn_label.text="It is a tie Between X & O"
            self.turn_label.color = (0.945, 0.769, 0.059, 1)
    def plot(self, row, col):
        button = self.nacbs[row][col]
        global turn
        global grid
        global mutable
        global playing
        global moves
        global move
        if mutable[row][col] and playing:
            button.text=player[turn]
            button.background_color = player[turn+2]
            grid[row][col] = turn
            self.check_win()
            if turn == 0:
                turn = 1
            else:
                turn = 0
            mutable[row][col] = False
            if playing:
                self.turn_label.text=f"You're playing {mode}: player {player[turn]} turn"
            moves += 1
            move[moves] = [row,col]
    def check_promise(self):
        global coordinates
        check = False
        x_promise = False
        o_promise = False
        x_coordinate = []
        o_coordinate = []
        for r in range(3):
            for c in range(3):
                if c == 0:
                    x_counter = 0
                    o_counter = 0
                    space_counter=0
                    space_coordinate = []
                    for i in range(3):
                        if grid[r][c+i] == 0:
                            x_counter += 1
                        elif grid[r][c+i] == 1:
                            o_counter += 1
                        elif grid[r][c+i] == 2:
                            space_counter += 1
                            space_coordinate = [r,c+i]
                    if x_counter == 2 and space_counter == 1:
                        check = True
                        x_promise = True
                        x_coordinate = space_coordinate
                    elif o_counter == 2 and space_counter == 1:
                        check = True
                        o_promise = True
                        o_coordinate = space_coordinate
                if r == 0 :
                    x_counter = 0
                    o_counter = 0
                    space_counter=0
                    space_coordinate = []
                    for i in range(3):
                        if grid[r+i][c] == 0:
                            x_counter += 1
                        elif grid[r+i][c] == 1:
                            o_counter += 1
                        elif grid[r+i][c] == 2:
                            space_counter += 1
                            space_coordinate = [r+i,c]
                    if x_counter == 2 and space_counter == 1:
                        check = True
                        x_promise = True
                        x_coordinate = space_coordinate
                    elif o_counter == 2 and space_counter == 1:
                        check = True
                        o_promise = True
                        o_coordinate = space_coordinate
                if r == 0 and c == 0:
                    x_counter = 0
                    o_counter = 0
                    space_counter=0
                    space_coordinate = []
                    for i in range(3):
                        if grid[r+i][c+i] == 0:
                            x_counter += 1
                        elif grid[r+i][c+i] == 1:
                            o_counter += 1
                        elif grid[r+i][c+i] == 2:
                            space_counter += 1
                            space_coordinate = [r+i,c+i]
                    if x_counter == 2 and space_counter == 1:
                        check = True
                        x_promise = True
                        x_coordinate = space_coordinate
                    elif o_counter == 2 and space_counter == 1:
                        check = True
                        o_promise = True
                        o_coordinate = space_coordinate
                if r == 0 and c == 2:
                    x_counter = 0
                    o_counter = 0
                    space_counter=0
                    space_coordinate = []
                    for i in range(3):
                        if grid[r+i][c-i] == 0:
                            x_counter += 1
                        elif grid[r+i][c-i] == 1:
                            o_counter += 1
                        elif grid[r+i][c-i] == 2:
                            space_counter += 1
                            space_coordinate = [r+i,c-i]
                    if x_counter == 2 and space_counter == 1:
                        check = True
                        x_promise = True
                        x_coordinate = space_coordinate
                    elif o_counter == 2 and space_counter == 1:
                        check = True
                        o_promise = True
                        o_coordinate = space_coordinate
        if mode == "Vs AI X":
            if x_promise == True:
                coordinates = x_coordinate
            elif o_promise == True and x_promise == False:
                coordinates = o_coordinate
        elif mode == "Vs AI O":
            if o_promise == True:
                coordinates = o_coordinate
            elif x_promise == True and o_promise == False:
                coordinates = x_coordinate
        return check #if check it returns true then get coordinates
    def check_opportunity(self):
        global coordinates
        check = False
        x_promise = False
        o_promise = False
        x_coordinate = []
        o_coordinate = []
        for r in range(3):
            for c in range(3):
                if c == 0:
                    x_counter = 0
                    o_counter = 0
                    space_counter=0
                    space_coordinate = []
                    for i in range(3):
                        if grid[r][c+i] == 0:
                            x_counter += 1
                        elif grid[r][c+i] == 1:
                            o_counter += 1
                        elif grid[r][c+i] == 2:
                            space_counter += 1
                            space_coordinate = [r,c+i]
                    if x_counter == 2 and space_counter == 1:
                        check = True
                        x_promise = True
                        x_coordinate = space_coordinate
                    elif o_counter == 2 and space_counter == 1:
                        check = True
                        o_promise = True
                        o_coordinate = space_coordinate
                if r == 0 :
                    x_counter = 0
                    o_counter = 0
                    space_counter=0
                    space_coordinate = []
                    for i in range(3):
                        if grid[r+i][c] == 0:
                            x_counter += 1
                        elif grid[r+i][c] == 1:
                            o_counter += 1
                        elif grid[r+i][c] == 2:
                            space_counter += 1
                            space_coordinate = [r+i,c]
                    if x_counter == 2 and space_counter == 1:
                        check = True
                        x_promise = True
                        x_coordinate = space_coordinate
                    elif o_counter == 2 and space_counter == 1:
                        check = True
                        o_promise = True
                        o_coordinate = space_coordinate
                if r == 0 and c == 0:
                    x_counter = 0
                    o_counter = 0
                    space_counter=0
                    space_coordinate = []
                    for i in range(3):
                        if grid[r+i][c+i] == 0:
                            x_counter += 1
                        elif grid[r+i][c+i] == 1:
                            o_counter += 1
                        elif grid[r+i][c+i] == 2:
                            space_counter += 1
                            space_coordinate = [r+i,c+i]
                    if x_counter == 1 and space_counter == 2:
                        check = True
                        x_promise = True
                        x_coordinate = space_coordinate
                    elif o_counter == 1 and space_counter == 2:
                        check = True
                        o_promise = True
                        o_coordinate = space_coordinate
                if r == 0 and c == 2:
                    x_counter = 0
                    o_counter = 0
                    space_counter=0
                    space_coordinate = []
                    for i in range(3):
                        if grid[r+i][c-i] == 0:
                            x_counter += 1
                        elif grid[r+i][c-i] == 1:
                            o_counter += 1
                        elif grid[r+i][c-i] == 2:
                            space_counter += 1
                            space_coordinate = [r+i,c-i]
                    if x_counter == 1 and space_counter == 2:
                        check = True
                        x_promise = True
                        x_coordinate = space_coordinate
                    elif o_counter == 1 and space_counter == 2:
                        check = True
                        o_promise = True
                        o_coordinate = space_coordinate
        if mode == "Vs AI X":
            if x_promise == True:
                coordinates = x_coordinate
            elif o_promise == True and x_promise == False:
                coordinates = o_coordinate
        elif mode == "Vs AI O":
            if o_promise == True:
                coordinates = o_coordinate
            elif x_promise == True and o_promise == False:
                coordinates = x_coordinate
        return check #if check it returns true then get coordinates
    def ai_x(self):
        if moves == 2:
            if move[2] == [1,1]:
                self.plot(0,2)
            elif move[2][1] == 0:
                self.plot(2,2)
            elif move[2][1] == 2 and move[2] != [2,2]:
                self.plot(2,2)
            elif move[2][1] == 2 and move[2] == [2,2]:
                self.plot(0,0)
            elif move[2] == [0,1] or move[2] == [2,1]:
                self.plot(0,0)
        elif moves == 4:
            if move[3] == [2,2]:
                if grid[2][1] == 2:
                    self.plot(2,1)
                elif move[2] == [0,0]:
                    self.plot(0,2)
                elif move[2] == [1,0]:
                    self.plot(0,2)
                elif move[2] == [0,2]:
                    self.plot(0,0)
                elif move[2] == [1,2]:
                    self.plot(0,0)
            elif move[3] == [0,0]:
                if grid[1][0] == 2:
                    self.plot(1,0)
                elif move[2] == [2,1]:
                    self.plot(1,1)
                elif move[2] == [0,1]:
                    self.plot(2,2)
                elif move[2] == [2,2]:
                    self.plot(0,2)
            elif move[3] == [0,2]:
                if move[4] == [0,0]:
                    self.plot(2,2)
                elif move[4] == [2,2]:
                    self.plot(0,0)
                elif move[4] == [1,0]:
                    self.plot(1,2)
                elif move[4] == [1,2]:
                    self.plot(1,0)
                elif move[4] == [0,1]:
                    self.plot(2,1)
                elif move[4] == [2,1]:
                    self.plot(0,1)
        elif moves == 6:
            global coordinates
            prob = self.check_promise()
            if prob == True:
                self.plot(coordinates[0],coordinates[1])
            else:
                probs = self.check_opportunity()
                if probs == True:
                    self.plot(coordinates[0],coordinates[1])
                else:
                    for r in range(3):
                        for c in range(3):
                            if grid[r][c] == 2:
                                self.plot(r,c)
        elif moves == 8:
            for r in range(3):
                for c in range(3):
                    if grid[r][c] == 2:
                        self.plot(r,c)
                        break
    def ai_o(self):
        global coordinates
        if moves == 1 and move[1] != [1,1]:
            self.plot(1,1)
        elif moves == 1 and move[1] == [1,1]:
            self.plot(2,0)
        elif moves == 3:
            if (move[1] == [0,1] or move[1] == [1,2]) and (move[3] == [0,1] or move[3] == [1,2]):
                self.plot(0,2)
            elif (move[1] == [2,0] and move[3] == [0,2]) or (move[1] == [0,2] and move[3] == [2,0]) or (move[1] == [0,0] and move[3] == [2,2]) or (move[1] == [2,2] and move[3] == [0,0]):
                self.plot(2,1)
            elif (move[1] == [0,0] and (move[3] == [1,2] or move[3] == [2,1])) or (move[1] == [0,2] and (move[3] == [2,1] or move[3] == [1,0])) or (move[1] == [2,0] and (move[3] == [0,1] or move[3] == [1,2])) or (move[1] == [2,2] and (move[3] == [0,1] or move[3] == [1,0])):
                if move[1] == [0,0]:
                    if move[3] == [1,2]:
                        self.plot(0,1)
                    elif move[3] == [2,1]:
                        self.plot(1,0)
                elif move[1] == [0,2]:
                    if move[3] == [2,1]:
                        self.plot(1,2)
                    elif move[3] == [1,0]:
                        self.plot(0,1)
                elif move[1] == [2,0]:
                    if move[3] == [0,1]:
                        self.plot(1,0)
                    elif move[3] == [1,2]:
                        self.plot(2,1)
                elif move[1] == [2,2]:
                    if move[3] == [0,1]:
                        self.plot(1,2)
                    elif move[3] == [1,0]:
                        self.plot(2,1)
            elif (move[3] == [0,0] and (move[1] == [1,2] or move[1] == [2,1])) or (move[3] == [0,2] and (move[1] == [2,1] or move[1] == [1,0])) or (move[3] == [2,0] and (move[1] == [0,1] or move[1] == [1,2])) or (move[3] == [2,2] and (move[1] == [0,1] or move[1] == [1,0])):
                if move[3] == [0,0]:
                    if move[1] == [1,2]:
                        self.plot(0,1)
                    elif move[1] == [2,1]:
                        self.plot(1,0)
                elif move[3] == [0,2]:
                    if move[1] == [2,1]:
                        self.plot(1,2)
                    elif move[1] == [1,0]:
                        self.plot(0,1)
                elif move[3] == [2,0]:
                    if move[1] == [0,1]:
                        self.plot(1,0)
                    elif move[1] == [1,2]:
                        self.plot(2,1)
                elif move[3] == [2,2]:
                    if move[1] == [0,1]:
                        self.plot(1,2)
                    elif move[1] == [1,0]:
                        self.plot(2,1)
            else:
                prob = self.check_promise()
                if prob == True:
                    self.plot(coordinates[0],coordinates[1])
                else:
                    probs = self.check_opportunity()
                    if probs == True:
                        self.plot(coordinates[0],coordinates[1])
                    else:
                        for r in range(3):
                            for c in range(3):
                                if grid[r][c] == 2:
                                    self.plot(r,c)
                                    break
        elif moves == 5 or moves == 7:
            prob = self.check_promise()
            if moves == 5 and ((((move[1] == [2,0] and move[3] == [1,2])or(move[3] == [2,0] and move[1] == [1,2])) and move[5] == [0,1]) or (((move[1] == [0,2] and move[3] == [2,1])or(move[3] == [0,2] and move[1] == [2,1])) and move[5] == [1,0]) or (((move[1] == [2,2] and move[3] == [1,0])or(move[3] == [2,2] and move[1] == [1,0])) and move[5] == [0,1]) or (((move[1] == [0,0] and move[3] == [2,1])or(move[3] == [0,0] and move[1] == [2,1])) and move[5] == [1,2]) ):
                if ((move[1] == [2,0] and move[3] == [1,2])or(move[3] == [2,0] and move[1] == [1,2])) and move[5] == [0,1]:
                    self.plot(0,0)
                elif ((move[1] == [0,2] and move[3] == [2,1])or(move[3] == [0,2] and move[1] == [2,1])) and move[5] == [1,0]:
                    self.plot(0,0)
                elif ((move[1] == [2,2] and move[3] == [1,0])or(move[3] == [2,2] and move[1] == [1,0])) and move[5] == [0,1]:
                    self.plot(0,2)
                elif ((move[1] == [0,0] and move[3] == [2,1])or(move[3] == [0,0] and move[1] == [2,1])) and move[5] == [1,2]:
                    self.plot(0,2)
            elif prob == True:
                self.plot(coordinates[0],coordinates[1])
            else:
                probs = self.check_opportunity()
                if probs == True:
                    self.plot(coordinates[0],coordinates[1])
                else:
                    for r in range(3):
                        for c in range(3):
                            if grid[r][c] == 2:
                                self.plot(r,c)
                                break
    def o_handle(self,r,c):
        self.plot(r,c)
        self.ai_o()
    def x_handle(self,r,c):
        self.plot(r,c)
        self.ai_x()
    def setup(self,n):
        global playing
        global turn
        global mutable
        global grid
        global mode
        global moves
        global move
        for r in range(3):
            for c in range(3):
                self.nacbs[r][c].text=""
                self.nacbs[r][c].background_color = (0.925,0.941,0.945,1)
                if n == 0:
                    self.nacbs[r][c].on_press = lambda r=r, c=c: self.plot(r,c)
                elif n == 1:
                    self.nacbs[r][c].on_press = lambda r=r, c=c: self.x_handle(r,c)
                else:
                    self.nacbs[r][c].on_press = lambda r=r, c=c: self.o_handle(r,c)
        turn = 0
        grid = [[2,2,2],[2,2,2],[2,2,2]]
        mutable = [[True, True, True],[True, True, True],[True, True, True]]
        moves = 0
        move = [[],[],[],[],[],[],[],[],[],[]]
        if n == 0:
            mode = "PvP"
        elif n == 1:
            mode = "Vs AI X"
        else:
            mode = "Vs AI O"
        self.turn_label.text = f"You're playing {mode}: player {player[turn]} turn" 
        self.turn_label.color = (1,1,1,1)
        playing = True
        if mode == "Vs AI X":
            self.plot(2,0)
class NaughtsAndCrossesApp(App):
    def build(self):
        return MainWidget()
Window.set_icon("app_icon.png")
Window.clearcolor = (0.173, 0.243, 0.314, 1) #set bg color
NaughtsAndCrossesApp().run() #name of window: NaughtsAndCrosses automatically
