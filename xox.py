import random
class Game:

    def __init__(self): #ToInitilizeAllVariable

        self.p1 = 0    #CurrentPlayerPosition
        self.p2 = 0    #CurrentPlayerPosition

        self.pb = [100,100,100,100,100,100,100,100,100]  #PositionsTakenOnBoard

        self.c = 0 #PlayerCounter

        self.c1 = 0 #Player1Counter - To input at correct location of wc1
        self.c2 = 0 #Player2Counter - To input at correct location of wc2

        self.br = [['_','_','_'],['_','_','_'],['_','_','_']]

        self.wc1 = [100,100,100,100,100,100]    #ToCheckWinForPlayer1
        self.wc2 = [100,100,100,100,100,100]    #ToCheckWinForPlayer2

        self.win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]]    #winCombinations

        self.bc = 0

    def input(self):    #ToGetTheIdentityInput(x or o)
        print("Player_1 make your choice")
        print("x")
        print("o")
        self.pc1 = str(input("Enter your choice"))
        if(self.pc1 == 'x'):
            self.pc2 = 'o'
            print("Player_2 is assigned o")
            print()
        else:
            self.pc2 = 'x'
            print("Player_2 is assigned x")
            print()

    def start1(self):   #ToGetThePlayer1CurrentInputAnd_UpDateItOnBoard
        print("0  1  2")
        print("3  4  5")
        print("6  7  8")
        print()
        self.p1 = int(input("Enter the position Player1__"))

        Game.recheck1(self) #CallingRecheck
    
    def recheck1(self): #ToCheckRepetationInentry
        if (self.p1 in self.pb):
            print("Repeated Entry!,Player1 Enter Again")
            Game.start1(self)
        else:
            self.pb[self.c] = self.p1
            self.c = self.c + 1
            self.wc1[self.c1] = self.p1
            self.c1 = self.c1 + 1
            self.bc = self.bc + 1
            print("Board Counter",self.bc)
            Game.display(self,self.p1,self.pc1)

    def start2(self):   #ToGetThePlayer1CurrentInputAnd_UpDateItOnBoard
        print("0  1  2")
        print("3  4  5")
        print("6  7  8")
        print()
        self.p2 = int(input("Enter the position Player2__"))
        Game.recheck2(self)

    def recheck2(self): #ToCheckRepetationInEntry
        if (self.p2 in self.pb):
            print("Repeated_Entry!,Player2 Enter Again")
            print()
            Game.start2(self)
        else:
            self.pb[self.c] = self.p2
            self.c = self.c + 1
            self.wc2[self.c2] = self.p2
            self.c2 = self.c2 + 1
            self.bc = self.bc + 1
            print("Board Counter",self.bc)
            Game.display(self,self.p2,self.pc2)

    #p - Positing of player1/2
    #c - It is the identity of player1/2(*/o)

    def display(self,p,c): #ToDisplayCurrentBoard
        #Updating the board profile
        if p >= 0 and p <=2:
	        self.br[0][p] = c
        elif p >= 3 and p <=5:
	        self.br[1][(p-3)] = c
        else:
	        self.br[2][(p-6)] = c
        
        #Printing the board
        for i in range(0,3):
            for j in range(0,3):
                print(self.br[i][j],end = "  ")
            print()    

    #wc = Contains positions of player1 or player2

    def check(self,pc,wc):    #ToCheckTheWin
        c = 0
        for i in self.win:
	        c1 = 0
	        for j in range(0, len(wc)):
		        if (wc[j] in i):
			        c = c + 1
			        c1 = c1 + 1
		        else:
			        c1 = c1+1
	        if (c == 3):
		        return(1)
	        else:
		        c = 0
        return 0

if __name__ == "__main__":
    g = Game()
    g.input()
    c = 0
    while(True):
        g.start1()
        p = g.check(g.pc1,g.wc1)
        if(p == 1):
            print("Player1 Won the Game!")
            break
        if(g.bc == 9):
            print("Draw!")
            break 
        g.start2()
        p = g.check(g.pc2,g.wc2)
        if (p == 1):
            print("Player2 Won the Game!")
            break
        if(g.bc == 9):
            print("Draw!")
            break 

