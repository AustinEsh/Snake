import pygame
from DQNagent import DQNAgent
from GAagent import GAAgent
import numpy as np
import utils
import keyboard
from Game import Game
from Food import Food
from Player import Player
import os

# importing modules del snake.
# use os functions for file paths
# install varios modules via pip
# change dimensions to units in add model dense kwargs
# game speed? // add pygame.event.get / default speed 300
# game record??
# save animation in utils, line 66 below


def run_snake():
    pygame.init()
    pygame.font.init()
    game = Game(20, 20)

    snake_green = Player(game, "green", ai="heuristic")
    game.player.append(snake_green)

    game.food.append(Food(game))
    sourceFileDir = os.path.dirname(os.path.abspath(__file__))

    ga_agent = GAAgent(population_name="standard_population", generation=100)

    game.game_speed = 0  # parameter: game speed
    game.display_option = True  # parameter: show game
    record = True  # parameter: True if recording the game
    frames = []

    while not keyboard.is_pressed('s'):
        for i in range(len(game.player)):
            move = game.player[i].select_move(game)
            game.player[i].do_move(move, game)
            if game.player[i].crash:
                game.player[i].init_player(game)

        if game.display_option:
            game.display()
            pygame.time.wait(game.game_speed)
            pygame.event.get() # add
            if record:
                data = pygame.image.tostring(game.gameDisplay, 'RGBA')
                from PIL import Image
                img = Image.frombytes('RGBA', (game.game_width, game.game_height + 100), data)
                img = img.convert('RGB')
                frames.append(np.array(img))
    #utils.save_animation(frames, 'videos/snake.mp4', 25)
    sourceFileDir = os.path.dirname(os.path.abspath(__file__))
    utils.save_animation(frames, (os.path.join(sourceFileDir,'videos/snake.mp4')), 25)
    for i, snake in enumerate(game.player):
        print("Snake" + str(i+1) + " Max score: " + str(snake.record) +
              ", Avg Score: " + str(snake.total_score / snake.deaths) +
              ", Deaths: " + str(snake.deaths))


if __name__ == "__main__":
    run_snake()
