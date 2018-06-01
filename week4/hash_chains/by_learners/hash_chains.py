# python3
import pdb

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
	_multiplier = 263
	_prime = 1000000007

	def __init__(self, bucket_count):
		self.bucket_count = bucket_count
		# store all strings in one list -- no more - end the naivete once and for all - evil starter suppliers!
		self.elems = []
		for i in range(bucket_count) :
			self.elems.append( [] )

	def _hash_func(self, s):
		ans = 0
		for c in reversed(s):
			ans = (ans * self._multiplier + ord(c)) % self._prime
		return ans % self.bucket_count

	def write_search_result(self, was_found):
		print('yes' if was_found else 'no')

	def write_chain(self, chain):
		print(' '.join(chain))

	def read_query(self):
		return Query(input().split())

	def process_query(self, query):
		if query.type == "check":
            # use reverse order, because we append strings to the end
            # self.write_chain(cur for cur in reversed(self.elems)
                        # if self._hash_func(cur) == query.ind)
			# it looks like this is where the naivete comes in - one list (no real chaining)
			# and then we go through the entire list and recompute hashes each time.. duh - 
			# why not call it out so we can be efficient?
			self.write_chain( reversed( self.elems[query.ind]) )
			# logic : pick the right sub-list, and then reverse it.. and..
		else:
			try:
				ind = self.elems[self._hash_func(query.s)].index(query.s)
				# logic : compute hash, use that to pick appropriate sub-list, then, same as naive
			except ValueError:
				ind = -1
			if query.type == 'find':
				self.write_search_result(ind != -1)
			elif query.type == 'add':
				if ind == -1:
					self.elems[self._hash_func(query.s)].append(query.s)
			else:				# only remaining case is "del" (delete)
				if ind != -1:
					self.elems[self._hash_func(query.s)].pop(ind)

	def process_queries(self):
		n = int(input())
		for i in range(n):
			self.process_query(self.read_query())

if __name__ == '__main__':
	bucket_count = int(input())		# das ist m
	proc = QueryProcessor(bucket_count)
	#pdb.set_trace()
	proc.process_queries()


# our masters don't tell us where the naivete is implemented in the starter
# solution :)