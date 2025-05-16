import pygame
import sys

#initialize
pygame.init()

#display
WIDTH, HEIGHT = 600, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CLICK THE CIRCLE")

#main game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  window.fill((255,255,255))

  pygame.display.update()
