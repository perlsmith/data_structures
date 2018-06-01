# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
	# nothing --> list of Query objects
    n = int(input())	# read the first line, get N
	# N times, read a line, split on space, send the words to Query.__init__ for processing :)
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
	result = []
	# Keep list of all existing (i.e. not deleted yet) contacts.
	contacts = [''] * 10000000	# 10^7 is given as the max number of contacts..
	for cur_query in queries:
		if cur_query.type == 'add':
			# if we already have contact with such number,
			# we should rewrite contact's name
			contacts[cur_query.number] = cur_query.name
		elif cur_query.type == 'del':
			contacts[cur_query.number] = ''
		else:
			response = contacts[cur_query.number]
			if response == '' :
				response = 'not found'
			result.append(response)
	return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

# mission - improve speed - using direct addressing..
