```python
# vr_module.py

import pyvirtualdisplay
import pygame
from pygame.locals import *

class VR:
    def __init__(self):
        # Initialize the virtual display
        self.display = pyvirtualdisplay.Display(visible=0, size=(800, 600))
        self.display.start()

        # Initialize Pygame
        pygame.init()

        # Set up the display
        self.screen = pygame.display.set_mode((800, 600))

    def render_lesson(self, lesson):
        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Render the lesson
        font = pygame.font.Font(None, 36)
        text = font.render(lesson, True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 300))
        self.screen.blit(text, text_rect)

        # Update the display
        pygame.display.flip()

        # Wait for the user to close the window
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
```
