# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node :
	def __init__( self, parent ) :
	# ( object, integer ) --> nothing (creates object in memory)
		self.parent = parent
		if -1 == parent :
			self.depth = 1	# root node!!
		else
			self.depth = 0	# >= 1 always, so, this tells you to compute
				# and assign!

	def get_depth( self ) :
	# ( object ) --> int (which is 1 + num branches to root )
		if 0 == self.depth :
			self.depth = self.parent.get_depth()
			return self.depth
		else
			return self.depth	# this is where the dynamic programming comes in

class Tree :
	def read(self) :
		self.n = int( sys.stdin.readline() )
		for i, parent in list( map( int, sys.stdin.readline().split())) :
			
	
class TreeHeight:	# from starter solution
	def read(self):
		self.n = int(sys.stdin.readline())
		self.parent = list(map(int, sys.stdin.readline().split()))

	def compute_height(self):
		# Replace this code with a faster implementation
		maxHeight = 0
		for vertex in range(self.n):
			height = 0
			i = vertex
			while i != -1:
				height += 1
				i = self.parent[i]
				maxHeight = max(maxHeight, height);
		return maxHeight;

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
