import pygame

class Wayly:
    def __init__(self):
        self.wayly_hSpeed = 0
        self.wayly_vSpeed = 0
        self.wayStarting_pos = (1300, 375)
    
    def return_startingPos(self):
        return self.wayStarting_pos

    def return_hSpeed(self):
        return self.wayly_hSpeed
    
    def return_vSpeed(self):
        return self.wayly_vSpeed

    def faster(self,speed):
        self.wayly_hSpeed += speed
        return self.wayly_hSpeed

way = Wayly()

print(way.return_hSpeed())