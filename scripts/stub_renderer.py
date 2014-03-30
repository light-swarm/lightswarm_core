#!/usr/bin/env python

import rospy
import pygame

from lightswarm_core.msg import World
from lightswarm_core.msg import Penumbras

WIDTH = 500
HEIGHT = 500
WORLD_LIMIT = 100 # 100cm in each direction

X_SCALE = WIDTH / (2.0*WORLD_LIMIT)
Y_SCALE = HEIGHT / (2.0*WORLD_LIMIT)

def boid_world_to_pixels(point):

    x = (point.x + WORLD_LIMIT) * X_SCALE

    y = (point.y + WORLD_LIMIT) * Y_SCALE
    return (int(x), int(y))


class Renderer(object):
    def __init__(self):
        pygame.init()
        rospy.init_node('renderer')

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((20,20,20))

        self.world_sub = rospy.Subscriber('/world', World, self.world_callback)
        self.penumbras_sub = rospy.Subscriber('/penumbras', Penumbras, self.penumbras_callback)

        self.last_world = None
        self.last_penumbras = None

    def world_callback(self, world):
        self.last_world = world

    def penumbras_callback(self, penumbras):
        self.last_penumbras = penumbras

    def render_boid(self, boid):
        (x,y) = boid_world_to_pixels(boid.location)
        pygame.draw.circle(self.screen, (255, 250, 250), (x,y), 3)

    def render_world(self):
        if self.last_world is None:
            return
        for boid in self.last_world.boids:
            self.render_boid(boid)

    def render_shadow(self, shadow):
        boid_world_polygon = shadow.polygon
        pixel_polygon = [boid_world_to_pixels(p) for p in boid_world_polygon.points]
        pygame.draw.circle(self.screen, (255, 128, 228), pixel_polygon[0], 5)
        pygame.draw.polygon(self.screen, (255, 128, 228), pixel_polygon, 3)


    def render_penumbras(self):
        if self.last_penumbras is None:
            return
        for shadow in self.last_penumbras.projector_shadows:
            self.render_shadow(shadow)


    def render_one_frame(self):
        self.screen.blit(self.background, (0,0))

        self.render_world()
        self.render_penumbras()
        pygame.display.flip()


    def run(self):
        r = rospy.Rate(30) # 30Hz. nothing to do with ros
        while not rospy.is_shutdown():
            self.render_one_frame()
            r.sleep()



if __name__ == '__main__':
    renderer = Renderer()
    renderer.run()
    