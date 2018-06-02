# python3
import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def preComputeHashes( text, P , p, x ) :
	# (string, int ) --> list of ints
	L = len( text ) 
	H = [0] * ( L - P + 1 )
	S = text[-P::]
	H[L-P] = PolyHash( S, p, x )
	y = 1
	for i in range( P ) :
		y = y * x % p
	for i in range( L - P - 1, -1, -1 ) :
		H[i] = ( H[i+1] * x + ord( text[i] ) - y * ord( text[i + P ]) ) % p
	return H
	
def PolyHash( text , p , x ) :
	# string --> int
	hash = 0
	for char in text[::-1] :
		hash = (hash * x + ord(char) ) % p
	return hash
	
def get_occurrences(pattern, text):
	# ( string, string ) --> list of ints
	p = 3000017		# thanks Wolfram Alpha
	random.seed( 0 )
	x = random.randint( 1,  p-1 )
	L = len( text )
	result = []
	pHash = PolyHash( pattern, p, x )
	tHashes = preComputeHashes( text, len(pattern) , p, x)
	for i in range(len(text) - len(pattern) + 1) :
		if pHash != tHashes[i] :
			continue
		if text[i:i + len(pattern)] == pattern :
			result.append( i )
	return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

