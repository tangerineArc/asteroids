import circleshape
import constants
import pygame


class Shot(circleshape.CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, constants.SHOT_RADIUS)

  def draw(self, screen):
    pygame.draw.circle(screen, "#ffffff", self.position, self.radius, width = 2)

  def update(self, dt):
    self.position += self.velocity * dt
