import pygame

pygame.init()

SIZE = (400, 400)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Idk")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.KEYDOWN:
        #     if 
    

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (200, 200), 50)
    pygame.display.flip()

pygame.quit()