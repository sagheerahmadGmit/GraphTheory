#Sagheer Ahmad
# Classes used in Thompsons Construction

class  State:	
    """ A state with one or two arrows, all arrows labeled by label """
    #Constructor
    def __init__(self, label=None, edges=[]):
        #Every state has 0,1, or 2 edges from it
        self.edges = edges
        #label for the arrows, none means epsilon
        self.label = label

# An NFA is represented by its initial and accept states.
class Frag:
    """ An NFA fragment with a start and accept state """
    # Constructor
    def __init__(self, start, accept):
        #Start state of the NFA Fragment
        self.start = start
        #Accept state of the NFA Fragment
        self.accept = accept
		
def shunt(infix):
    """ Return the infix regular expression in postfix """

    #Convert input to a stackish list
    infix = list(infix)[::-1]

    #operator stack and the output list
    opers = []

    #output list for regular expression
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

def regex_compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]

    nfa_stack = []

    while postfix:
        #pop a character from postfix
        c = postfix.pop()
        
        if c == '*':
            #pop a single fragment of the stack
            frag = nfa_stack.pop()
	    #create new start and accept state
            accept = State()
            #point old accept state to the new one
            start = State(edges=[frag.start, accept])
            #point the arrows
            frag.accept.edges = [frag.start,accept]
            #create new instance of fragments to represent the new nfa
            newfrag = Frag(start,accept)
        elif c == '.':
            #pop two fragments of the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            #point frag2's accept state at frag1's start state
            frag2.accept.edges.append(frag1.start)
            #create new instance of fragment to represent the new nfa
            newfrag = Frag(frag2.start, frag1.accept)
        elif c == '|':
            #pop 2 fragments of the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            #create new start and accept state
            accept = State()
            start = State(edges=[frag2.start, frag1.start])
            #point the old accept state to the new one
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)
            #create new instance of fragment to represent the new nfa
            newfrag = Frag(start, accept)
        else:
            #create new start and accept state
            accept = State()
            start = State(label=c, edges=[accept])
            #create new instance of fragment to represent the new nfa
            newfrag = Frag(start, accept)

	#push the new nfa to the nfa_stack
        nfa_stack.append(newfrag)

    #The NFA stack should only have exactly one  nfa on it
    return nfa_stack.pop()


#Add a state to the set and follow al the E arrows
def followes(state, current):
    #only do something when we haven't already seen the state
    if state not in current:
        #put the state itself into the state
        current.add(state)
        #See whether state is labelled be E
        if state.label is None:
            #Loop through the states pointed to by this state
            for x in state.edges:
                #follow all of their epsilons too
                followes(x, current)


def match(regex, s):
    #this function will return true if and only if the regular expression
    #regex (fully) matches the string s. It returns false otherwise
    
    #compile the regular expression into nfa
    nfa = regex_compile(regex)

    # try to match the regular expression to the string s.
    #the current set of states
    current = set()
    #add the first state, and follow all of epsilon arrows
    followes(nfa.start, current)
    #the previuos set of states
    previous = set()

    #loop through characters in s
    for c in s:
        previous = current
        #creat a new empty set for states we're about to be in
        current = set()
        #loop through the previous states
        for state in previous:
            #only follow arrows not labeled by E (epsilon)
            if state.label is not None:
                #if the label of the state is = to the character we've read
                if state.label == c:
                    #add the state(s) at the end of the arrow to current.
                   followes(state.edges[0], current)

    #ask the nfa if it matches the string s.
    return nfa.accept in current	

if __name__ == "__main__":
    print(match("a.b|b*", "bbbbbbb"))
