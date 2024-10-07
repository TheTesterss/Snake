import time
import pygame as game
import random
from Player import Player

class Game:
    def __init__(self):
        self.__board_size = 16
        self.__x = 1920
        self.__y = 1080
        self.__running = False
        self.__clock = None
        self.__screen = None
        self.__interface = None
        self.player = None

    def runningState(self):
        while self.__running:
            for event in game.event.get():
                if event.type == game.QUIT:
                    running = False
                elif event.type == game.KEYDOWN:
                    if event.key == game.K_z:
                        self.player.setDirection("up")
                    elif event.key == game.K_q:
                        self.player.setDirection("left")
                    elif event.key == game.K_s:
                        self.player.setDirection("down")
                    elif event.key == game.K_d:
                        self.player.setDirection("right")
                    
            self.__clock.tick(60)
            background = game.image.load("./images/clouds.jpg")
            resized = game.transform.scale(background, (self.__x, self.__y))
            self.__screen.blit(resized, (0, 0))
            
            self.interface()
            if self.player and self.player.isAlive():
                self.player.move(self.lostWindow, self.__interface)
            game.display.flip()
            
    def interface(self):
        info = game.display.Info()
        back_size = (info.current_w, info.current_h)
        
        self.__interface = game.Surface((back_size[0]//3, back_size[1]//1.5))
        self.__interface.fill((165, 232, 93))
        if not self.player:
            self.player = Player(self.__board_size, self.__interface.get_width() // self.__board_size, self.__screen)

        self.createTiles()
        self.player.draw(self.__interface)
        interface_x = (back_size[0] - back_size[0]//3) // 2
        interface_y = (back_size[1] - back_size[1]//1.1)
        game.draw.rect(surface=self.__interface, rect=self.__interface.get_rect(), color=(0, 0, 0), width=2) 
        self.__screen.blit(self.__interface, (interface_x, interface_y))
        
        
    def createTiles(self):
        tile_size_x = self.__interface.get_width() // self.__board_size
        tile_size_y = self.__interface.get_height() // self.__board_size

        for row in range(self.__board_size):
            for column in range(self.__board_size):
                tile = game.Surface((tile_size_x, tile_size_y))
                tile_rect = tile.get_rect(topleft=(column * tile_size_x, row * tile_size_y + self.__interface.get_height()*0.2))
                game.draw.rect(surface=tile, rect=tile.get_rect(), color=(165, 232, 93) if (row+column)%2==0 else (82, 169, 7)) 
                self.__interface.blit(tile, (tile_rect.x, tile_rect.y))  
    
    def lostWindow(self):
        surface = game.Surface((400, 200))
        surface.fill((255, 0, 0))
        font = game.font.Font(None, 74)
        text = font.render("Tu as perdu", True, (255, 255, 255))
        text_rect = text.get_rect(center=(200, 100))
        surface.blit(text, text_rect)

        self.__screen.blit(surface, (self.__x // 2 - 200, self.__y // 2 - 100))
        game.display.flip()

        time.sleep(3)
        self.__running = False

    def start(self):
        game.init()
        self.__screen = game.display.set_mode((self.__x, self.__y))
        self.__clock = game.time.Clock()
        
        self.__running = True
        self.runningState()



Game().start()