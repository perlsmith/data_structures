# python3
import pdb

class HeapBuilder:		# min heap..
	def __init__(self):
		self._swaps = []
		self._data = []

	def ReadData(self):
		n = int(input())
		self._data = [int(s) for s in input().split()]
		assert n == len(self._data)

	def WriteResponse(self):
		print(len(self._swaps))
		for swap in self._swaps:
			print(swap[0], swap[1])

	def SiftDown( self , index ) :
	# HeapBuilder object , int --> nothing, adds to the swaps list to sift the element
	# down until it is smaller than its children
		n = len( self._data )
		if index > n // 2 : # i.e., already a leaf, we're done..
			return
		else :
			minInd = index
			l = 2*index + 1
			r = 2*index + 2
			if l < n and self._data[minInd] > self._data[l] :
				minInd = l
			if r < n and self._data[minInd] > self._data[r] :
				minInd = r
			if minInd != index :
				self._swaps.append( (minInd, index) )
				self._data[minInd], self._data[index] = self._data[index], self._data[minInd]
				self.SiftDown( minInd )
	  
	def GenerateSwaps(self):
    # ( HeapBuilder object with data populated (ints) ) --> swaps list populated
	# implements the siftdowns essentially. This is for a min-heap BTW..
		n = len(self._data)
		for i in range( n // 2 , -1, -1 ) :
			self.SiftDown( i )

	def Solve(self):
		self.ReadData()
		self.GenerateSwaps()
		self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    # pdb.set_trace()
    heap_builder.Solve()
