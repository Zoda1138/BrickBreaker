import pygame
from pygame.locals import *


class App:

    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((640, 640), flags)
        App.running = True

        self.shortcuts = {
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'print("ctrl+X")',
        }

    def do_shortcut(self, event):
        """Find the the key/mod combination in the dictionary and execute the cmd."""

        k = event.key
        m = event.mod
        if (k, m) in self.shortcuts:
            exec(self.shortcuts[k, m])

    def run(self):
        """Run the main event loop."""

        while App.running:
            for event in pygame.event.get():

                if event.type == QUIT:
                    App.running = False

                if event.type == KEYDOWN:
                    self.do_shortcut(event)

        pygame.quit()
