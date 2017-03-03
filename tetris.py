import pygame
import time
import random
pygame.init()
clock=pygame.time.Clock()
from Block import Block
from Board import Board
from Gameplay import Gameplay
from Block2 import block2
from Block3 import block3
from Block4 import block4
from Block5 import block5
from Block6 import block6
from MagicBlock1 import MagicBlock1

gamestop=False
pygame.key.set_repeat(250,25)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
yellow=(255,255,0)
green=(0,155,0)
blue=(0,0,255)
grey=(128,128,128)
display_width=720
display_height=640
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tetris')
block_size=20
arr=[[0,1,0],[1,1,1]]
newobject=True
b=0
gameexit=False
def boxgenerator(r,i):
    if r==0:
        return Block(620,20+i,20)
    elif r==1:
        return block2(620,20+i,20)
    elif r==2:
        return block3(620,20+i,20)
    elif r==3:
        return block4(620,20+i,20)
    elif r==4:
        return block5(620,20+i,20)
    elif r==5:
        return block6(620,20+i,20)
    elif r==6:
        return MagicBlock1(620,20+i,20)
f=[]
for i in range(0,4):
    r=random.randrange(0,7)
    f.append(r)
img=pygame.image.load("hebg.png")
while not gameexit:
    gameDisplay.fill(white)
    game=Gameplay()
    board=Board()
    while not gamestop:
        gameDisplay.fill(white)
        if not game.checkRowEmpty():
            gamestop=True
        move=0
        for event in pygame.event.get():
                 if event.type==pygame.QUIT:
                     gamestop=True
                     gameexit=True
                 if event.type==pygame.KEYDOWN:
                    if event.key ==pygame.K_s:
                        b.rotate(game)
                    elif event.key ==pygame.K_a:
                        move=-20
                    elif event.key ==pygame.K_d:
                        move=20
                    elif event.key==pygame.K_SPACE:
                        gmve=True
                        while(gmve):
                             gmve=b.movedown(20,game)
                        b.moveup(20)
                 if event.type==pygame.KEYUP:
                     move=0
        if b:
            b.move(game,move)
        if newobject:
            r=random.randrange(0,7)
            f.append(r)
            r=f[0]
            del(f[0])
            if r==0:
                b=Block(300,0,20)
            elif r==1:
                b=block2(300,0,20)
            elif r==2:
                b=block3(300,0,20)
            elif r==3:
                b=block4(300,0,20)
            elif r==4:
                b=block5(300,0,20)
            elif r==5:
                b=block6(300,0,20)
            elif r==6:
                b=MagicBlock1(300,0,20)
            newobject=False
        else:
            w=b.movedown(20,game)
            if not w:
                b.moveup(20)
                #score+=10
                game.setscore(10)
                newobject=True
                b.finish(game)
                if game.getscore()%100==0:
                    game.increaselevel()
                    if game.getlevel()%3==0:
                        game.addfilledrow()
        gameDisplay.blit(pygame.transform.scale(img, (20, 620)), (0, 0))
        gameDisplay.blit(pygame.transform.scale(img, (20, 620)), (580, 0))
        gameDisplay.blit(pygame.transform.scale(img, (600, 20)), (0, 620))
        for i in range(1,29):
            for j in range(1,31):
                if (i+j)%2:
                        pygame.draw.rect(gameDisplay,grey, [i*20,j*20,block_size,block_size])

        font = pygame.font.SysFont(None, 25)
        text = font.render("Score: "+str(game.getscore()), True, black)
        gameDisplay.blit(text,(600,400))
        text2 = font.render("Level: "+str(game.getlevel()), True, black)
        gameDisplay.blit(text2,(420,0))
        game.aprint(green,gameDisplay)
        b.draw(20,gameDisplay)
        text = font.render("Next", True, black)
        gameDisplay.blit(text,(620,0))
        text = font.render("2nd Next", True, black)
        gameDisplay.blit(text,(620,100))
        text = font.render("3nd Next", True, black)
        gameDisplay.blit(text,(620,300))
        text = font.render("4nd Next", True, black)
        gameDisplay.blit(text,(620,200))
        text = font.render("Developed by", True, black)
        gameDisplay.blit(text,(600,450))
        text = font.render("Satyam", True, green)
        gameDisplay.blit(text,(620,500))
        newbox=boxgenerator(f[0],20)
        newbox.draw(20,gameDisplay)
        newbox=boxgenerator(f[1],120)
        newbox.draw(20,gameDisplay)
        newbox=boxgenerator(f[2],220)
        newbox.draw(20,gameDisplay)
        newbox=boxgenerator(f[3],320)
        newbox.draw(20,gameDisplay)

        pygame.display.update()


        rowfull=game.checkRowFull()
        score=str(game.getscore())

        while rowfull!=False:
            game.delarray(rowfull)
            game.setscore(100)
            game.increaselevel()
            pygame.display.update()
            rowfull=game.checkRowFull()
        clock.tick(game.getlevel()+2)
    gameDisplay.fill(white)
    board.message_to_screen("Game Over",red,300,300,gameDisplay)
    board.message_to_screen("Score: "+score,red,300,400,gameDisplay)
    board.message_to_screen("Type q to quit and c to replay",red,300,500,gameDisplay)
    pygame.display.update()
    for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 gameexit=True
             if event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_q:
                     gameexit=True
                 if event.key==pygame.K_c:
                     gamestop=False
