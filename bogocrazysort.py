import random
from random import shuffle
import copy

#Use a parnet child relationship to rnadom assign nodes next to each other so that there is no need to examine them again

class Node:
    def __init__(self, id):
        self.id = id           # Unique identifier for the node
        self.parents = []      # List of parent nodes
        self.children = []     # List of child nodes

    # Method to add a child to this node
    def addChild(self, child):
        self.children.append(child)  # Use append, not push
        child.parents.append(self)

    # Method to remove this node
    def remove(self):
        # Remove this node from all its children's parents lists
        for child in self.children:
            child.parents = [parent for parent in child.parents if parent != self]

        # Optionally: Set parents and children to empty arrays
        self.parents = []
        self.children = []

    def removeChild(self, childID):
        return False
    
    def parentChild(self, parentID):
        return False

    # Method to check if the node has no parents (is a root node)
    def isRoot(self):
        return len(self.parents) == 0  # Use len() to get the length of the list

    # Define a __repr__ method for better output
    def __repr__(self):
        return f"Node({self.id})"

# Function to check if the list of nodes is sorted by their id
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i].id > arr[i + 1].id:
            return False
    return True

def find_and_link(list, id1, id2):
    nodesToLink = []
    for items in list:
        if(items.id == id2):
            nodesToLink.append(items)
    for items in list:
        if(items.id == id1):
            for i in nodesToLink:
                items.addChild(i)

allNodes = []

# Create an initial node and add it to the list
a = Node(25)
allNodes.append(a)

for i in range(3):
    a = Node(random.randint(1, 200))
    allNodes.append(a)

while True:
    new_list = copy.deepcopy(allNodes)
    shuffle(new_list)
    duplicate_list = []

    #Check each node to see it is a root node and then adds it to duplicate_list
    while(len(new_list) != 0):
        for i in new_list:
            if(i.isRoot() == 0):
                duplicate_list.append(i)
                new_list.remove(i)
    
    if is_sorted(duplicate_list):
        print(duplicate_list)  # This will now show [Node(25)]
        break
    print("Fail")
    print(duplicate_list)
    previousItem = "initial"
    for i in duplicate_list:
        if(previousItem == "initial"):
            previousItem = i
        else:
            if(i.id > previousItem.id):
                find_and_link(allNodes, i.id, previousItem.id)
            previousItem = i
    #break
