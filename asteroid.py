import circleshape
import constants
import pygame
import random


class Asteroid(circleshape.CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "#ffffff", self.position, self.radius, width = 2)

  def split(self, playerInstance):
    self.kill()

    playerInstance.score += self.radius // 2

    if self.radius <= constants.ASTEROID_MIN_RADIUS:
      return

    random_angle = random.uniform(20, 50)
    new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

    ast1 = Asteroid(self.position.x, self.position.y,
    new_radius)
    ast1.velocity = self.velocity.rotate(random_angle) * 1.2

    ast2 = Asteroid(self.position.x, self.position.y, new_radius)
    ast2.velocity = self.velocity.rotate(-random_angle) * 1.2

  def update(self, dt):
    self.position += self.velocity * dt
