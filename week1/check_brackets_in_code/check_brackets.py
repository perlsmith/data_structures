# python3

import sys
import pdb

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
	text = sys.stdin.read()

	opening_brackets_stack = []
	#pdb.set_trace()
	for i, next in enumerate(text):
		if next == '(' or next == '[' or next == '{':
			# Process opening bracket, write your code here
			brk = Bracket( next, i )
			opening_brackets_stack.append( brk )

		if next == ')' or next == ']' or next == '}':
			# Process closing bracket, write your code here
			if len( opening_brackets_stack) > 0 and opening_brackets_stack[ -1 ].Match(next) :
				del opening_brackets_stack[ -1 ]
			else :
				print( i+1 )
				exit()
	
	if len( opening_brackets_stack) != 0 :
		print( opening_brackets_stack[-1].position + 1 )
	else :
		print( "Success")

    # Printing answer, write your code here
