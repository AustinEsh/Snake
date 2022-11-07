import pygame
import os



class Food(object):

    def __init__(self, game):
        sourceFileDir = os.path.dirname(os.path.abspath(__file__))

        self.x_food, self.y_food = 0, 0
        self.food_coord(game)
        #self.image = pygame.image.load('img/food2.png')
        self.image = pygame.image.load(os.path.join(sourceFileDir, 'img/food2.png'))

    def food_coord(self, game):
        self.x_food, self.y_food = game.find_free_space()

    def display_food(self, game):
        game.gameDisplay.blit(self.image, (self.x_food, self.y_food))
        pygame.display.update()
