# Работа с графической библиотекой для игр и окон
# python -m pip install --user --upgrade pip    - Обновление пакета pip
# python -m pip install --user pygame           - Установка библиотеки PyGame
# import pygame.examples.stars                  - Примеры игр
# pygame.examples.stars.main()

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

    while True:
        pygame.display.flip()