import pygame
import os
from Main_Menu.main_menu import MainMenu

if __name__ == "__main__":
    pygame.init()
    icon = pygame.image.load(os.path.join("assets", "logo.png"))
    icon = pygame.transform.scale(icon, (32, 32))
    pygame.display.set_icon(icon)
    pygame.display.set_caption("EnemyDefense")
    window = pygame.display.set_mode((1000, 700))
    mainMenu = MainMenu(window, 1000, 700)
    mainMenu.run()