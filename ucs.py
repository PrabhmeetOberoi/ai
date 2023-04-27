class UCS:

  def __init__(self, graph, start_position, target):
    self.graph = graph
    self.start = graph.find_node(start_position)
    self.target = graph.find_node(target)
    self.opened = []
    self.closed = []
    self.number_of_steps = 0


  def calculate_distance(self, parent, child):
    for neighbor in parent.neighbors:
      if neighbor[0] == child:
        distance = parent.heuristic_value + neighbor[1]
        if distance < child.heuristic_value:
          child.parent = parent
          return distance
        
        return child.heuristic_value

  
  def insert_to_list(self, list_category, node):
    if list_category == "open":
      self.opened.append(node)
    else:
      self.closed.append(node)
  

  def remove_from_opened(self):
    self.opened.sort()
    # for n in self.opened:
    #   print(f"({n},{n.heuristic_value})", end = " ")
    # print("\n")
    node = self.opened.pop(0)
    self.closed.append(node)
    return node


  def opened_is_empty(self):
    return len(self.opened) == 0


  def get_old_node(self, node_value):
    for node in self.opened:
      if node.value == node_value:
        return node
    return None 
      

  def calculate_path(self, target_node):
    path = [target_node.value]
    node = target_node.parent
    while True:
      path.append(node.value)
      if node.parent is None:
        break
      node = node.parent
    path.reverse()
    return path
  
  
  def search(self):
    # The heuristic value of the starting node is zero
    self.start.heuristic_value = 0
    # Add the starting point to opened list
    self.opened.append(self.start)

    while True:
      self.number_of_steps += 1

      if self.opened_is_empty():
        print(f"No Solution Found after {self.number_of_steps} steps!!!")
        break
        
      selected_node = self.remove_from_opened()
      # print(f"Selected Node {selected_node}")
      # check if the selected_node is the solution
      if selected_node == self.target:
        path = self.calculate_path(selected_node)
        return path, self.number_of_steps

      # extend the node
      new_nodes = selected_node.extend_node()

      # add the extended nodes in the list opened
      if len(new_nodes) > 0:
        for new_node in new_nodes:
          
          new_node.heuristic_value = self.calculate_distance(selected_node, new_node)
          if new_node not in self.closed and new_node not in self.opened:
            self.insert_to_list("open", new_node)
          elif new_node in self.opened and new_node.parent != selected_node:
            old_node = self.get_old_node(new_node.value)
            if new_node.heuristic_value < old_node.heuristic_value:
              new_node.parent = selected_node
              self.insert_to_opened(new_node)

from cmath import inf


class Node:
    def __init__(self, value, neighbors=None):
        self.value = value
        self.heuristic_value = inf
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors
        self.parent = None


    def has_neighbors(self):
        if len(self.neighbors) == 0:
            return False
        return True


    def number_of_neighbors(self):
        return len(self.neighbors)

    def add_neighboor(self, neighboor):
        self.neighbors.append(neighboor)
    

    def extend_node(self):
        children = []
        for child in self.neighbors:
            children.append(child[0])
        return children
    

    def __gt__(self, other):
        if isinstance(other, Node):
            if self.heuristic_value > other.heuristic_value:
                return True
            if self.heuristic_value < other.heuristic_value:
                return False
            return self.value > other.value
            

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value
        return self.value == other


    def __str__(self):
        return self.value
        

class Graph:
    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes


    def add_node(self, node):
        self.nodes.append(node)


    def find_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node 
        return None


    def add_edge(self, value1, value2, weight=1):
        node1 = self.find_node(value1)        
        node2 = self.find_node(value2)

        if (node1 is not None) and (node2 is not None):
            node1.add_neighboor((node2, weight))
            node2.add_neighboor((node1, weight))
        else:
            print("Error: One or more nodes were not found")


    def number_of_nodes(self):
        return f"The graph has {len(self.nodes)} nodes"


    def are_connected(self, node_one, node_two):
        node_one = self.find_node(node_one)
        node_two = self.find_node(node_two)

        for neighboor in node_one.neighbors:
            if neighboor[0].value == node_two.value:
                return True
        return False


    def __str__(self):
        graph = ""
        for node in self.nodes:
            graph += f"{node.__str__()}\n" 
        return graph
    
def run():
    graph = Graph()
    graph.add_node(Node('V1'))
    graph.add_node(Node('V2'))
    graph.add_node(Node('V3'))
    graph.add_node(Node('V4'))
    graph.add_node(Node('V5'))
    graph.add_node(Node('V6'))
    
    graph.add_edge('V1', 'V2', 9)
    graph.add_edge('V1', 'V3', 4)
    graph.add_edge('V2', 'V3', 2)
    graph.add_edge('V2', 'V4', 7)
    graph.add_edge('V2', 'V5', 3)
    graph.add_edge('V3', 'V4', 1)
    graph.add_edge('V3', 'V5', 6)
    graph.add_edge('V4', 'V5', 4)
    graph.add_edge('V4', 'V6', 8)
    graph.add_edge('V5', 'V6', 2)

    alg = UCS(graph, "V1", "V6")
    path, path_length = alg.search()
    print(" -> ".join(path))
    print(f"Length of the path: {path_length}")

if __name__ == '__main__':
  run()
