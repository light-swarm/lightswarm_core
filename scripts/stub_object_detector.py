#!/usr/bin/env python

import rospy
from lightswarm_core.msg import Objects
from lightswarm_core.msg import Cylinder

WORLD_LIMIT = 100

class ObjectDetector(object):
	def __init__(self):
		rospy.init_node('object_detector')

		self.pub = rospy.Publisher('/objects', Objects)

	def run(self):
		fake_cylinder = Cylinder()
		fake_cylinder.location.x = 0
		fake_cylinder.location.y = 0
		fake_cylinder.height = 180  # about 6ft tall
		fake_cylinder.radius = 20 # chubby

		objects = Objects()
		objects.cylinders.append(fake_cylinder)

		r = rospy.Rate(10) # 10hz

		while not rospy.is_shutdown():
			rospy.loginfo('published something')
			self.pub.publish(objects)
			fake_cylinder.location.x = (fake_cylinder.location.x + 1) % WORLD_LIMIT
			r.sleep()


if __name__ == '__main__':
	detector = ObjectDetector()
	detector.run()



