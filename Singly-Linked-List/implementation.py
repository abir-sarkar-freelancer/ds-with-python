# First we need to define the node class
# this node class constructor will initiate new nodes 
# that will be added to the linked list

# two instance variables are needed 
# one is data, to store the data corresponding to node
# another one is next, to store the pointer to next node
class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
# Now We are going to define the LinkedList class
# it will have one instance variable to be precise 
# and that is head
# head is the reference to the very first node
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    # the value of head is initially None
    # Now we need to define 
    # an instance method to append 
    # node to the linked list
    
    def append(self, data):
        # we are going to append 
        # this node to the list

        new_node = Node(data) 

        # but first we need to check 
        # whether the list is empty or not
        # it can be done simply by checking 
        # if head is point to None or not

        if self.head is None:
            # list is empty
            self.head = new_node
            return f"{data} appended"
        
        # if list is not empty
        current_node = self.head
        # till the next Node is not None
        while current_node.next:
            # we continue traversing the list
            current_node = current_node.next
            
        # finally append the new_node at the end
        current_node.next = new_node
        
    # Now Prepend
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return f"{data} prepended"
    
    # Insert After a Given Node 
    def insert_after(self, given_node, data):
        new_node = Node(data)
        
        if not given_node:
            print("The Node Does Not Exist")
            return
        
        new_node.next = given_node.next
        given_node.next = new_node
        
        return "Successfully Inserted"
    
    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return f"{key} deleted"
        
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
            
        if current_node is None:
            return f"{key} does not exist"
        
        prev_node.next = current_node.next
        current_node = None
        
        return f"{key} deleted"   
    
    # let's define a method to print the entire List
    def show_items(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
