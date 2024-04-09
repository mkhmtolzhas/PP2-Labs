# import pygame
# import sys
# from datetime import datetime

# pygame.init()

# WIDTH, HEIGHT = 400, 400
# WINDOW_SIZE = (WIDTH, HEIGHT)
# screen = pygame.display.set_mode(WINDOW_SIZE)
# pygame.display.set_caption("Часы")

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# def draw_clock():
#     current_time = datetime.now().strftime("%H:%M:%S")
#     font = pygame.font.SysFont(None, 50)
#     text = font.render(current_time, True, WHITE)
#     screen.blit(text, (150, 150))


# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill(BLACK)
#     draw_clock()
#     pygame.display.update()

#     pygame.time.delay(1000)

# pygame.quit()
# sys.exit()

# import pygame
# import sys
# import math
# from datetime import datetime

# # Инициализация Pygame
# pygame.init()

# # Установка размеров окна
# WIDTH, HEIGHT = 400, 400
# WINDOW_SIZE = (WIDTH, HEIGHT)
# screen = pygame.display.set_mode(WINDOW_SIZE)
# pygame.display.set_caption("Обычные часы")

# # Цвета
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)

# # Функция для отрисовки циферблата
# def draw_clock_face():
#     pygame.draw.circle(screen, BLACK, (WIDTH // 2, HEIGHT // 2), 150, 2)
#     for i in range(1, 13):
#         angle = math.radians(i * 30)
#         x = int(WIDTH // 2 + 130 * math.cos(angle))
#         y = int(HEIGHT // 2 + 130 * math.sin(angle))
#         pygame.draw.circle(screen, BLACK, (x, y), 5)

# # Функция для отрисовки стрелок
# def draw_hands():
#     current_time = datetime.now()
#     hour = current_time.hour % 12  # Приводим к 12-часовому формату
#     minute = current_time.minute
#     second = current_time.second

#     # Часовая стрелка
#     hour_angle = math.radians((hour * 30) + (minute / 2))
#     hour_length = 70
#     pygame.draw.line(screen, BLACK, (WIDTH // 2, HEIGHT // 2), (WIDTH // 2 + hour_length * math.cos(hour_angle),
#                                                                HEIGHT // 2 + hour_length * math.sin(hour_angle)), 6)

#     # Минутная стрелка
#     minute_angle = math.radians(minute * 6)
#     minute_length = 100
#     pygame.draw.line(screen, BLACK, (WIDTH // 2, HEIGHT // 2), (WIDTH // 2 + minute_length * math.cos(minute_angle),
#                                                                HEIGHT // 2 + minute_length * math.sin(minute_angle)), 3)

#     # Секундная стрелка
#     second_angle = math.radians(second * 6)
#     second_length = 120
#     pygame.draw.line(screen, RED, (WIDTH // 2, HEIGHT // 2), (WIDTH // 2 + second_length * math.cos(second_angle),
#                                                              HEIGHT // 2 + second_length * math.sin(second_angle)), 1)

# # Основной цикл игры
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill(WHITE)
#     draw_clock_face()
#     draw_hands()
#     pygame.display.update()

#     pygame.time.delay(1000)  # Задержка 1 секунда

# pygame.quit()
# sys.exit()



# import pygame

# pygame.init()

# WIDTH, HEIGHT = 400, 400
# WINDOW_SIZE = (WIDTH, HEIGHT)
# screen = pygame.display.set_mode(WINDOW_SIZE)
# pygame.display.set_caption("Часы")

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# pygame.Rect(50, 50, 50, 50)

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.K_0:
#             r = re

# import pygame

# pygame.init()
# screen = pygame.display.set_mode((400, 300))
# done = False
# is_blue = True
# x = 30
# y = 30

# while not done:
#         for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                         done = True
#                 if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#                         is_blue = not is_blue
        
#         pressed = pygame.key.get_pressed()
#         if pressed[pygame.K_UP]: y -= 3
#         if pressed[pygame.K_DOWN]: y += 3
#         if pressed[pygame.K_LEFT]: x -= 3
#         if pressed[pygame.K_RIGHT]: x += 3
        
#         if is_blue: color = (0, 128, 255)
#         else: color = (255, 100, 0)
#         pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
#         pygame.display.flip()



import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()
        clock.tick(60)