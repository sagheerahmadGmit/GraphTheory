#Sagheer Ahmad
# Classes used in Thompsons Construction

class  state:
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
