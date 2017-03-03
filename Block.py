import pygame
import time
import random
class Block(object):
    def __init__(self,a,b,bs):
        self.x1=a
        self.x2=a+bs
        self.x3=a
        self.x4=a+bs
        self.leftx=a
        self.y1=b
        self.y2=b
        self.y3=b+bs
        self.y4=b+bs
        self.lefty=b
        self.array=[[1,1],[1,1]]
        red=(255,0,0)
        self.color=red

    def draw(self,block_size,gameDisplay):
        pygame.draw.rect(gameDisplay,self.color, [self.x1,self.y1,block_size-1,block_size-1])
        pygame.draw.rect(gameDisplay,self.color, [self.x2,self.y2,block_size-1,block_size-1])
        pygame.draw.rect(gameDisplay,self.color, [self.x3,self.y3,block_size-1,block_size-1])
        pygame.draw.rect(gameDisplay,self.color, [self.x4,self.y4,block_size-1,block_size-1])
    def moveleft(self,bs):
        self.x1-=bs
        self.x2-=bs
        self.x3-=bs
        self.x4-=bs
        self.leftx-=bs
    def moveRight(self,bs):
        self.x1+=bs
        self.x2+=bs
        self.x3+=bs
        self.x4+=bs
        self.leftx+=bs
    def movedown(self,bs,game):
        self.y1+=bs
        self.y2+=bs
        self.y3+=bs
        self.y4+=bs
        self.lefty+=bs
        return self.check(game);
    def check(self,game):
        if self.y1>=620 or self.y2>=620 or self.y3>=620 or self.y4>=620:
            return False
        elif((game.findvalue(self.x1,self.y1)!="X" and game.findvalue(self.x2,self.y2)!="X" and game.findvalue(self.x3,self.y3)!="X" and game.findvalue(self.x4,self.y4)!="X")and (game.findvalue(self.x1,self.y1)!="Y" and game.findvalue(self.x2,self.y2)!="Y" and game.findvalue(self.x3,self.y3)!="Y" and game.findvalue(self.x4,self.y4)!="Y")):
            return True
        else:
            return False
    def moveup(self,bs):
        self.y1-=bs
        self.y2-=bs
        self.y3-=bs
        self.y4-=bs
        self.lefty-=bs

    def set(self,a,b,c,d,e,f,g,h):
        self.x1=a
        self.x2=b
        self.x3=c
        self.x4=d
        self.y1=e
        self.y2=f
        self.y3=g
        self.y4=h
    def finish(self,game):
        game.setvalue(self.x1,self.y1,self.color)
        game.setvalue(self.x2,self.y2,self.color)
        game.setvalue(self.x3,self.y3,self.color)
        game.setvalue(self.x4,self.y4,self.color)
    def rotate(self,game):
        rx1=self.x1
        rx2=self.x2
        rx3=self.x3
        rx4=self.x4
        ry1=self.y1
        ry2=self.y2
        ry3=self.y3
        ry4=self.y4
        self.array=list(reversed(zip(*(self.array))))
        con=0
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                if self.array[i][j]==1 and con==0:
                    self.x1=self.leftx+20*i
                    self.y1=self.lefty+20*j
                    con=con+1
                elif self.array[i][j]==1 and con==1:
                    self.x2=self.leftx+20*i
                    self.y2=self.lefty+20*j
                    con=con+1
                elif self.array[i][j]==1 and con==2:
                    self.x3=self.leftx+20*i
                    self.y3=self.lefty+20*j
                    con=con+1
                elif self.array[i][j]==1 and con==3:
                    self.x4=self.leftx+20*i
                    self.y4=self.lefty+20*j
                    con=con+1
        self.leftx=self.x1
        self.lefty=self.y1
        if(self.check(game)==False):
            self.x1=rx1;
            self.x2=rx2;
            self.x3=rx3;
            self.x4=rx4;
            self.y1=ry1;
            self.y2=ry2;
            self.y3=ry3;
            self.y4=ry4;

    def move(self,game,movel):
        u1=self.x1+movel
        u2=self.x2+movel
        u3=self.x3+movel
        u4=self.x4+movel
        u5=self.leftx+movel
        if not ( u1<20 or u1>=580 or u2<20 or u2>=580 or u3<20 or u3>=580 or u4<20 or u4>=580 or game.findvalue(u1,self.y1)=="X" or game.findvalue(u2,self.y2)=="X" or game.findvalue(u3,self.y3)=="X" or game.findvalue(u4,self.y4)=="X"):
            self.x1=u1
            self.x2=u2
            self.x3=u3
            self.x4=u4
            self.leftx=u5
    def moveleft(self):
        self.x1-=bs
        self.x2-=bs
        self.x3-=bs
        self.x4-=bs
        self.leftx-=bs
