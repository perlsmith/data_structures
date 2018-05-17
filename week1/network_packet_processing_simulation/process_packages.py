# python3
import pdb

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
	def __init__(self, size):
		self.size = size
		self.finish_time = []

	def Process(self, request):
	# request object --> tuple of bool, int
		# write your code here
		if self.size == len( self.finish_time ) and self.finish_time[0] > request.arrival_time :
			return Response(True, -1)	# dropped packet
		else :
			if len( self.finish_time ) > 0 :
				start = max( self.finish_time[-1], request.arrival_time )
				if self.finish_time[0] <= request.arrival_time and len( self.finish_time) == 1 :
					del self.finish_time[0]	# dequeue 
				self.finish_time.append( start + request.process_time )
				return Response( False, start )
			else :
				self.finish_time.append( request.arrival_time + request.process_time )
				return Response( False, request.arrival_time )
			
			

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)
	
    pdb.set_trace()
    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
