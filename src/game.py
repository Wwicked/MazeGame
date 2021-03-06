import pygame
from src.player import Player
from src.popup import Popup


class Game:
    def __init__(self, cfg):
        self.cfg = cfg
        self.window = None
        self.level = None
        self.player = Player(self.cfg, self)
        self.in_menu = False
        self.menu = None
        self.is_popup_open = False

        pygame.init()
        pygame.display.set_caption(self.cfg.window_title)

        bs = self.cfg.block_size
        maze = self.cfg.maze
        size = (bs * len(maze[0]), bs * len(maze))

        self.window = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

    def set_menu(self, menu):
        self.in_menu = True if menu is not None else None
        self.menu = menu

    def set_popup(self, status, **options):
        self.is_popup_open = status

        if status:
            self.popup = Popup(**options)
        else:
            self.popup = None

    def draw(self) -> None:
        if self.in_menu:
            self.menu.draw(self.window)

        else:
            self.level.draw(self.window)
            self.player.draw(self.window)

        if self.is_popup_open:
            self.popup.draw(self.window)

    def event(self, e) -> None:
        if e.type == pygame.QUIT:
            self.quit()

        if self.in_menu:
            self.menu.event(e)

        if self.is_popup_open:
            self.popup.event(e)

        elif e.type == pygame.KEYDOWN:
            self.player.move(e.key)

    def loop(self) -> None:
        while True:
            self.clock.tick(self.cfg.fps)

            for e in pygame.event.get():
                self.event(e)

            self.draw()

            pygame.display.update()

    def quit(self):
        pygame.quit()
        quit()
