#!/usr/bin/env python

import rospy
from lightswarm_core.msg import Shadow
from lightswarm_core.msg import Obstacles
from lightswarm_core.msg import World
from lightswarm_core.msg import Boid

WORLD_LIMIT = 100

class BoidSimulator:
    def __init__(self):
        self.node_name = 'boid_simulator'
        rospy.init_node(self.node_name)

        self.world = World()
        self.setup_world(0)

        self.sub = rospy.Subscriber('/obstacles', Obstacles, self.obstacles_callback)
        self.pub = rospy.Publisher('/world', World)


    def setup_world(self, idx):
        boids = []
        for x in range(-WORLD_LIMIT, WORLD_LIMIT+1, 10):
            for y in range(-WORLD_LIMIT, WORLD_LIMIT+1, 10):
                boid = Boid()
                boid.location.x = x
                boid.location.y = y
                boid.theta = idx%350.0
                boid.color = [100, 100, 100+idx%150]
                boids.append(boid)
        self.world.boids = boids



    def obstacles_callback(self, umbras):
        pass

    def run(self):
        r = rospy.Rate(1) # 1hz
        idx = 0

        while not rospy.is_shutdown():
            rospy.loginfo('published world')
            self.setup_world(idx)
            self.pub.publish(self.world)
            idx += 10
            r.sleep()



if __name__ == '__main__':
    simulator = BoidSimulator()
    simulator.run()


