#!/usr/bin/env python

import rospy
from lightswarm_core.msg import Shadow
from lightswarm_core.msg import Point
from lightswarm_core.msg import Obstacles
from lightswarm_core.msg import Polygon
from lightswarm_core.msg import Penumbras
from lightswarm_core.msg import Objects

WORLD_LIMIT = 100

class ShadowCalculator(object):
	def __init__(self):
		rospy.init_node('shadow_calculator')
		self.sub = rospy.Subscriber('/objects', Objects, self.objects_callback)
		self.penumbras_pub = rospy.Publisher('/penumbras', Penumbras)
		self.obstacles_pub = rospy.Publisher('/obstacles', Obstacles)

	def objects_callback(self, objects):
		polygon = self.get_polygon_from_location(objects.cylinders[0].location)

		self.obstacles_pub.publish(Obstacles(polygons=[polygon])) 

		shadow = Shadow(projector_id = 'fake_projector', polygon = polygon)
		self.penumbras_pub.publish(Penumbras(projector_shadows=[shadow]))


	def get_polygon_from_location(self, location):
		shadow_vertex1 = location
		shadow_vertex2 = Point(x = location.x + 10, y = location.y)
		shadow_vertex3 = Point(x = location.x, y = location.y + 10)
		p = Polygon(points=[shadow_vertex1, shadow_vertex2, shadow_vertex3])
		return p

	def run(self):
		rospy.spin()


if __name__ == '__main__':
	shadow_calc = ShadowCalculator()
	shadow_calc.run()

