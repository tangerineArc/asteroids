import circleshape
import constants
import pygame
import shot
import sys


class Player(circleshape.CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, constants.PLAYER_RADIUS)

    self.rotation = 0
    self.cooldown = 0
    self.score = 0
    self.lives = constants.PLAYER_LIVES

  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]

  def get_score_surface(self, font):
    return font.render(f"SCORE: {self.score}", True, "#ffffff")

  def get_lives_surface(self, font):
    return font.render(f"LIVES: {self.lives}", True, "#ffffff")

  def draw(self, screen):
    pygame.draw.polygon(screen, "#ffffff", self.triangle(), width = 2)

  def rotate(self, dt):
    self.rotation += constants.PLAYER_TURN_SPEED * dt

  def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * constants.PLAYER_SPEED * dt

  def shoot(self):
    if self.cooldown > 0:
      return

    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    sht = shot.Shot(self.position.x, self.position.y)
    sht.velocity = forward * constants.PLAYER_SHOOT_SPEED

    self.cooldown = constants.PLAYER_SHOOT_COOLDOWN

  def die(self):
    if self.lives > 0:
      self.lives -= 1

    if self.lives == 0:
      print("Game over!")
      sys.exit()

  def re_spawn(self):
    self.rotation = 0
    self.velocity = pygame.Vector2(0, 0)
    self.cooldown = 0
    self.position = pygame.Vector2(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

  def update(self, dt):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
      self.rotate(-dt)
    if keys[pygame.K_d]:
      self.rotate(dt)

    if keys[pygame.K_w]:
      self.move(dt)
    if keys[pygame.K_s]:
      self.move(-dt)

    if keys[pygame.K_SPACE]:
      self.shoot()

    self.cooldown -= dt
