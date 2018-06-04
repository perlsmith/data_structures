#!/usr/bin/python3

import sys, threading, pdb

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree, index):
	# list of list of ints , int --> boolean
	# [ [ key , left_index , right_index ] ... ] , index of root --> True/False (True if a b tree)
	# Implement correct algorithm here
	if len( tree ) == 0 :
		return True
	if tree[index][1] == tree[index][2] == -1 :
		return True
	if tree[index][1] != -1 and tree[index][0] < getMax( tree, tree[index][1] ) :
		return False
	if tree[index][2] != -1 and tree[index][0] > getMax( tree, tree[index][2] ) :
		return False
	return IsBinarySearchTree( tree, tree[index][1] ) and IsBinarySearchTree( tree, tree[index][2] )
	
def getMax( tree, index ) :
	# list of list of ints, int --> int
	# will just travel down the right children to report back the max value
	if tree[index][2] == -1 :
		return tree[index][0]	# da key
	else :
		return max( tree[index][0] , getMax( tree, tree[index][2] ) )

def getMin( tree, index ) :
	# list of list of ints, int --> int
	# will just travel down the right children to report back the max value
	if tree[index][1] == -1 :
		return tree[index][0]	# da key
	else :
		return min( tree[index][0] , getMin( tree, tree[index][1] ) )
		
def main():
	nodes = int(sys.stdin.readline().strip())	# reads the first line --> int - # of nodes
	tree = []
	for i in range(nodes):
		tree.append(list(map(int, sys.stdin.readline().strip().split())))
	# pdb.set_trace()
	if IsBinarySearchTree(tree, 0):
		print("CORRECT")
	else:
		print("INCORRECT")

threading.Thread(target=main).start()

# statement says vertex with index 0 is the root..