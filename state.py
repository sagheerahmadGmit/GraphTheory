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
		
myinstance = State(label='a', edges=[])
anotherinstance = State(edges=[myinstance])
myfrag = Frag(myinstance, anotherinstance)

print(myinstance.label)
print(anotherinstance.edges[0])
print(myfrag)
