class game:
    
    def __init__(self):
        self.a = [['_','_','_'],['_','_','_'],['_','_','_']]
        self.pp = 0
        self.pc1 = 0
        self.pc2 = 0
        self.gc = 0
        self.pp1 = [0,0,0,0,0]
        self.ppc1 = 0
        self.pp2 = [0,0,0,0,0]
        self.ppc2 = 0
        self.win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]]
        self.c = 0
        self.w1 = 0
        self.w2 = 0
    def start(self):

        print("Give your position")
        print("0 1 2")
        print("3 4 5")
        print("6 7 8")
        print()

        if(self.gc%2 == 0):
            self.gc = self.gc+1
            self.pp = int(input("Enter your place on the board"))
            if(self.pp >= 0 and self.pp <= 2):
                self.a[0][self.pp] = self.pc1
                self.pp1[self.ppc1] = self.pp
                self.ppc1 = self.ppc1+1
            if(self.pp >= 3 and self.pp <= 5):
                self.a[1][self.pp - 3] = self.pc1
                self.pp1[self.ppc1] = self.pp
                self.ppc1 = self.ppc1+1
            if(self.pp >=6 and self.pp <=8):
                self.a[2][self.pp - 6] = self.pc1
                self.pp1[self.ppc1] = self.pp
                self.ppc1 = self.ppc1+1
        else:
            self.gc = self.gc+1
            self.pp = int(input("Enter your place on the board"))
            if(self.pp >= 0 and self.pp <= 2):
                self.a[0][self.pp] = self.pc2
                self.pp2[self.ppc2] = self.pp
                self.ppc2 = self.ppc2+1
            if(self.pp >= 3 and self.pp <= 5):
                self.a[1][self.pp - 3] = self.pc2
                self.pp2[self.ppc2] = self.pp
                self.ppc2 = self.ppc2+1
            if(self.pp >=6 and self.pp <=8):
                self.a[2][self.pp - 6] = self.pc2
                self.pp2[self.ppc2] = self.pp
                self.ppc2 = self.ppc2+1

        print("Current Board!")
        for i in range(0,3):
            for j in range(0,3):
                print(self.a[i][j],end = " ")
            print() 
        print()

    def input(self):
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
        
    def check(self):
        if(self.gc >= 5):
            #This is for player_1 -> check
            for i in range(0,self.ppc1-2):
                for j in range(0,8):
                    self.c = 0
                    for k in range(0,3):
                        if(i+3 <= self.ppc1):
                            for p in range(i,i+3):
                                if (self.win[j][k] == self.pp1[p]):
                                    self.c = self.c+1
                                else:
                                    continue
                            if(self.c == 3):
                                print("Player_1 Wins!")
                                self.w1 = 1
                                break
                        else:
                            break
        if(self.gc >= 6):  
            #This is for player_2 -> check
            for i in range(0,self.ppc2-2):
                for j in range(0,8):
                    self.c = 0
                    for k in range(0,3):
                        if(i+3 <= self.ppc2):
                            for p in range(i,i+3):
                                if (self.win[j][k] == self.pp2[p]):
                                    self.c = self.c+1
                                else:
                                    continue
                            if(self.c == 3):
                                print("Player_2 Wins!")
                                self.w2 = 1
                                break
                        else:
                            break                  
if __name__ == "__main__":
    g = game()
    g.input()
    c1 = 0
    while(True):
        if(c1 < 9):
            g.start()
            g.check()
            c1 = c1+1
            if(g.w1 == 1):
                break
            if(g.w2 == 1):
                break
        else:
            print("Draw!")
            break
        