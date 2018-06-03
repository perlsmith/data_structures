# python3

import sys, threading, pdb
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

# class Vertex :
	# def __init__( self, key, l_child, r_child ) : 
		# self.key

class TreeOrders:
	def read(self):
		self.n = int(sys.stdin.readline())
		self.key = [0 for i in range(self.n)]
		self.left = [0 for i in range(self.n)]
		self.right = [0 for i in range(self.n)]
		for i in range(self.n):
			[a, b, c] = map(int, sys.stdin.readline().split())
			self.key[i] = a
			self.left[i] = b	# 0 based indexing, -1 = null
			self.right[i] = c

	def io_traverse(self, index ) :
		if self.left[index] != -1 :
			result = self.io_traverse( self.left[index] )
		else :
			result = []
		result = result + [self.key[index]]
		if self.right[index] != -1 :
			result = result + self.io_traverse( self.right[index] )
		return result
			
	def po_traverse(self, index ) :
		if self.left[index] != -1 :
			result = self.po_traverse( self.left[index] )
		else :
			result = []
		if self.right[index] != -1 :
			result = result + self.po_traverse( self.right[index] )
		result = result + [self.key[index]]
		return result

	def preo_traverse(self, index ) :
		result = [self.key[index]]
		if self.left[index] != -1 :
			result = result + self.preo_traverse( self.left[index] )
		if self.right[index] != -1 :
			result = result + self.preo_traverse( self.right[index] )
		return result		

	def inOrder(self):
	# called on TreeOrders object --> list of ints (keys)
	# left-child, node, right-child
		self.result = []
		self.result = self.io_traverse(0)
    # Finish the implementation
    # You may need to add a new recursive method to do that
                
		return self.result

	def preOrder(self):
		self.result = []
		self.result = self.preo_traverse(0)
                
		return self.result

	def postOrder(self):
		self.result = []
		self.result = self.po_traverse(0)
                
		return self.result

def main():
	tree = TreeOrders()
	tree.read()
	# pdb.set_trace()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
