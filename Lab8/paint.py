import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Простой Paint")

# Настройка цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLOR = BLACK

# Установка начальных координат для рисования
start_pos = None

# Основной цикл приложения
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                start_pos = None
        elif event.type == pygame.MOUSEMOTION:
            if start_pos:
                end_pos = pygame.mouse.get_pos()
                pygame.draw.line(screen, COLOR, start_pos, end_pos, 3)
                start_pos = end_pos
    
    # Обновление экрана
    pygame.display.flip()
    screen.fill(WHITE)
