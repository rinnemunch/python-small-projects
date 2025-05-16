import pygame
import sys
import random

#initialize
pygame.init()

#display
WIDTH, HEIGHT = 600, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CLICK THE CIRCLE")

#circle
circle_radius = 30
circle_x = random.randint(circle_radius, WIDTH - circle_radius)
circle_y = random.randint(circle_radius, HEIGHT - circle_radius)

#main game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x, mouse_y = pygame.mouse.get_pos()
      distance = ((mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2) ** 0.5
      if distance <= circle_radius:
        print("HIT!")
      else:
        print("MISS!")

  window.fill((255,255,255))
  pygame.draw.circle(window, (255, 0, 0), (circle_x, circle_y), circle_radius)
  pygame.display.update()
