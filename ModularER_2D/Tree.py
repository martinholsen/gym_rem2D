import matplotlib.pyplot as plt
'''
Tree blueprint
'''
class Tree:
	def __init__(self, moduleList):
		self.nodes = []
		self.moduleList = moduleList
	def getNodes(self):
		return self.nodes
	def get_leaves(self):
		leaves = 0
		for node in self.nodes:
			if node.parent != None or node.parent != -1:
				if isinstance(node.parent,int):
					self.nodes[node.parent].has_children = True
					continue
				node.parent.has_children = True
		for node in self.nodes:
			if node.has_children != True:
				leaves += 1
		return leaves


class Node:
	def __init__(self, index, parent, type, parent_connection_coordinates, controller=None,component=None, module_ = None):
		self.index = index
		self.type = type
		self.parent = parent
		self.has_children = False
		self.parent_connection_coordinates = parent_connection_coordinates
		# A controller can be attached for decentralized control of the robot
		self.controller = controller
		self.expressed = False
		# Component can be used to attach an object for reference
		self.component = component
		self.module_ = module_

	def __bool__(self):
		return self.expressed


# Could be used later when using weighted edges
class Edge:
	def __init__(self,parent, target):
		self.parent = parent
		self.target = target

