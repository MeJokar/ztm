class Graph():
    def __init__(self) -> None:
        self.numberOfNodes = 0 
        self.adjacentList = {}
        pass
    def addVertex(self, node):
        if node not in self.adjacentList:
            self.adjacentList.update({node: []})
        self.numberOfNodes +=1

    def addEdge(self, node1, node2):
        if node1 in self.adjacentList and node2 in self.adjacentList:
            if node2 not in self.adjacentList[node1]:
                self.adjacentList[node1].append(node2)
                self.adjacentList[node2].append(node1)
                return
            else:
                return "Edge already exists"
        else: 
            return 'node does not exist'
        
    def show_connections(self):
        for node in self.adjacentList:
            print(f'{node} -->> {" ".join(map(str, self.adjacentList[node]))}')
        

if __name__ == "__main__":
    my_graph = Graph()
    my_graph.addVertex(1)
    my_graph.addVertex(2)
    my_graph.addVertex(3)
    my_graph.addEdge(1,2)
    my_graph.addEdge(1,3)
    my_graph.addEdge(2,3)
    my_graph.show_connections()
    print(my_graph.adjacentList)