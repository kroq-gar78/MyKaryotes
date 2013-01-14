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

import pygame

class Wall(pygame.sprite.Sprite):
  wall_image = None
  #highlight_image = None
  
  def __init__(self, color, size, initial_position):
    pygame.sprite.Sprite.__init__(self)
    
    if Wall.wall_image is None:
      Wall.wall_image = pygame.image.load("graphics/walls/wall_rounded.png")
    
    # TODO: Change wall sprite based on position next to other walls.
    self.image = Wall.wall_image
    self.rect = self.image.get_rect()
    self.color = color
    self.size = size
    self.rect.topleft = initial_position
    
    new_width = int(self.image.get_rect().width * self.size)
    new_height = int(self.image.get_rect().height * self.size)
    self.image = pygame.transform.scale(self.image, (new_width, new_height))
    self.rect = self.image.get_rect()
    self.rect.topleft = initial_position
  
  def update(self, width, height):
    # TODO: Put wall...stuff... in here.
    if self.rect.left < 0:
      self.rect.left = 0
