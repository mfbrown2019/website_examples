
from time import sleep
import os
import pygame
from pygame.locals import *

class Game():
    def __init__(self):
        self.size = 40
        self.WIDTH, self.HEIGHT = 1000, 1000
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill((0, 0, 255))
        self.grid = [[Square(i, x, 0, (0, 0, 255)) for i in range(self.size)] for x in range(self.size)]
        self.path = []
        self.TX, self.TY = self.size - 4, self.size / 2
        self.final_path = None
        self.startY = 4 
        self.startX = self.size // 2
        self.path.append(self.grid[self.startX][self.startY])


    def get_neighbors(self, y, x):

        # if y < self.size - 1 and x < self.size - 1 and self.grid[x + 1][y + 1].visited == 0: 

        #     self.path.append(self.grid[x + 1][y + 1])
        #     self.grid[x + 1][y + 1].visited = 1
        #     self.grid[x + 1][y + 1].color = (255, 255, 0)
        #     self.grid[x + 1][y + 1].lx = x
        #     self.grid[x + 1][y + 1].ly = y
        #     if self.grid[x + 1][y + 1].x == self.TX and self.grid[x + 1][y + 1].y == self.TY:
        #         return 1

        # if y > 0 and x < self.size - 1 and self.grid[x + 1][y - 1].visited == 0: 

        #     self.path.append(self.grid[x + 1][y - 1])
        #     self.grid[x + 1][y - 1].visited = 1
        #     self.grid[x + 1][y - 1].color = (255, 255, 0)
        #     self.grid[x + 1][y - 1].lx = x
        #     self.grid[x + 1][y - 1].ly = y
        #     if self.grid[x + 1][y - 1].x == self.TX and self.grid[x + 1][y - 1].y == self.TY:
        #         return 1

        # if y < self.size - 1 and x > 0 and self.grid[x - 1][y + 1].visited == 0: 

        #     self.path.append(self.grid[x - 1][y + 1])
        #     self.grid[x - 1][y + 1].visited = 1
        #     self.grid[x - 1][y + 1].color = (255, 255, 0)
        #     self.grid[x - 1][y + 1].lx = x
        #     self.grid[x - 1][y + 1].ly = y
        #     if self.grid[x - 1][y + 1].x == self.TX and self.grid[x - 1][y + 1].y == self.TY:
        #         return 1

        # if y > 0 and x > 0 and self.grid[x - 1][y - 1].visited == 0: 

        #     self.path.append(self.grid[x - 1][y - 1])
        #     self.grid[x - 1][y - 1].visited = 1
        #     self.grid[x - 1][y - 1].color = (255, 255, 0)
        #     self.grid[x - 1][y - 1].lx = x
        #     self.grid[x - 1][y - 1].ly = y
        #     if self.grid[x - 1][y - 1].x == self.TX and self.grid[x - 1][y - 1].y == self.TY:
        #         return 1    

         # UP
        if x > 0 and self.grid[x - 1][y].visited == 0: 
            self.path.append(self.grid[x - 1][y])
            self.grid[x - 1][y].visited = 1
            self.grid[x - 1][y].color = (255, 255, 0)
            self.grid[x - 1][y].lx = x
            self.grid[x - 1][y].ly = y
            if self.grid[x - 1][y].x == self.TX and self.grid[x - 1][y].y == self.TY:
                return 1
            
        # DOWN
        if x < self.size - 1 and self.grid[x + 1][y].visited == 0:  
            self.path.append(self.grid[x + 1][y])
            self.grid[x + 1][y].visited = 1
            self.grid[x + 1][y].color = (255, 255, 0)
            self.grid[x + 1][y].lx = x
            self.grid[x + 1][y].ly = y
            if self.grid[x + 1][y].x == self.TX and self.grid[x + 1][y].y == self.TY:
                return 1

         # LEFT
        if y > 0 and self.grid[x][y - 1].visited == 0: 
            self.path.append(self.grid[x][y - 1])
            self.grid[x][y - 1].visited = 1
            self.grid[x][y - 1].color = (255, 255, 0)
            self.grid[x][y - 1].lx = x
            self.grid[x][y - 1].ly = y
            if self.grid[x][y - 1].x == self.TX and self.grid[x][y - 1].y == self.TY:
                return 1

        # RIGHT
        if y < self.size - 1 and self.grid[x][y + 1].visited == 0: 
            self.path.append(self.grid[x][y + 1])
            self.grid[x][y + 1].visited = 1
            self.grid[x][y + 1].color = (255, 255, 0)
            self.grid[x][y + 1].lx = x
            self.grid[x][y + 1].ly = y
            if self.grid[x][y + 1].x == self.TX and self.grid[x][y + 1].y == self.TY:
                return 1

        return 0

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        drawing_borders = True

        while drawing_borders:
            self.grid[self.size // 2][4].color = (0, 255, 0)
            self.grid[self.size // 2][self.size - 4].color = (255, 0, 0)
            
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        drawing_borders = False



                mouse = pygame.mouse.get_pos()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    for i in range(self.size):
                        for x in range(self.size):
                            if self.grid[i][x].thing.collidepoint(mouse):
                                self.grid[i][x].color = (0, 0, 0)
                                self.grid[i][x].visited = 2
                # if pygame.mouse.get_pressed()[2]:
                #     for i in range(self.size):
                #         for x in range(self.size):
                #             if self.grid[i][x].thing.collidepoint(mouse):
                #                 self.grid[i][x].color = (0, 0, 255)
                #                 self.grid[i][x].visited = 0

            for i in range(self.size):
                for x in range(self.size):
                    pygame.draw.rect(self.screen, self.grid[i][x].color, self.grid[i][x].dimension)

            pygame.display.update()

        for spot in self.path:
            # sleep()
            # print(spot.x, spot.y)
            self.grid[self.size // 2][4].color = (0, 255, 0)
            self.grid[self.size // 2][self.size - 4].color = (255, 0, 0)
            for i in range(self.size):
                for x in range(self.size):
                    pygame.draw.rect(self.screen, self.grid[i][x].color, self.grid[i][x].dimension)
            pygame.display.update()
            final = g.get_neighbors(spot.x,spot.y)
            if final == 1:
                self.final_path = self.path[len(self.path) - 1]
                break

        final = []
        while True:
            if self.final_path.lx == self.startX and self.final_path.ly == self.startY:
                break
            else:
                final.append([self.final_path.lx, self.final_path.ly])
                # print(path.lx, path.ly)
                self.final_path = self.grid[self.final_path.lx][self.final_path.ly]
                # print(path.lx, path.ly)
        # print(final)
        for i in range(self.size):
            for x in range(self.size):
                temp = [i, x]
                if temp in final:
                    self.grid[i][x].color = (0, 255, 100)
        last = True
        while last:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        last = False
            self.grid[self.size // 2][4].color = (0, 255, 0)
            self.grid[self.size // 2][self.size - 4].color = (255, 0, 0)
            for i in range(self.size):
                for x in range(self.size):
                    pygame.draw.rect(self.screen, self.grid[i][x].color, self.grid[i][x].dimension)
            pygame.display.update()


class Square():
    def __init__(self, x, y, visited, color):
        # ! FOR PYGAME
        self.size = 25
        self.color = color

        # ! FOR THE ACTUAL PAATH
        self.visited = visited
        self.x = x
        self.y = y
        self.lx = 0
        self.ly = 0

        # ! Pygame rect init
        self.dimension = (0 + self.size * self.x, 0 + self.size * self.y, self.size, self.size)
        self.thing = pygame.Rect(self.dimension)




g = Game()
g.run()









