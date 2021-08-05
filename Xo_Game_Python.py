class Board:
    # พีรพล พันธุ์สง่า 6301012620162
    # ธนธรณ์ เหล่าทวีคุณ 6301012610043
    # ปุญชรัสมิ์ วงค์คม 6301012620146
    # ธรรณทรณ์ สมตน 6201012610010
    def __init__(self):
        self.board_array = [["1", "2", "3"],["4", "5", "6"], ["7", "8", "9"]]
        self.player = "X"
        self.turn_count = 0
    def display_board(self):
        print()
        for y in self.board_array:
            print("| ",end="")
            for x in y:
                print(x,end=" ")
            print("|")
        print()
    def change_player(self):
        if self.player =='X':
            self.player = 'O'
        else:
            self.player = 'X'
    def add_postion(self) :
        self.turn_count += 1
        done = False
        while(not done):
            print("Turn " + self.player)
            inputtext = input("Select Position 1 - 9 > ")
            if inputtext.isnumeric():
                arg = int(inputtext) - 1
                if (arg <= 8 and arg >= 0):
                    column = int(arg/3)
                    row = int(arg%3)
                    if self.board_array[column][row] != "X" and self.board_array[column][row] != "O":
                        self.board_array[column][row] = self.player
                        done = True
                        break
                    else :
                        print("This position is already added")
                        done = False
            
    def check_winner(self):
        if self.board_array[0][0] == self.board_array[0][1] == self.board_array[0][2] or\
            self.board_array[1][0] == self.board_array[1][1] == self.board_array[1][2] or\
            self.board_array[2][0] == self.board_array[2][1] == self.board_array[2][2] or\
            self.board_array[0][0] == self.board_array[1][0] == self.board_array[2][0] or\
            self.board_array[0][1] == self.board_array[1][1] == self.board_array[2][1] or\
            self.board_array[0][2] == self.board_array[1][2] == self.board_array[2][2] or\
            self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2] or\
            self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]:
            if self.player == "X":
                self.display_board()
                print("Player O Win")
            else:
                self.display_board()
                print("Player X Win")
                return True
        elif self.turn_count == 9:
            print("to end in a tie")
            return True
        else:
            return False

board = Board()
while(not board.check_winner()):
    board.display_board()
    board.add_postion()
    board.change_player()
    