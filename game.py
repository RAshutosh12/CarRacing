import pygame
import time

pygame.init()
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
grey=(105,105,105)
green=(0,255,0)
width=800
height=600
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption(' CAR RACING  ') 
clock=pygame.time.Clock()

font = pygame.font.SysFont(None,30)

def score_board(msg,color):
    score_1=font.render(msg,True,color)
    gameDisplay.blit(score_1,[700,200])
    pygame.display.update()

def message_to_screen(msg,color):
    gameDisplay.fill(white)
    screen_text=font.render(msg,True,color)
    gameDisplay.blit(screen_text,[200,300])
    pygame.display.update()
  

def gameloop():
    gameExit=False
    gameOver=False
    score=0
    car_x=300
    car_y=420
    har_x=300
    har_y=0
    har_x1=500
    har_y1=350
    har_y_change1=0
    har_y_change=0
    x_change=0
    y_change=0
     

    while not gameExit:

        while gameOver ==True:
            message_to_screen("Score: "+str(score)+"    game over , press c to play and quit to q",black)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key==pygame.K_c:
                        gameloop()
            
        for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 gameExit=True
             if event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_LEFT:
                     x_change=-1
                     har_y_change=2
                     har_y_change1=2
                 elif event.key==pygame.K_RIGHT:
                     x_change= 1
                     har_y_change=2
                     har_y_change1=2 
                  
        if car_x ==510 or car_x ==200:
            gameOver = True  
            
        if har_y == 300:
            har_y1 = 0
            score = score+1
                
        if har_y1 == 300:
            har_y = 0
            score = score+1

        
        if((har_y+30<=560) and (har_y+30>=420)) or ((har_y-30<=560) and (har_y-30>=420)) :
            if(car_x<=340 ):
                 time.sleep(2)
                 gameOver = True

        if((har_y1+30<=560) and (har_y1+30>=420)) or ((har_y1-30<=560) and (har_y1-30>=420)) :
            if(car_x+100>=460 ):
                 time.sleep(2)
                 gameOver = True     

        car_x += x_change
        har_y += har_y_change
        har_y1 += har_y_change1
        gameDisplay.fill(green)
        
           
        pygame.draw.rect(gameDisplay,grey,[200,0,400,600])

        pygame.draw.circle(gameDisplay,(0,0,0),(har_x,har_y),(60))

        pygame.draw.circle(gameDisplay,(0,0,0),(har_x1,har_y1),(60))

        pygame.draw.rect(gameDisplay,red,[car_x,car_y,100,140])

        score_board("score\n  "+str(score) ,grey)
        
        pygame.display.update()
        
        clock.tick(3000)
        
 
    pygame.quit()
    quit()

gameloop()
