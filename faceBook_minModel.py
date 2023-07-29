class Node:

	def __init__(self, main, edge=None, next=None):
		#print("Hello, ", main)
		self.main = main
		self.next = next
		self.edge = edge


Node_arr = []
ALL_node = []
Node_name = []


class Grap:
	global Node_arr
	global ALL_node  # Node which all ready present already in Grap #

	def __init__(self, node):
		Node_arr.insert(len(Node_arr), node)  # Node_arr.insert(-1, self.node)
		self.head = Node_arr[-1]
		self.edge = node.edge
		if node.main not in Node_name or Node_name == []:
			Node_name.append(node.main)
			ALL_node.append(node)

	def work(self):
		if self.head:
			for i in self.edge:
				current = self.head
				if i not in Node_name:
					temp_node = Node(i)
					ALL_node.append(temp_node)
					Node_name.append(i)
				else:
					for j in ALL_node:
						if j.main == i:
							temp_node = j
							break
				while current.next:
					current = current.next
				current.next = temp_node

	def print_grap(self):
		for i in Node_arr:
			current = i
		loop_stoper = []
		while current:
			if current.main in loop_stoper:
				break
			loop_stoper.append(current.main)
			print(current.main, end=" ")
			current = current.next
		print()

	def friends(self, name):
		current = None
		if name not in Node_name:
			print(f"{name} is not found :(")
			return -1
		for i in Node_arr:
			if i.main == name:
				current = i
		if current == None:
			print("It is not Main Node")
		else:
			print(f"Friends of {name} : ", end=" ")
			for i in Node_arr:
				if i.main == name:
					continue
				current_main = i.next
				while current_main:
					if current_main.main == name:
						print(i.main, end=" ")
						break
					current_main = current_main.next
			loop_stoper = []
			current = current.next
			while current:
				if current.main in loop_stoper:
					break
				loop_stoper.append(current.main)
				print(current.main, end=" ")
				current = current.next
			print()

	def main_name(self):
		for i in Node_arr:
			print(i.main)
		print("Node_arr: ", Node_arr)
		print("ALL_node: ", ALL_node)
		print("Node_name: ", Node_name)
