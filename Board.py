import pygame
import time
import random
class Board(object):
    @staticmethod
    def checkPiece(self,x,y):
        #arrayv=game.value(x,y)
        if(arrayv=='X'):
            return False
        else:
            return True
    @staticmethod
    def fillpiecepos(self,x,y,color):
        #game.setvalue(x,y)
            r1=x/20
            r2=y/20
            self.array[r2][r1]='X'
            self.colorarray[r2][r1]=color
    def message_to_screen(self,msg,color,display_width,display_height,gameDisplay):
        font=pygame.font.SysFont(None,25)
        screen_text=font.render(msg,True,color)
        gameDisplay.blit(screen_text,[display_width/2,display_height/2])
