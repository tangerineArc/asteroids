import constants
import player
import pygame


def main():
  print("Starting Asteroids!")
  print(f"Screen width: {constants.SCREEN_WIDTH}")
  print(f"Screen height: {constants.SCREEN_HEIGHT}")

  pygame.init()

  clock = pygame.time.Clock()
  dt = 0

  screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

  p = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    screen.fill("#000000")

    p.draw(screen)
    p.update(dt)

    pygame.display.flip()

    dt = clock.tick(60) / 1000


if __name__ == "__main__":
  main()
