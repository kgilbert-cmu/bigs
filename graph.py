men = { "Xavier" : ["Alice", "Brenda", "Claire"], 
		"Yuri" : ["Brenda", "Alice", "Claire"],
		"Zoran" : ["Alice", "Brenda", "Claire"]}
women = { "Alice" : ["Yuri", "Xavier", "Zoran"],
		  "Brenda" : ["Xavier", "Yuri", "Zoran"],
		  "Claire" : ["Xavier", "Yuri", "Zoran"]}

def ignore(sequence, value):
	return [x for x in sequence if x != value]

class Graph:
	free = {}
	men = {}       # who can he still propose to?
	women = {}     # who would she prefer?
	marriages = {}  # who is she engaged to?
	
	def __init__(self, men, women):
		self.free.update({m: True for m in men})
		self.free.update({w: True for w in women})
		self.men = men
		for w in women:
			pref = women[w]
			rank = range(0, len(pref))
			self.women[w] = dict(zip(pref, rank))
	
	def luckyBachelor(self):
		for m in self.men.keys():
			if self.free[m]:
				return m
		return None
	
	def hisJuliet(self, romeo):
		preferences = self.men[romeo]
		if len(preferences) > 0:
			return preferences[0]
		else:
			raise KeyError(romeo + " has no preferences left.")
	
	def propose(self, romeo, juliet):
		self.men[romeo] = ignore(self.men[romeo], juliet)
		self.free[romeo] = False
		self.free[juliet] = False 
		self.marriages[juliet] = romeo
	
	def reject(self, juliet, tybalt):
		self.men[tybalt] = ignore(self.men[tybalt], juliet)
	
	def divorce(self, juliet):
		paris = self.marriages.pop(juliet)
		self.free[paris] = True
		self.free[juliet] = True
	
	def perfectMatching(self):
		while True:
			romeo = self.luckyBachelor()
			if romeo == None:
				return self.marriages
			juliet = self.hisJuliet(romeo)
            # if juliet is free
                # assign m and w to be engaged
            # if juliet prefers romeo to her paris
                # assign m and w to be engaged
                # assign m' to be free
            # else
                # juliet rejects romeo
			if self.free[juliet]:
				self.propose(romeo, juliet)
			elif self.women[juliet][romeo] < self.women[juliet][self.marriages[juliet]]:
				self.divorce(juliet)
				self.propose(romeo, juliet)
			else:
				self.reject(juliet, romeo)

graph = Graph(men, women)
bipartite = graph.perfectMatching()
for pair in bipartite:
	print pair, "...", bipartite[pair]

