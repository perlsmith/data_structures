# python3

import sys
import pdb


def getParent(table):
	# int --> int
	# find parent and compress path
	if table != parents[table] :	# not the root
		parents[table] = getParent( parents[table] )	# replace current parent
	return parents[table]

def merge(destination, source, lines, ans):
	# (int, int, list, int ) --> int, and side effect is that lines and parents are manipulated
	# given ans, it will return the updated ans - that is, lines of the destination topping existing ans will
	# cause ans to be updated
	realDestination, realSource = getParent(destination), getParent(source)

	if realDestination != realSource :

	# merge two components
	# use union by rank heuristic 
		if rank[ realSource ] > rank[ realDestination ] :
			parents[realSource] = realDestination
			lines[realDestination] += lines[realSource]
			# lines[source] = 0	# is this really necessary? Shouldn't parents tell you if you have a link?
			if lines[realDestination] > ans :
				return lines[realDestination]
			else :
				return ans
		else :
			parents[realDestination] = realSource
			lines[realSource] += lines[realDestination]
			if rank[ realDestination] == rank[realSource] :
				rank[ realSource ] += 1
			if lines[realSource] > ans :
				return lines[realSource]
			else :
				return ans
	else :
		return ans
		

    
if __name__ == '__main__':
	# sys.setrecursionlimit( 100000 )
		
	n, m = map(int, sys.stdin.readline().split())
	lines = list(map(int, sys.stdin.readline().split()))
	rank = [0] * n				# starter had 1 not 0
	parents = list(range(0, n))	# to start with, each table is its own disjoint set. If parent[i] == i, then not a link :)
	ans = max(lines)			# with each merge, check if A+B > ans and updated..
	
	# pdb.set_trace()
	for i in range(m):
		destination, source = map(int, sys.stdin.readline().split())
		ans = merge(destination - 1, source - 1, lines, ans)
		print(   ans  )

# n tables and m operations, each op is a merge and you have to report max size (of any table) after the op
# not that that input is using 1 based indexing for the merge operations