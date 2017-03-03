import pygame
import time
import random
from Block import Block;
class MagicBlock1(Block):
    def __init__(self,a,b,bs):
         self.x1=a
         self.leftx=a
         self.y1=b
         self.lefty=b
         self.array=[[1,0,0],[0,0,0]]
         gold=(255,215,0)
         self.color=gold
    def draw(self,block_size,gameDisplay):
        pygame.draw.rect(gameDisplay,self.color, [self.x1,self.y1,block_size,block_size])
    def moveleft(self,bs):
        self.x1-=bs
    def moveRight(self,bs):
        self.x1+=bs
        self.leftx+=bs
    def movedown(self,bs,game):
        self.y1+=bs
        self.lefty+=bs
        return self.check(game);
    def check(self,game):
        if self.y1>=620 :
            return False
        elif((game.findvalue(self.x1,self.y1)!="X")):
            return True
        else:
            return False
    def moveup(self,bs):
        self.y1-=bs
        self.lefty-=bs

    def set(self,a,b,c,d,e,f,g,h):
        self.x1=a
    def finish(self,game):
        game.delarray((self.y1+20)/20)
    def rotate(self,game):
        return True

    def move(self,game,movel):
        u1=self.x1+movel
        u5=self.leftx+movel
        if not ( u1<20 or u1>=580 or game.findvalue(u1,self.y1)=="X"):
            self.x1=u1
            self.leftx=u5
    def moveleft(self):
        self.x1-=bs
        self.leftx-=bs
