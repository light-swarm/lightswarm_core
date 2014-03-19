#!/usr/bin/env python

import rospy
from lightswarm_core.msg import World
from lightswarm_core.msg import Penumbras

WORLD_LIMIT = 100


class Renderer(object):
	def __init__(self):
		rospy.init_node('renderer')
		self.world_sub = rospy.Subscriber('/world', World, self.world_callback)
		self.penumbras_sub = rospy.Subscriber('/penumbras', Penumbras, self.penumbras_callback)

	def world_callback(self, world):
		pass

	def penumbras_callback(self, penumbras):
		pass

	def run(self):
		rospy.spin()


if __name__ == '__main__':
	renderer = Renderer()
	renderer.run()
	