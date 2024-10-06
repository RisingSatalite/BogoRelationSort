import random
from random import shuffle
import copy

class Node:
    def __init__(self, id):
        self.id = id  # Unique identifier for the node
        self.parents = []  # List of parent nodes
        self.children = []  # List of child nodes

    def addChild(self, child):
        # Check if this creates a cycle, the system will never do this so no worries
        #if self.creates_cycle(child):
            #print(f"Cannot link {self.id} to {child.id}, as it would create a cycle.")
            #return
        self.children.append(child)
        child.parents.append(self)

    # Check if adding a child would create a cycle
    def creates_cycle(self, child):
        return child.isAncestorOf(self)

    # Check if a node is an ancestor of this node
    def isAncestorOf(self, node, visited=None):
        if visited is None:
            visited = set()
        if self in visited:
            return False
        visited.add(self)

        if self == node:
            return True
        # Check each parent to see if any is an ancestor
        return any(parent.isAncestorOf(node, visited) for parent in self.parents)

    def remove(self):
        for child in self.children:
            child.parents = [parent for parent in child.parents if parent != self]
        self.parents = []
        self.children = []

    def isRoot(self):
        #print("Getting root")
        return not self.parents  # Simple check for root

    def __repr__(self):
        return f"Node({self.id})"

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i].id > arr[i + 1].id:
            return False
    return True

def find_and_link(nodes, id1, id2):
    parent_node = next((node for node in nodes if node.id == id1), None)
    child_nodes = [node for node in nodes if node.id == id2]
    for child in child_nodes:
        parent_node.addChild(child)

# Create nodes and add them to the list
allNodes = []

a = Node(25)
allNodes.append(a)

for i in range(100):
    allNodes.append(Node(random.randint(1, 200)))

while True:
    new_list = copy.deepcopy(allNodes)
    shuffle(new_list)
    duplicate_list = []

    while new_list:
        # Only append root nodes
        for i in new_list[:]:
            if i.isRoot():
                duplicate_list.append(i)
                i.remove()
                new_list.remove(i)

    if is_sorted(duplicate_list):
        print(duplicate_list)
        break

    print("Fail")
    print(duplicate_list)
    
    previousItem = None
    for i in duplicate_list:
        if previousItem:
            if i.id < previousItem.id:
                find_and_link(allNodes, i.id, previousItem.id)
            elif previousItem.id > i.id:
                find_and_link(allNodes, previousItem.id, i.id)
        previousItem = i
