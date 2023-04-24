class Graph():
    def __init__(self) -> None:
        self.numberOfNodes = 0 
        self.adjacentList = 0
        pass
    def addVertex(self, node):
        if node not in self.adjacentList:
            self.adjacentList.update({node: []})
        self.numberOfNodes +=1

    def addEdge(self, node1, node2):
        if node1 in self.adjacentList and node2 in self.adjacentList:
            if node2 not in self.adjacency_list[node1]:
                self.adjacentList[node1].append[node2]
                self.adjacentList[node2].append[node1]
                return
            else 
            return "Edge already exists"
        else: 
            return 'node does not exist'
        
        
        