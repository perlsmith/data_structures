# python3

import sys, pdb

# Vertex of a splay tree
class Vertex:
	def __init__(self, char, size, left, right, parent):
  # maintains the size of the subtree
		(self.char, self.size, self.left, self.right, self.parent) = (char, size, left, right, parent)
	# the key is the character value - single string char like 'b'

def update(v):
# called by the rotation functions to update the sum and the childrens' parent pointers
	if v == None:
		return
	v.size = 1 + (v.left.size if v.left != None else 0) + (v.right.size if v.right != None else 0)
	if v.left != None:
		v.left.parent = v
	if v.right != None:
		v.right.parent = v

def smallRotation(v):
	parent = v.parent
	size = v.size
	if parent == None:		# already the root (?)
		return
	grandparent = v.parent.parent
	if parent.left == v:		# i.e., we are left child, parent's key is > than us.. so it gets our right child..
		v.size = v.size + (parent.right.size if parent.right != None else 0) -(v.right.size if v.right != None else 0 )
		parent.size = parent.size - size + (v.right.size if v.right != None else 0 )
		m = v.right
		v.right = parent
		parent.left = m
	else:	# we are the right child
		v.size = v.size + 1 + (parent.left.size if parent.left != None else 0 ) - (v.left.size if v.left != None else 0 )
		parent.size = parent.size -size + (v.left.size if v.left != None else 0 )
		m = v.left
		# sizes updated prior to rotation..
		v.left = parent
		parent.right = m
		
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

	
# Searches for the given position in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger position (next value in the order).
# If the position is bigger than all positions in the tree,
# then result is None.
def find(root, position): 
	target = find_position( root, position )
	if target != None :
		root = splay(target)
	return (target, root)
	
def find_position( root, position ) :
	# ( vertex object , int ) --> vertex object
	# same as find, but doesn't do any splaying since this
	# calls itself recursively
	if None == root :
		return None
	else :
		if root.left == None :	# if root has no left child, then
								# string starts here :)
			if position == 1 :
				return root
			else :
				if root.right == None :
					return None
				else :
					if position < root.size + 1 :
					# only then can the target exist here
						return find_position( root.right, position - 1 )
					else :
						return None
		else :
			s = root.left.size
			if position == s + 1 :
				return root
			else :
				if position < s + 1 : # char exists in this subtree
					return find_position( root.left, position )
				elif root.right != None :
					return find_position( root.right, position -s -1)
				else :
					return None

	
class Rope:
	def __init__(self, s):
		self.s = s
		# char, size, left, right, parent
		latest = None
		for i, char in enumerate( reversed( s[1::] ) ) :
			c = Vertex( char, i+1, None, None, None )
			if latest != None :
				c.right = latest
				latest.parent = c
			latest = c
		self.root = Vertex( s[0], 1 + latest.size, None, latest, None )
		latest.parent = self.root
			
	def result(self):
		return self.s
	def process(self, i, j, k):
                # Write your code here
		extract = self.s[i:j+1]
		self.s = self.s[0:i] + self.s[j+1:]
		self.s = self.s[0:k] + extract + self.s[k:]
                
if __name__ == "__main__":
	pdb.set_trace()
	rope = Rope(sys.stdin.readline().strip())
	# debug WIP
	mid,root = find( rope.root, 3 )
	q = int(sys.stdin.readline())
	for _ in range(q):
		i, j, k = map(int, sys.stdin.readline().strip().split())
		rope.process(i, j, k)
	print(rope.result())
