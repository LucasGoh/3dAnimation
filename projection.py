import pygame
import numpy as np
from math import *

WHITE = (255, 255, 255)
RED = (255, 0 ,0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
pygame.init()
pygame.display.set_caption("3D projection in pygame!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

scale = 100

circle_pos = [WIDTH/2, HEIGHT/2]

angle = 0

points = []

points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1,  1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))

projection_scale = 1;


# contains positions of all the projected points 
projected_points = [
    [n, n] for n in range(len(points))
]

def connect_points(i, j, points):
    pygame.draw.line(screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))

clock = pygame.time.Clock()
while True:

    clock.tick(6)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == pygame.K_0:
                projection_scale += 0.5
            if event.key == pygame.K_9:
                projection_scale -= 0.5


    # update stuff
    # rotation matrix

    rotation_z = np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ])
    rotation_y = np.matrix([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)],
    ])

    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)],
    ])
    angle += 0.1

    screen.fill(WHITE)

    # drawing stuff
    
    projection_matrix = np.matrix([
        [projection_scale, 0, 0],
        [0, projection_scale, 0]
    ])

    i = 0
    for point in points:
        # applying rotation matrix
        rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
        rotated2d = np.dot(rotation_y, rotated2d)
        rotated2d = np.dot(rotation_x, rotated2d)

        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]

        projected_points[i] =[int(x), int(y)]
        pygame.draw.circle(screen, RED, (x,y), 5)
        i += 1
    
    # connect points
    for p in range(4):
            connect_points(p, (p+1) % 4, projected_points)
            connect_points(p+4, ((p+1) % 4) + 4, projected_points)
            connect_points(p, (p+4), projected_points)

    pygame.display.update()
