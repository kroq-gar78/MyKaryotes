# This file is part of MyKaryotes.
# Copyright (C) 2013  Christopher Kyle Horton <christhehorton@gmail.com>

# MyKaryotes is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# MyKaryotes is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with MyKaryotes.  If not, see <http://www.gnu.org/licenses/>.

import sys, pygame
from cells import Cell
from walls import Wall
from buttons import ButtonSize, ButtonType, Button
pygame.init()
fpsClock = pygame.time.Clock()

size = width, height = 960, 608
mouse_x, mouse_y = 0, 0
speed = [2, 2]
black = 0, 0, 0

# Set up the window.
pygame.display.set_icon(pygame.image.load("graphics/icon_256x256.png"))
pygame.display.set_caption("MyKaryotes")
screen = pygame.display.set_mode(size)

# HUD setup.
panel_top = pygame.image.load("graphics/backgrounds/controlpanel_top.png")
panel_bottom = pygame.image.load("graphics/backgrounds/controlpanel_bottom.png")
panel_top = panel_top.convert()
panel_bottom = panel_bottom.convert()

rect_panel_top = pygame.Rect(0, 0, width, 64)
rect_panel_bottom = pygame.Rect(0, height - 32, width, height)

panel_font = pygame.font.Font(None, 32)

# Default background.
background = pygame.image.load("graphics/backgrounds/default_bkg.png")
background = background.convert()
bkg_rect = background.get_rect()
bkg_rect.topleft = (0, 64)

# Initial objects.
cells = []
for color, size, location, speed in [([0, 255, 0], 0.50, [64, 128], [0.0, 2.0]),
                                     ([0, 255, 0], 0.25, [width / 2, height / 2], [3.0, 0.0])]:
  cells.append(Cell(color, size, location, speed))

walls = []
for color, size, location in [([0, 255, 0], 1.0, [64, 128]),
                              ([0, 255, 0], 0.5, [width / 2, height / 2])]:
  walls.append(Wall(color, size, location))

left_buttons = []
right_buttons = []
for location, button_size, button_type in [([0, 0], ButtonSize.Large, ButtonType.Quit),
                                           ([64, 0], ButtonSize.Small, ButtonType.Producers),
                                           ([96, 0], ButtonSize.Small, ButtonType.Herbivores),
                                           ([128, 0], ButtonSize.Small, ButtonType.Carnivores),
                                           ([160, 0], ButtonSize.Small, ButtonType.Load)]:
  left_buttons.append(Button(location, button_size, button_type))

for location, button_size, button_type in [([width - 32 * 1, 0], ButtonSize.Small, ButtonType.Quit),
                                           ([width - 32 * 2, 0], ButtonSize.Small, ButtonType.Restart),
                                           ([width - 32 * 3, 0], ButtonSize.Small, ButtonType.Run),
                                           ([width - 32 * 4, 0], ButtonSize.Small, ButtonType.Options),
                                           ([width - 32 * 5, 0], ButtonSize.Small, ButtonType.Help)]:
  right_buttons.append(Button(location, button_size, button_type))

# Main game loop.
while 1:
  # Check if we quit yet.
  mouse_button = 0
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.MOUSEMOTION:
      mouse_x, mouse_y = event.pos
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x, mouse_y = event.pos
      mouse_button = event.button
  
  # Drawing and game object updates.
  screen.fill(black)
  screen.blit(background, bkg_rect)
  
  for w in walls:
    w.update(width, height)
    screen.blit(w.image, w.rect)
  
  for c in cells:
    c.update(width, height)
    screen.blit(c.image, c.rect)
  
  screen.blit(panel_top, rect_panel_top)
  screen.blit(panel_bottom, rect_panel_bottom)
  
  current_fps = int(fpsClock.get_fps())
  fpsSurface = panel_font.render("FPS: " + str(current_fps) + " [30 max.]", True, (0, 255, 255))
  fpsRect = fpsSurface.get_rect()
  fpsRect.topleft = rect_panel_bottom.topleft
  screen.blit(fpsSurface, fpsRect) 
  
  for b in left_buttons:
    b.update(mouse_x, mouse_y, mouse_button)
    screen.blit(b.image, b.rect)
  
  for b in right_buttons:
    b.update(mouse_x, mouse_y, mouse_button)
    screen.blit(b.image, b.rect)
  
  pygame.display.update()
  fpsClock.tick(30)
