# python3

import sys, threading, pdb
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

	
class TreeHeight:	# from starter solution
	def read(self):
		self.n = int(sys.stdin.readline())
		self.parents = list(map(int, sys.stdin.readline().split()))
		self.depths = [0] * self.n

	def get_depth(self, index ) :
	# object, int --> int
	# int is the index of the child parents array - i.e., 0 in [4 -1 ..]
	# means that 4 is the parent of 0 and will be returned
		if -1 == self.parents[ index ] :
			return 1
		elif 0 == self.depths[index] :
			self.depths[index] = 1 + self.get_depth( self.parents[index] )	# dynamic programming
			return self.depths[index]
		else :
			return self.depths[index]
		
		
	def compute_height(self):
		# Replace this code with a faster implementation
		maxDepth = 0
		for vertex in range(self.n):
			maxDepth = max(maxDepth, self.get_depth( vertex ) )
		return maxDepth;

def main():
  tree = TreeHeight()
  #pdb.set_trace()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
