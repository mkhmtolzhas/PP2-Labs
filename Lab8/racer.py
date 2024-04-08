import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

clock = pygame.time.Clock()

class Car:
    def __init__(self) -> None:
        self.positon = [1, 2, 3]
        self.image = pygame.image.load("car.png")
        self.image = pygame.transform.scale(pygame.image.load("car.png"), (800 / 3, 800 / 3))


running = True

car = Car()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(car.image, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()