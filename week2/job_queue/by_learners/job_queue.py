# python3
import pdb

class JobQueue:
	def read_data(self):
		self.num_workers, m = map(int, input().split())		# threads and # jobs
		self.jobs = list(map(int, input().split()))			# CPU time of each job
		assert m == len(self.jobs)

	def write_response(self):
		for i in range(len(self.jobs)):
			print(self.assigned_workers[i], self.start_times[i]) 

	def replace_min( self, CPU_time ) :
	# object, int --> (int,int) ( manipulates self.occupancy)
	# given JobQueue object and new job's CPU_time, it returns the next available thread and finish time
	# of the existing job and also updates the priority queue
		resource = self.occupancy[0]	# will be a tuple containing (thresd, finish_time)
		self.occupancy[0] = resource[0],CPU_time + resource[1]
		self.sift_down( 0 )
		return resource[0], resource[1]
	
	def sift_down( self , index) :
	# object , int --> nothing (manipulates self.occupancy )
		n = self.num_workers
		if index > n // 2 : # i.e., already a leaf, we're done..
			return
		else :
			minInd = index
			l = 2*index + 1
			r = 2*index + 2
			if l < n :
				if self.occupancy[minInd][1] > self.occupancy[l][1] :
					minInd = l
				elif self.occupancy[minInd][1] == self.occupancy[l][1] and self.occupancy[minInd][0] > self.occupancy[l][0] :
					minInd = l
			if r < n :
				if self.occupancy[minInd][1] > self.occupancy[r][1] :
					minInd = r
				elif self.occupancy[minInd][1] == self.occupancy[r][1] and self.occupancy[minInd][0] > self.occupancy[r][0] :
					minInd = r
			# if l < n and r < n and self.occupancy[l][1] == self.occupancy[r][1] == self.occupancy:
				# if self.occupancy[l][0] < self.occupancy[r][0] :
					# minInd = l
				# else :
					# minInd = r
			if minInd != index :
				self.occupancy[minInd], self.occupancy[index] = self.occupancy[index], self.occupancy[minInd]
				self.sift_down( minInd )
			
		  
	def assign_jobs(self):
		# TODO: replace this code with a faster algorithm.
		self.assigned_workers = [None] * len(self.jobs)
		self.start_times = [None] * len(self.jobs)
		self.occupancy = []	# this is the priority queue (a binary min heap)
		for i in range( self.num_workers ) :	# initialize the priority queue
			self.occupancy.append( (i,0) )	# which thread, and finish time initialized to 0
		for i, CPU_time in enumerate(self.jobs) :
			resource = self.replace_min( CPU_time )
			self.assigned_workers[i] = resource[0]
			self.start_times[i] = resource[1]
			# pp_b_heap( self.occupancy)

	def solve(self):
		self.read_data()
		self.assign_jobs()
		self.write_response()

def pp_b_heap( heap ) :
	# list that is a binary heap --> nothing, but pretty prints
	count = 0
	start = 0
	while 2**count < len( heap ) :
		print( heap[start: (start + 2**count) ] )
		count += 1
		start = 2**count - 1

		
if __name__ == '__main__':
	# pdb.set_trace()
	job_queue = JobQueue()
	job_queue.solve()

