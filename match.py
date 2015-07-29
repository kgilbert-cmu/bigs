from graph import Graph

men = { "Xavier" : ["Alice", "Brenda", "Claire"],
        "Yuri" : ["Brenda", "Alice", "Claire"],
        "Zoran" : ["Alice", "Brenda", "Claire"]}
women = { "Alice" : ["Yuri", "Xavier", "Zoran"],
          "Brenda" : ["Xavier", "Yuri", "Zoran"],
          "Claire" : ["Xavier", "Yuri", "Zoran"]}

graph = Graph(men, women)
bipartite = graph.perfectMatching()
for pair in bipartite:
	print pair, "...", bipartite[pair]

