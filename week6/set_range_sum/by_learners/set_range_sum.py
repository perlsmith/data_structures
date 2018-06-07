# python3

from sys import stdin

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
	while v.parent != None:
		if v.parent.parent == None:
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
	(left, right) = split(root, x)
	new_vertex = None
	if right == None or right.key != x:	# don't insert if the key already exists i the tree
		new_vertex = Vertex(x, x, None, None, None)  
	root = merge(merge(left, new_vertex), right)
  
def erase(x): 
	# int --> nothing; side effect - vertex with given key is removed
	global root
  # Implement erase yourself
	search( x + 1 )	# get the successor to the root position (splaying)
	if not search( x ) :
		return
	else :	# now, we have x at the root position
		L = root.left
		R = root.right
		R.left = L
		L.parent = R
		root = R
		R.parent = None		# this is the new root
		update(L)
		update(R)
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
	if None == find_node or x != find_node.key :
		return False
	else :
		return True
  
def sum(fr, to): 
	global root
	(left, middle) = split(root, fr)
	(middle, right) = split(middle, to + 1)
	ans = 0
  # Complete the implementation of sum
  # not clear if the sum operation should be self-adjusting like a search or insertion..
	ans = middle.sum - right.sum
	merge(middle, right)

	return ans

MODULO = 1000000001
n = int(stdin.readline())		# how many operations
last_sum_result = 0
for i in range(n):
	line = stdin.readline().split()
	if '+' == line[0] :
		x = int(line[1])
		insert((x + last_sum_result) % MODULO)
	elif '-' == line[0] :
		x = int(line[1])
		erase((x + last_sum_result) % MODULO)
	elif '?' == line[0] :
		x = int(line[1])
		print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
	elif 's' == line[0] :
		l = int(line[1])
		r = int(line[2])
		res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
		print(res)
		last_sum_result = res % MODULO