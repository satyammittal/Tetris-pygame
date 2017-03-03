import pygame
import time
import random
from Block import Block;
class block4(Block):
    def __init__(self,a,b,bs):
         self.x1=a
         self.x2=a+bs
         self.x3=a
         self.x4=a-bs
         self.leftx=a-bs
         self.y1=b+bs
         self.y2=b+bs
         self.y3=b
         self.y4=b+bs
         self.lefty=b
         self.array=[[0,1,0],[1,1,1]]
         self.color=(0,0,0)
