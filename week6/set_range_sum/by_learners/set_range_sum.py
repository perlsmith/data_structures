# python3

from sys import stdin, stderr
import pdb

import inspect

def isDBG():
	for frame in inspect.stack():
		if frame[1].endswith("pdb.py"):
			return True
	return False

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
	def __init__(self, key, sum, left, right, parent):
  # maintains the sum of the subtree
		(self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
# called by the rotation functions to update the sum and the childrens' parent pointers
	if v == None:
		return
	v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
	if v.left != None:
		v.left.parent = v
	if v.right != None:
		v.right.parent = v

def smallRotation(v):
	parent = v.parent
	if parent == None:		# already the root (?)
		return
	grandparent = v.parent.parent
	if parent.left == v:		# i.e., we are left child, parent's key is > than us.. so it gets our right child..
		m = v.right
		v.right = parent
		parent.left = m
	else:
		m = v.left
		v.left = parent
		parent.right = m
	update(parent)
	update(v)
	v.parent = grandparent
	if grandparent != None:
		if grandparent.left == parent:
			grandparent.left = v
		else: 
			grandparent.right = v

def bigRotation(v):
	if v.parent.left == v and v.parent.parent.left == v.parent:
		# Zig-zig
		smallRotation(v.parent)
		smallRotation(v)
	elif v.parent.right == v and v.parent.parent.right == v.parent:
		# Zig-zig
		smallRotation(v.parent)
		smallRotation(v)    
	else: 
		# Zig-zag
		smallRotation(v)
		smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v) :
	if v == None :
		return None
	while v.parent != None:	# i.e, v is not yet root!!
		if v.parent.parent == None: # if v's parent IS root
			smallRotation(v)
			break
		bigRotation(v)
	return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key): 
	v = root
	last = root
	next = None
	while v != None:
		if v.key >= key and (next == None or v.key < next.key):
			next = v    
			last = v
		if v.key == key:
			break    
		if v.key < key:
			v = v.right
		else: 
			v = v.left      
	root = splay(last)
	return (next, root)

def split(root, key):  
	(result, root) = find(root, key)  
	if result == None:    
		return (root, None)  
	right = splay(result)
	left = right.left
	right.left = None
	if left != None:
		left.parent = None
	update(left)
	update(right)
	return (left, right)

  
def merge(left, right):
	if left == None:
		return right
	if right == None:
		return left
	while right.left != None:
		right = right.left
	right = splay(right)
	right.left = left
	update(right)
	return right

  
# Code that uses splay tree to solve the problem
                                    
root = None

def insert(x):
	global root
	(left, right) = split(root, x) # this is what lets you insert at the right place
	new_vertex = None
	if right == None or right.key != x:	# don't insert if the key already exists i the tree
		new_vertex = Vertex(x, x, None, None, None)  
	root = merge(merge(left, new_vertex), right)
  
def erase(x): 
	# int --> nothing; side effect - vertex with given key is removed
	# may not have correctly implemented case of x being largest key..
	# in which case there is no successor..
	# might be a very leaky implementation since we don't have a destructor
	# for class Vertex.. how to fix that?
	global root
  # Implement erase yourself
	search( x + 1 )	# get the successor to the root position (splaying)
	if not search( x ) :
		return
	else :	# now, we have x at the root position
		if root.left == None and root.right == None :
			root = None
			return
		L = root.left
		R = root.right
		if R != None :
			if L != None :
				R.left = L
				L.parent = R
				update(L)
			root = R
			R.parent = None		# this is the new root
			update(R)
		else : # that is, only L exists
			root = L
			L.parent = None
			update(L)
# L <— N.Left
# R <— N.Right
# R.Left <— L
# L.Parent <— R
# Root <— R
# R.Parent <- null

def search(x): 
  # int --> boolean
	global root
  # Implement find yourself
	find_node, find_root = find( root, x )
	root = find_root
	if None == find_node or x != find_node.key :
		return False
	else :
		return True
  
def Sum(fr, to): 
	global root
	(left, middle) = split(root, fr)
	(middle, right) = split(middle, to + 1)
	ans = 0
  # Complete the implementation of sum
  # not clear if the sum operation should be self-adjusting like a search or insertion..
	if middle != None :
		# ans = middle.sum - ( right.sum if right != None else 0 )
		ans = middle.sum
		root = merge( left , merge(middle, right) )
	else :
		root = merge( left, right )

	return ans

def nElems( vertex ) :
	if vertex == None :
		return 0 
	if isDBG() :
		print( vertex.key )
	return 1 + nElems( vertex.left ) + nElems( vertex.right )

	
if __name__ == "__main__":
	line = None
	MODULO = 1000000001
	n = int(stdin.readline())		# how many operations
	line_cnt = 0	# debug aid
	last_sum_result = 0
	# cheating :
	sum_count = 0
	cheat_list = []
	for i in range(n):
		old_line = line
		line = stdin.readline().split()
		if len( line ) == 1 :
			stderr.write( "entering debug 1")
			stderr.write( "# lines ...... " + str(line_cnt) )
			pdb.set_trace()
		line_cnt += 1	# debug aid
		# pdb.set_trace()
		if '+' == line[0] :
			x = int(line[1])
			insert((x + last_sum_result) % MODULO)
			if not (x + last_sum_result ) % MODULO in cheat_list :
				cheat_list.append( (x + last_sum_result) % MODULO ) # dbg aid
		elif '-' == line[0] :
			x = int(line[1])
			# pdb.set_trace()
			erase((x + last_sum_result) % MODULO)
			if (x + last_sum_result) % MODULO in cheat_list :
				cheat_list.remove( (x + last_sum_result) % MODULO )
			if len( cheat_list ) != nElems( root ) :
				stderr.write( "bad delete op!")
				stderr.write( "# lines :::::::::: " + str(line_cnt) ) 
				pdb.set_trace()
			
		elif '?' == line[0] :
			x = int(line[1])
			print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
		elif 's' == line[0] :
			l = int(line[1])
			r = int(line[2])
			sum_count += 1
			# if 11 == sum_count :
				# pdb.set_trace()
			res = Sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
			print(res)
			# if sum_count > 8 and None == root :
				# pdb.set_trace()
			last_sum_result = res % MODULO
		elif 'd' == line[0] : # or line_cnt == 63 :
			stderr.write( "entering debug 2")
			pdb.set_trace()	# debug aid

		if len( cheat_list ) != nElems( root ) :
			stderr.write( "# lines ---------  " +str( line_cnt ) + "\n" )
			pdb.set_trace()