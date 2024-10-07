import pygame as game
import time

class Player:
    def __init__(self, board_size, tile_size, screen):
        self.__board_size = board_size
        self.__tile_size = tile_size
        self.__screen = screen
        # Snake textures
        self.__image = game.image.load('./images/snake.png')
        self.__image = game.transform.scale(self.__image, (tile_size, tile_size))
        
        self.__direction = "right"
        self.__rotated = False
        self.__alive = True
        self.__blocks = [[2, 3]]

    def draw(self, surface):
        for block in self.__blocks:
            head_x = block[0] * self.__tile_size + surface.get_width()*0.01
            head_y = block[1] * self.__tile_size + surface.get_height()*0.24
            if self.__direction in ["down", "up"] and not self.__rotated:
                self.__image = game.transform.rotate(self.__image, 90)
                self.__rotated = True
            elif self.__direction in ["left", "right"] and self.__rotated:
                self.__image = game.transform.rotate(self.__image, 90)
                self.__rotated = False
            surface.blit(self.__image, (head_x, head_y))
            
    def move(self, lostWindow, surface):
        blocks = []
        for block in self.__blocks:
            if self.__direction == "right":
                if block[0]+1 > self.__board_size-1:
                    lostWindow()
                else:
                    blocks.append([block[0]+1, block[1]])
            elif self.__direction == "left":
                if block[0]-1 < -1:
                    lostWindow()
                else:
                    blocks.append([block[0]-1, block[1]])
            elif self.__direction == "up":
                if block[1]-1 < -1:
                    lostWindow()
                else:
                    blocks.append([block[0], block[1]-1])
            elif self.__direction == "down":
                if block[1]+1 > self.__board_size-1:
                    lostWindow()
                else:
                    blocks.append([block[0], block[1]+1])
        self.draw(surface=surface)
        time.sleep(0.2)
        self.__blocks = blocks
            
    def setDirection(self, direction):
        self.__direction = direction
        
    def isAlive(self):
        return self.__alive