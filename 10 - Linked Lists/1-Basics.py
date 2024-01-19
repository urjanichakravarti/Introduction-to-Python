class Node:
    # we will use the Node class to create a linked list
    #  __init__ method that initializes the linked list with an empty head
    def __init__(self, data):
        # The __init__ method takes a parameter data and initializes the data attribute with the provided value.
        self.data = data
        # The next attribute is initialized to None. This indicates that when a node is created,
        # it initially doesn't point to any other node (since it's the last node in the list).
        self.next = None

class LinkedList:
    def __init__(self):
        # The __init__ method initializes the head attribute to None.
        # This indicates that when a linked list is created, it starts with an empty list (no nodes yet).
        self.head = None

    # we have created an insertAtBegin() method to insert a node at the beginning of the linked list,
    # an insertAtIndex() method to insert a node at the given index of the linked list,
    # and insertAtEnd() method inserts a node at the end of the linked list.

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position += 1
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index doesn't exist")

    def insertAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    # the updateNode() function is to update a node at a given index
    # the remove_first_node() function is to remove the first node of a ll
    # the remove_last_node() function is to remove the last node of a ll

    def updateNode(self, val, index):
        position = 0
        current_node = self.head
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position += 1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index is not present")

    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return
        current_node = self.head

        while current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def printll(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

# Create a new Linked List
llist = LinkedList()

# Add Nodes
llist.insertAtEnd('a')
print("Node Data")
llist.printll()
llist.insertAtEnd('b')
print("Node Data")
llist.printll()
llist.insertAtBegin('c')
print("Node Data")
llist.printll()
llist.insertAtIndex('d', 2)
print("Node Data")
llist.printll()