import pygame,sys
from pygame.locals import *  
from prueba import Game
from prueba import Scores

pygame.init()

Playing = True
pygame.display.set_caption ("PPT: The Game")
Pantalla = pygame.display.set_mode((600, 600))



icono = pygame.image.load("Imgs/lilpic.png")
fondo = pygame.image.load("Imgs/fondo.jpg")
Start_Img_1 = pygame.image.load("Imgs/start1.png").convert_alpha()
Start_Img_2 = pygame.image.load("Imgs/start2.png").convert_alpha()
Exit_Img_1 = pygame.image.load("Imgs/Exit1.png").convert_alpha()
Exit_Img_2 = pygame.image.load("Imgs/Exit2.png").convert_alpha()
Score_Img_1 = pygame.image.load("Imgs/Score1.png").convert_alpha()
Score_Img_2 = pygame.image.load("Imgs/Score2.png").convert_alpha()


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int( height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.click = False

    def draw(self):

        Acción = False
        Pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(Pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                Acción = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False


        Pantalla.blit(self.image, (self.rect.x, self.rect.y))
        return Acción



Start_Button = Button(70, 405, Start_Img_1, 0.6)
Exit_Button = Button(400, 400, Exit_Img_1, 0.6)
Score_Button = Button(250, 500, Score_Img_1, 0.6)


while Playing: 
 
    pygame.display.set_icon(icono)
    Pantalla.blit(fondo,(0,0))


    colour = (0, 0, 0)
    font1 = pygame.font.Font(None, 200)
    font2 = pygame.font.Font(None, 80)
    Mi_fuente = pygame.font.SysFont("Lucida", 120)
    location1 = (55, 70)
    location2 = (205, 200)
    Pantalla.blit(font1.render("PPT:", True,
    colour), location1)
    Pantalla.blit(font2.render("THE GAME", True,
    colour), location2)


    ##Click botones
    if Start_Button.draw() == True:
        Start_Button = Button(70, 405, Start_Img_2, 0.6)
        print ("aaaaaaaaaaaaa")
        a = 1
        while a == 1:
            print (" ")
            Start_Button = Button(70, 405, Start_Img_1, 0.6)
            a = 0
        
        Start_Button.draw() == False
        if Start_Button.draw() == False: 
            Game()
               
            
    if Exit_Button.draw() == True:
        Exit_Button = Button(396, 401, Exit_Img_2, 0.6)
        print ("Pa' fuera, mi loco XDDD")
        Exit_Button.draw() == False
        if Exit_Button.draw() == False:
            Exit_Button = Button(400, 400, Exit_Img_1, 0.6)
            Playing = False


    if Score_Button.draw() == True: 
        a = 1
        while a == 1:
            Score_Button = Button(250, 500, Score_Img_2, 0.6)
            a = 0
        Score_Button.draw() == False
        if Exit_Button.draw() == False:
            Score_Button = Button(250, 500, Score_Img_1, 0.6)
        Scores()
        input("Press ENTER to continue")
        
    


    for evento in pygame.event.get():            
            if evento.type == QUIT:                 
                pygame.quit()                         
                sys.exit()           
    pygame.display.update()  
