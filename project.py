#Sagheer Ahmad
# Classes used in Thompsons Construction

class  State:
	#Every state has 0, 1, or 2 edges from it
    edges = []
	
	#label for the arrows, none means epsilon
    label = None
	
    #Constructor for the class
    # Constructor function
    # Constructor is inside class state
    def __init__(self, label=None, edges=[]):
        self.edges = edges
        self.label = label

# An NFA is represented by its initial and accept states.
class Frag:
	#start state of the NFA fragment
    start = None
	#Accept state of the NFA fragment
    accept = None

    # Constructor function
    # Constructor is inside class nfa
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept
		
def shunt(infix):
	#The input
	infix = "(a|b).c*"
	print("The input is: ", infix )
	#Expected output = "ab|c*."

	#Convert input to a stackish list
	infix = list(infix)[::-1]

	#operator stack
	opers = []

	#output list
	postfix = []

	#Operator precedence
	prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

	#loop through the input one character at a time
	while infix:
		#pop a characterfro the input
		c = infix.pop()

		#decide what to do
		#if c is an operator or a bracket - do something
		if c == '(':
			#Push an open bracket to the opers stack
			opers.append(c)
		elif c == ')':
			#pop the operator stack until you find an open bracket
			while opers[-1] != '(':
				postfix.append(opers.pop())
			#get rid of the open bracket
			opers.pop()
		elif c in prec:
			#push any operators on the opers stack with the higher prec to the output
			while opers and  prec[c] < prec[opers[-1]]:
				postfix.append(opers.pop())
			#push c to the operator stack
			opers.append(c)
		else:
			#typically, we just push the character to the output
			postfix.append(c)

	#pop all operators to the output
	while opers:
		postfix.append(opers.pop())


	#Convert output list to string
	return ''.join(postfix)

def match(regex, s):
	#this function will return true if and only if the regular expression
	#regex (fully) matches the string s. It returns false otherwise
	
	#compile the regular expression into nfa
	nfa = regex_compile(regex)
	#ask the nfa if it matches the string s.
	return nfa
	

match("a.b|b*", "bbbbbbb")
