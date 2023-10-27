# ---
# title: LinkedList
# tags: [CodingChallenges, Python, LinkedList]
# created: '2023-10-27'
# ---

# ## Problem Description

# A LinkedList is a linear data structure, in which the elements are not stored at contiguous memory locations. In simple words, the elements are linked using pointers.

# In this task, you are required to implement a LinkedList in Python, including methods to add a node after a specific node and to represent the LinkedList.

# ## Solution

# This problem can be solved using the concept of Nodes and LinkedList data structure. A Node has two properties: data and next. The LinkedList has a head, which points to the first Node in the list. 

# ```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
      
    def add_after(self, target_node_data, new_node):
      if self.head is None:
        raise Exception("List is empty")

      for node in self:
        if node.data == target_node_data:
          new_node.next = node.next
          node.next = new_node
          return

    raise Exception("Node with data '%s' not found" % target_node_data)

# >>> llist = LinkedList()
# >>> llist.add_after("a", Node("b"))
# Exception: List is empty

# >>> llist = LinkedList(["a", "b", "c", "d"])
# >>> llist
# a -> b -> c -> d -> None

# >>> llist.add_after("c", Node("cc"))
# >>> llist
# a -> b -> c -> cc -> d -> None

# >>> llist.add_after("f", Node("g"))
# Exception: Node with data 'f' not found

      
      
# >>> llist = LinkedList()
# >>> llist
# None

# >>> first_node = Node("a")
# >>> llist.head = first_node
# >>> llist
# a -> None

# >>> second_node = Node("b")
# >>> third_node = Node("c")
# >>> first_node.next = second_node
# >>> second_node.next = third_node
# >>> llist
# a -> b -> c -> None