import pygame


pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill("blue")

  pygame.display.flip()

  clock.tick(60)

pygame.quit()











class Player:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.velocity = 0

  def draw(self):
    screen.blit(player_img, (self.x, self.y))

#Load Player
pygame.image.load('player.png').convert()
