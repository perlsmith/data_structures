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
	if tree[index][0] < tree[ tree[index][1] ][0] or tree[index][0] > tree[ tree[index][2] ][0] :
		return False
	else :
		return IsBinarySearchTree( tree, tree[index][1] ) and IsBinarySearchTree( tree, tree[index][2] )

def main():
	nodes = int(sys.stdin.readline().strip())	# reads the first line --> int - # of nodes
	tree = []
	for i in range(nodes):
		tree.append(list(map(int, sys.stdin.readline().strip().split())))
	pdb.set_trace()
	if IsBinarySearchTree(tree, 0):
		print("CORRECT")
	else:
		print("INCORRECT")

threading.Thread(target=main).start()

# statement says vertex with index 0 is the root..