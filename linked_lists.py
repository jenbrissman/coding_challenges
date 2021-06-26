# find and insert a node a certain index:

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def find(self, node_name):

        current = self.head

        while current is not None:
            if current.data == node_name:
                return current

            current = current.next
        
        return current
    
    def previous(self, node_name):
        current = self.head
        previous = None
        
        while current is not None:
            if current.data == node_name:
                return previous
            previous = current
            current = current.next

        return previous   
            
  # node_name = "berry" ; new_node = Node()
    def append_after(self, node_name, new_node):
      # find the instance by node_name
      # append the new_node to the found instance
        previous = self.find(node_name)
        new_node.next = previous.next
        previous.next = new_node
    
    # llist.add_before(berry_node, banana_node)

    def add_before(self, node_name, new_node):
        #find node we want to append before
        #append new node before that node
        # node_name = 'd'
        # new_node = newNode('b')
        # current ll
        # a -> d
        # outcome ll
        # a -> b -> d 
        firstNode = self.previous(node_name)
        lastNode = self.find(node_name)

        firstNode.next = new_node
        new_node.next = lastNode
      
        
    
    def remove(self, node_name):
        #node_name = 'b'
        #current llist
        #a -> b -> c -> d
        if self.head == None:
          return

        if self.head.data == node_name:
          self.head = self.head.next
          return

        nodeToRemove = self.find(node_name)
        previousNode = self.previous(node_name)
        previousNode.next = nodeToRemove.next

        if nodeToRemove.next == None:
          self.tail = previousNode




        # if self.head == node_name:
        #     self.head = self.head.next

        # current = self.head

        # while current.next is not None:

        #     if current.next == node_name:
        #         current.next = current.next.next
        #         if current.next is None:
        #             self.tail = current
        #             return
        #     else:
        #         current = current.next


    def print_ll(self):
        current = self.head
        
        # while current is not None:
        #     print(current.data)
        #     current = current.next
        concat = []
        while current is not None:
            concat.append(current.data)
            current = current.next
        print(" -> ".join(concat))


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# apple_node = Node("apple")
# berry_node = Node("berry")
# cherry_node = Node("cherry")
# pineapple_node = Node("pineapple")
# banana_node = Node("banana")

# jens_ll = LinkedList()

# jens_ll.head = apple_node
# apple_node.next = berry_node
# berry_node.next = cherry_node
# jens_ll.tail = cherry_node

# print("This is the linked list before add_before method:")
# jens_ll.print_ll()

# jens_ll.add_before(berry_node, banana_node)
# print(apple_node.next.data)

# print("This is the linked list after add_before method:")
# jens_ll.print_ll()

# jens_ll.remove(apple_node)

# print("This is jens_ll after removing apple")
# jens_ll.print_ll()

# print("before")
# print(jens_ll.find("jen"))

# print("append")
# jens_ll.append_after("apple", pineapple_node)
# print("after")
# print(jens_ll.find("jen"))

# homework: print out whole linked list. like jens_ll.print. iterate through and print out list
# "apple -> berry -> cherry"
# insert (anywhere) or insert_before or 
#insert_after, remove, append. 
# prepend and append

# print(jens_ll.previous("cherry").data)

#TODO = finish the append before
#TODO  = remove a node from list

ll = LinkedList()

node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('d')

ll.head = node1
print("This should print 'a'")
ll.print_ll()

print("append_after")
ll.append_after('a', node4)
print("This should print a -> d")
ll.print_ll()

print("add_before")
ll.add_before('d', node2)
print("This should print a -> b -> d")
ll.print_ll()

print("append_after")
ll.append_after('b', node3)
print("This should print a -> b -> c -> d")
ll.print_ll()

print("find")
n = ll.find('d')
if n:
  print("This should be d: ", n.data)
else:
  print("something is wrong there is no node")

print("previous")
n = ll.previous('c')
if n:
  print("This should be b:", n.data)
else:
  print("something is wrong there is no node")

print("remove")
ll.remove('c')
print("This should print a -> b -> d")
ll.print_ll()

print("remove")
ll.remove('d')
print("This should print a -> b")
ll.print_ll()

print("remove")
ll.remove('a')
print("This should print b")
ll.print_ll()
