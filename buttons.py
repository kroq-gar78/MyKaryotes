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

button_path = "graphics/buttons/"
button_icon_path = button_path + "icons/"

class ButtonSize:
  Large, Small = range(2)

class ButtonType:
  Options, Help, Run, Pause, Restart, Quit, \
  Carnivores, Herbivores, Producers, \
  Load = range(10)

class Button(pygame.sprite.Sprite):
  def __init__(self, initial_position, button_size, button_type):
    pygame.sprite.Sprite.__init__(self)
    
    icon_image = None
    if button_size == ButtonSize.Large:
      button_image = pygame.image.load(button_path + "button_base_64x32.png")
      highlight_image = pygame.image.load(button_path + "button_highlight_64x32.png")
    elif button_size == ButtonSize.Small:
      button_image = pygame.image.load(button_path + "button_base_32x32.png")
      highlight_image = pygame.image.load(button_path + "button_highlight_32x32.png")
    
    self.button_size = button_size
    self.button_type = button_type
    self.initial_position = initial_position
    self.image = button_image
    self.rect = self.image.get_rect()
    self.image.blit(highlight_image, self.rect)
    self.rect.topleft = initial_position
    if button_size == ButtonSize.Small:
      self.updateIcon()
  
  def update(self, mouse_x, mouse_y, mouse_button):
    # Only respond to left clicks.
    if mouse_button == 1:
      if self.rect.collidepoint(mouse_x, mouse_y):
        # The button was clicked. React accordingly.
        if self.button_type == ButtonType.Quit:
          pygame.quit()
          sys.exit()
        elif self.button_type == ButtonType.Run:
          self.button_type = ButtonType.Pause
          self.updateIcon()
        elif self.button_type == ButtonType.Pause:
          self.button_type = ButtonType.Run
          self.updateIcon()
        # TODO: Finish this up for all buttons.
  
  def updateIcon(self):
    # Updates the button icon.
    # Call only for small buttons.
    button_image = pygame.image.load(button_path + "button_base_32x32.png")
    highlight_image = pygame.image.load(button_path + "button_highlight_32x32.png")
    
    if self.button_type == ButtonType.Options:
      icon_image = pygame.image.load(button_icon_path + "options_icon.png")
    elif self.button_type == ButtonType.Help:
      icon_image = pygame.image.load(button_icon_path + "load_icon.png") # TODO: Create an icon for this
    elif self.button_type == ButtonType.Run:
      icon_image = pygame.image.load(button_icon_path + "run_icon.png")
    elif self.button_type == ButtonType.Pause:
      icon_image = pygame.image.load(button_icon_path + "pause_icon.png")
    elif self.button_type == ButtonType.Restart:
      icon_image = pygame.image.load(button_icon_path + "restart_icon.png")
    elif self.button_type == ButtonType.Quit:
      icon_image = pygame.image.load(button_icon_path + "quit_icon.png")
    elif self.button_type == ButtonType.Carnivores:
      icon_image = pygame.image.load(button_icon_path + "create_carnivores_icon.png")
    elif self.button_type == ButtonType.Herbivores:
      icon_image = pygame.image.load(button_icon_path + "create_herbivores_icon.png")
    elif self.button_type == ButtonType.Producers:
      icon_image = pygame.image.load(button_icon_path + "create_producers_icon.png")
    elif self.button_type == ButtonType.Load:
      icon_image = pygame.image.load(button_icon_path + "load_icon.png")
    else:
      icon_image = None
    
    self.image = button_image
    self.rect = self.image.get_rect()
    if icon_image != None and self.button_size == ButtonSize.Small:
      self.image.blit(icon_image, self.rect)
    self.image.blit(highlight_image, self.rect)
    self.rect.topleft = self.initial_position
