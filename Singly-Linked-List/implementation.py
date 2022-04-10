
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
    # Now we need to define an instance method to append node to the linked list
    
    def append(self, data):
        new_node = Node(data) # we are going to append this node to the list
        # but first we need to check whether the list is empty or not
        # it can be done simply by checking if head is point to None or not
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
    
    def delete_at_pos(self, pos):
        current_node = self.head
        
        if pos == 0:
            self.head = current_node.next
            current_node = None
            return
        
        index = 1
        prev = None
        while index <= pos and current_node:
            prev = current_node
            current_node = current_node.next
            index += 1
        
        if current_node is None:
            return f"No element found at {pos}"
        
        prev.next = current_node.next
        current_node = None
        
        return f"Element at {pos} has been deleted" 
            
        
        
    def len_iterative(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
            
        return count
    
    
    def len_recursive(self, node):
        # base case
        if node is None:
            return 0
        
        return 1 + self.len_recursive(node.next)
    
    def swap_nodes(self, key1, key2):

        if key1 == key2:
            return
        current_node = self.head
        
        prev_node = None
        prev_node_key_1 = None
        prev_node_key_2 = None
        node_key_1 = None
        node_key_2 = None
        
        flag = 0
        
        while current_node:
            
            if current_node.data == key1:
                # print("GOT Key 1")
                prev_node_key_1 = prev_node
                # print(prev_node_key_1.data)
                node_key_1 = current_node
                # print(node_key_1.data)
                flag += 1

                if flag >= 2:
                    # print("Out 1")
                    break
                
            if current_node.data == key2:
                # print("GOT Key 2")
                prev_node_key_2 = prev_node
                # print(prev_node_key_2.data)
                node_key_2 = current_node
                # print(node_key_2.data)
                flag += 1

                if flag >= 2:
                    # print("Out 2")
                    break
                
            prev_node = current_node
            current_node = current_node.next
            

        if not node_key_1 or not node_key_2:
            return

        
        if prev_node_key_1:
            prev_node_key_1.next = node_key_2
        else:
            self.head = node_key_2

        if prev_node_key_2:
            prev_node_key_2.next = node_key_1
        else:
            self.head = node_key_1

        node_key_1.next, node_key_2.next = node_key_2.next, node_key_1.next

        return "Swap Done"
        
    def swap_nodes_alt(self, key1, key2):
        if key1 == key2:
            return

        current_node = self.head

        prev_node = None
        node_key_1 = None
        node_key_2 = None
        
        flag = 0

        while current_node:
            
            if current_node.data == key1:
                # print("GOT Key 1")
                # prev_node_key_1 = prev_node
                # print(prev_node_key_1.data)
                node_key_1 = current_node
                # print(node_key_1.data)
                flag += 1

                if flag >= 2:
                    # print("Out 1")
                    break
                
            if current_node.data == key2:
                # print("GOT Key 2")
                # prev_node_key_2 = prev_node
                # print(prev_node_key_2.data)
                node_key_2 = current_node
                # print(node_key_2.data)
                flag += 1

                if flag >= 2:
                    # print("Out 2")
                    break
                
            prev_node = current_node
            current_node = current_node.next


        if not node_key_1 or not node_key_2:
            return

        node_key_1.data, node_key_2.data = node_key_2.data, node_key_1.data

        return "Swap Done"


        
            
    
    # let's define a method to print the entire List
    def show_items(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
