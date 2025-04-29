import asteroid
import asteroidfield
import constants
import player
import pygame
import shot
import sys


def main():
  print("Starting Asteroids!")
  print(f"Screen width: {constants.SCREEN_WIDTH}")
  print(f"Screen height: {constants.SCREEN_HEIGHT}")

  pygame.init()

  clock = pygame.time.Clock()
  dt = 0

  screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

  score_font = pygame.font.Font(size = 32)

  updatable_group = pygame.sprite.Group()
  drawable_group = pygame.sprite.Group()
  asteroid_group = pygame.sprite.Group()
  shot_group = pygame.sprite.Group()

  player.Player.containers = (updatable_group, drawable_group)

  asteroid.Asteroid.containers = (asteroid_group, updatable_group, drawable_group)

  asteroidfield.AsteroidField.containers = (updatable_group)

  shot.Shot.containers = (shot_group, updatable_group, drawable_group)

  p = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

  asteroidfield.AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    screen.fill("#000000")

    updatable_group.update(dt)

    for ast in asteroid_group:
      if ast.collide(p):
        print("Game over!")
        sys.exit()

      for sht in shot_group:
        if ast.collide(sht):
          sht.kill()
          ast.split(p)

    for drawable in drawable_group:
      drawable.draw(screen)

    screen.blit(p.get_score_surface(score_font), (20, 20))

    pygame.display.flip()

    dt = clock.tick(60) / 1000


if __name__ == "__main__":
  main()
