class Board:
    # พีรพล พันธุ์สง่า 6301012620162
    # ธนธรณ์ เหล่าทวีคุณ 6301012610043
    # ปุญชรัสมิ์ วงค์คม 6301012620146
    # ธรรณทรณ์ สมตน 6201012610010
    def __init__(self,isNumpadmode):
        if (isNumpadmode):
            self.board_array = [["7", "8", "9"],["4", "5", "6"], ["1", "2", "3"]]
        else:
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
    def add_postion(self,column,row) :
        if self.board_array[column][row] != "X" and self.board_array[column][row] != "O":
            self.board_array[column][row] = self.player
            self.turn_count += 1
            self.change_player()
        else :
            print("This position is already added")
        
    def check_winner(self):
        if self.board_array[0][0] == self.board_array[0][1] == self.board_array[0][2] or\
            self.board_array[1][0] == self.board_array[1][1] == self.board_array[1][2] or\
            self.board_array[2][0] == self.board_array[2][1] == self.board_array[2][2] or\
            self.board_array[0][0] == self.board_array[1][0] == self.board_array[2][0] or\
            self.board_array[0][1] == self.board_array[1][1] == self.board_array[2][1] or\
            self.board_array[0][2] == self.board_array[1][2] == self.board_array[2][2] or\
            self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2] or\
            self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]:
            if self.player == "x":
                self.display_board()
                print("Player o Win")
            else:
                self.display_board()
                print("Player x Win")
                return True
        elif self.turn_count == 9:
            print("to end in a tie")
            return True
        else:
            return False
        
class Input_Processor:
    def __init__(self,isNumpadmode):
        self.isNumpadmode = isNumpadmode
    def input_checker(self,text):
        if (self.isNumpadmode):
            while(True):
                inputtext = input(text)
                if inputtext.isnumeric():
                    arg = (10-int(inputtext)) - 1
                    if (arg <= 8 and arg >= 0):
                        column = int(arg/3)
                        row = 2-int(arg%3)
                        return column,row
                    else:
                        print("Input invalid")
        else:
            while(True):
               inputtext = input(text)
               if inputtext.isnumeric():
                   arg = int(inputtext) - 1
                   if (arg <= 8 and arg >= 0):
                       column = int(arg/3)
                       row = int(arg%3)
                       return column,row
                   else:
                       print("Input invalid")     
            

        
    
choice = input("Select Mode NumPad or PhonePad (1 or 2) > ")
if (choice == "1"):
    board = Board(True)
    input_processor = Input_Processor(True)
elif (choice == "2"):
    board = Board(False)
    input_processor = Input_Processor(False)

    
while(not board.check_winner()):
        board.display_board()
        column,row = input_processor.input_checker("Turn " + board.player + " Select Position 1 - 9 > ")
        board.add_postion(column,row)
