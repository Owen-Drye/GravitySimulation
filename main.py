import numpy as np
import pygame
import math 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (1000, 1000)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Gravity Simulation!")
 
done = False
 
clock = pygame.time.Clock()

def calculate_force(distance, m1, m2):
    G = 10
    force = G * ((m1 * m2) / distance ** 2)
    return force

def simulate(bodies):
    for body_one in bodies:
        for body_two in bodies:
                try:
                    distance = math.dist(body_two["position"], body_one["position"])
                    position_delta = (body_two["position"] - body_one["position"])
                    body_one["force_vector"] += calculate_force(distance, body_one["mass"], body_two["mass"]) * position_delta / float(body_one["mass"])
                except ZeroDivisionError:
                    pass
        
        
        body_one["position"] += body_one["force_vector"]

def draw_bodies(bodies):
    for body in bodies:
        pygame.draw.circle(screen, body["colour"], body["position"], body["size"])

bodies = [{"mass" : 10, "position" : np.array([500, 500], dtype=np.float64), "force_vector" : np.array([0, 0], dtype=np.float64), "size" : 20, "colour" : GREEN}, 
          {"mass" : 0.001, "position" : np.array([500, 800], dtype=np.float64), "force_vector" : np.array([10, 0], dtype=np.float64), "size" : 10, "colour" : RED}]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Logic

    simulate(bodies)

    screen.fill(BLACK)

    # Drawing
    draw_bodies(bodies)

    pygame.display.flip() 
    clock.tick(60)
 
pygame.quit()
