# ---
# title: Sorting Dwarfs Wearing Red and Blue Hats
# tags: [CodingChallenges, Python, LinkedList, Sorting]
# created: '2023-10-28'
# ---

# ## Problem Description

# In a dark cave, there live dwarfs wearing red and blue hats. They don't know the color of their own hats and they can't tell each other. They need to come out one by one and gather with dwarfs wearing the same color hat. What rules should the dwarfs set?

# ## Solution

# This problem can be solved using a linked list in Python. Each dwarf can follow these two rules:
# 1. Always stand between a dwarf in a red hat and a dwarf in a blue hat.
# 2. If there are only red or blue hats, stand anywhere.

# To continuously add to the list quickly, we use a linked list. 
# The time complexity of a typical operation that inserts a new node at a specific position in a linked list is O(n), 
# but in this code, we keep track of the last added red and blue hats, so the time complexity of inserting a new node is O(1). 
# The overall time complexity is O(N), which solves the problem.

# ```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_red = None
        self.last_blue = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            if data == 'r':
                if self.last_red is not None:
                    new_node.next = self.last_red.next
                    self.last_red.next = new_node
                else:
                    new_node.next = self.head
                    self.head = new_node
                self.last_red = new_node
            else:  # data == 'b'
                if self.last_blue is not None:
                    new_node.next = self.last_blue.next
                    self.last_blue.next = new_node
                else:
                    new_node.next = self.head
                    self.head = new_node
                self.last_blue = new_node

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next

def solution(hats):
    llist = LinkedList()
    for hat in hats:
        llist.insert(hat)
    llist.printLL()

hats = ['r','r','b','r','b','b','r','b','r','r','r','b','r','b','b','r','b','b','r','b','r','r','r','b','r','b','r','r','b','r','b','b','r','b','r','r','r','b','r','b','b','r','b','b','r','b','r','r','r','b','r','b','r','r','b','r','b','b','r','b','r','r','r','b','r','b','b','r','b','b','r','b','r','r','r','b','r','b','r','r','b','r','b','b','r','b','r','r','r','b','r','b','b','r','b','b','r','b','r','r','r','b','r','b','r','r','b','r','b','b','r','b','r','r','r','b','r','b','b','r','b','b','r','b','r','r','r','b','r','b','r','r','b','r','b','b','r','b','r','r','r','b','r','b','b','r','b','b','r','b','r','r','r','b','r','b','r','r','b','r','b','b','r','b','r','r','r','b','r','b','b','r','b','b','r','b','r','r','r','b','r','b','r','r','b','r','b','b','r','b','r','r','r','b','r','b','b','r','b','b','r','b','r','r','r','b','r','b','r','r','b','r','b','b']
solution(hats)
