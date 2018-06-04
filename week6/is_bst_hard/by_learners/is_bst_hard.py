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
	return chkMinMax( tree, 0 , -2**32, 2**32 )

	
def chkMinMax( tree, index, Min, Max ) : # min and max are builtins - maybe..
	if tree[index][0] < Min or tree[index][0] > Max :
		return False
	if tree[index][1] == tree[index][2] == -1 :
		return True
	if tree[index][1] != -1 and not chkMinMax( tree, tree[index][1], Min, tree[index][0]-0.5 ) :
	# left child - Max is what needs to reduce
		return False
	if tree[index][2] != -1 and not chkMinMax( tree, tree[index][2], tree[index][0], Max ) :
	# right child - Min is what needs to increase..
		return False
	return True
		
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

# what is the right way to do this and still be efficient?
# if you go down a left branch, then you need to be less than something, but,
# you also need to be greater than the root, if you're on the right of the root..
# means? when you go right, you pass the min of the root and the max of the parent to your children
# when you go left, ..
# min can only increase, max can only decrease.. start at -2**32 and +2**32