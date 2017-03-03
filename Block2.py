import pygame
import time
import random
from Block import Block;
from Board import Board;
class block2(Block):
    def __init__(self,a,b,bs):
        self.x1=a
        self.x2=a+bs
        self.x3=a+2*bs
        self.x4=a+3*bs
        self.leftx=a
        self.y1=b
        self.y2=b
        self.y3=b
        self.y4=b
        self.lefty=b
        self.array=[[1,1,1,1]]
        self.color=(0,0,255)
