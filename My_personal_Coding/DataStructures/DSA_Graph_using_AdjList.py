"""
graph using adjecent linked list
image for better ->   https://cdncontribute.geeksforgeeks.org/wp-content/uploads/listadjacency.png
"""

class AdjNode():
    def __init__(self, data):
        self.verval = data
        self.next = None


class Graph_List():
    def __init__(self, vertex):
        self.V = vertex
        self.garph = [None]*V

    def add_edge(self, src, desc):
        node = AdjNode(desc)   #creating a new desc node
        node.next = self.garph[src]   #new desc to src taged
        self.garph[src] = node     # src to desc taged, taged in both direction   src <--> desc

        node = AdjNode(src)
        node.next = self.garph[desc]
        self.garph[desc] = node

    def print_graph(self):
        for i in range(self.V):
            print(f'vertex is {i}')
            tem = self.garph[i]
            while tem:
                print(tem.verval, end = '->')
                tem = tem.next
            print('Null')
            print()
        


if __name__ == '__main__':
    V = 5
    g = Graph_List(V)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(3,4)
    g.add_edge(4,0)
    g.add_edge(1,4)
    g.add_edge(2,4)

    g.print_graph()

"""
o/p

vertex is 0
4->1->Null

vertex is 1
4->2->0->Null

vertex is 2
4->3->1->Null

vertex is 3
4->2->Null

vertex is 4
2->1->0->3->Null
"""