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
import math
import random

cell_path = "graphics/cells/"

class Cell(pygame.sprite.Sprite):
  cell_image = None
  membrane_image = None
  membrane_hl_image = None
  nucleus_image = None
  nucleus_hl_image = None
  
  def __init__(self, color, size, initial_position, speed):
    pygame.sprite.Sprite.__init__(self)
    
    if Cell.cell_image is None:
      Cell.cell_image = pygame.image.load(cell_path + "cytoplasm.png")
    if Cell.membrane_image is None:
      membrane_image = pygame.image.load(cell_path + "membrane.png")
    if Cell.membrane_hl_image is None:
      membrane_hl_image = pygame.image.load(cell_path + "membrane_highlight.png")
    if Cell.nucleus_image is None:
      nucleus_image = pygame.image.load(cell_path + "nucleus.png")
    if Cell.nucleus_hl_image is None:
      nucleus_hl_image = pygame.image.load(cell_path + "nucleus_highlight.png")
    
    # TODO: Implement image colorizing.
    
    cell_image = Cell.cell_image
    cell_rect = Cell.cell_image.get_rect()
    
    cell_image.blit(membrane_image, cell_rect)
    cell_image.blit(nucleus_image, cell_rect)
    cell_image.blit(nucleus_hl_image, cell_rect)
    cell_image.blit(membrane_hl_image, cell_rect)
    
    self.image = cell_image
    self.default_image = cell_image
    self.rect = self.image.get_rect()
    self.color = color
    self.size = size
    self.radius = self.rect.width / 2
    self.rect.center = initial_position
    # Trick I saw suggested in a comment on pygame.org to get better movement
    self.real_x = self.rect.centerx
    self.real_y = self.rect.centery
    self.speed = speed
    self.friction = 0.01
    # TODO: Flesh this out some more to setup other variables.
  
  def update(self, width, height):
    # Resize for size changes and bouncing.
    cur_pos_x = self.rect.centerx
    cur_pos_y = self.rect.centery
    new_width = int(self.default_image.get_rect().width * self.size)
    new_height = int(self.default_image.get_rect().height * self.size)
    self.image = pygame.transform.scale(self.default_image, (new_width, new_height))
    self.rect = self.image.get_rect()
    self.rect.center = [cur_pos_x, cur_pos_y]
    
    # Move at current velocity, then adjust velocity based on friction, etc.
    self.real_x = self.real_x + self.speed[0]
    self.real_y = self.real_y + self.speed[1]
    self.rect.center = [round(self.real_x), round(self.real_y)]
    self.applyFriction()
    if self.getVelocityMagnitude() < 1.0:
      self.tumbleAndRun()
    
    # Bounce away from arena edge walls.
    if self.rect.left < 0 or self.rect.right > width:
      self.speed[0] = -self.speed[0]
    if self.rect.top < 32 or self.rect.bottom > height - 32:
      self.speed[1] = -self.speed[1]
    # TODO: Add more stuff in here to check for and do.
  
  def applyFriction(self):
    # Applies friction to the given velocity.
    velocity_magnitude = self.getVelocityMagnitude()
    velocity_direction = self.getVelocityDirection()
    velocity_magnitude -= self.friction
    self.setVelocity(velocity_magnitude, velocity_direction)
  
  def tumbleAndRun(self):
    # Instantaenously and randomly changes the cell's speed and direction.
    velocity_magnitude = 5.0 * random.random()
    velocity_direction = 2 * math.pi * random.random()
    self.setVelocity(velocity_magnitude, velocity_direction)
  
  def getVelocityMagnitude(self):
    # Returns the magnitude of the current velocity vector.
    return math.hypot(self.speed[0], self.speed[1])
  
  def getVelocityDirection(self):
    # Returns the direction of the current velocity vector.
    return math.atan2(self.speed[1], self.speed[0])
  
  def setVelocity(self, magnitude, direction):
    # Sets the velocity based on a given magnitude and direction.
    self.speed[0] = magnitude * math.cos(direction)
    self.speed[1] = magnitude * math.sin(direction)
