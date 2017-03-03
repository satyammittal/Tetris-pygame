import pygame
import time
import random
from Block import Block;
from Board import Board;
class Gameplay(Board,Block):
        def __init__(self):
            #self.array=[[0]*30]*32
            self.array=[[0 for i in range(31)]for j in range(32)]
            self.colorarray=[[0 for i in range(31)]for j in range(32)]
            self.block_size=20
            self.__score=int(0)
            self.__level=int(1)
        def checkRowFull(self):
            test=False
            for i in range(1,31):
                test=True
                for j in range(1,29):
                    if self.array[i][j]!="X":
                        test=False
                        break
                if test:
                    return i
            return False
        def  checkRowEmpty(self):
          for i in range(1,31):
            test=True
            for j in range(1,29):
                if self.array[i][j]=="X" or self.array[i][j]=='Y':
                        test=False
                        break
            if test:
                return True
          return False
        def setscore(self,a):
            self.__score+=a
        def increaselevel(self):
            r1=random.randrange(20,200)
            r2=random.randrange(20,500)
	    if(self.array[r1/20][r2/20]=="X" or self.array[r1/20][r2/20]=="Y"):
		self.increaselevel();
	    else:
		self.__level+=1
            	self.fillpiecepos(self,r1,r2,(165,42,42))
        def getscore(self):
            return self.__score
        def getlevel(self):
            return self.__level
        def findvalue(self,x,y):
            return self.array[y/20][x/20];
        def setvalue(self,x,y,color):
            r1=x/20
            r2=y/20
            self.array[r2][r1]='X'
            self.colorarray[r2][r1]=color
        def emptyvalue(self,x,y):
            self.array[y/20][x/20]='0'
        def aprint(self,color,Gameplay):
	    dblue=(18,19,54)
            for i in range(1,29):
                for j in range(31):
                    if self.array[j][i]=="X":
                        pygame.draw.rect(Gameplay,self.colorarray[j][i], [i*20,j*20,self.block_size-1,self.block_size-1])
		    elif self.array[j][i]=="Y":
			pygame.draw.rect(Gameplay,dblue, [i*20,j*20,self.block_size-1,self.block_size-1])
        def delarray(self,i):
            del(self.array[i])
	    del(self.colorarray[i])
	    self.colorarray.insert(0,[0 for i in range(31)])
            self.array.insert(0,[0 for i in range(31)])
	def addfilledrow(self):
	    del(self.array[0])
	    del(self.colorarray[0])
	    self.colorarray.insert(30,[0 for i in range(31)])
	    self.array.insert(30,['Y' for i in range(31)])
