# """Each ListNode holds a reference to its previous node
# as well as its next node in the List."""
# class ListNode:
#   def __init__(self, value, prev=None, next=None):
#     self.value = value
#     self.prev = prev
#     self.next = next

#   """Wrap the given value in a ListNode and insert it
#   after this node. Note that this node could already
#   have a next node it is point to."""
#   def insert_after(self, value):
#     current_next = self.next
#     self.next = ListNode(value, self, current_next)
#     if current_next:
#       current_next.prev = self.next

#   """Wrap the given value in a ListNode and insert it
#   before this node. Note that this node could already
#   have a previous node it is point to."""
#   def insert_before(self, value):
#     current_prev = self.prev
#     self.prev = ListNode(value, current_prev, self)
#     if current_prev:
#       current_prev.next = self.prev

#   """Rearranges this ListNode's previous and next pointers
#   accordingly, effectively deleting this ListNode."""
#   def delete(self):
#     if self.prev:
#       self.prev.next = self.next
#     if self.next:
#       self.next.prev = self.prev

# """Our doubly-linked list class. It holds references to
# the list's head and tail nodes."""
# class DoublyLinkedList:
#   def __init__(self, node=None):
#     self.head = node
#     self.tail = node
#     self.length = 1 if node is not None else 0

#   def __len__(self):
#     return self.length

#   def add_to_head(self, value):
#     pass

#   def remove_from_head(self):
#     pass

#   def add_to_tail(self, value):
#     pass

#   def remove_from_tail(self):
#     pass

#   def move_to_front(self, node):
#     pass

#   def move_to_end(self, node):
#     pass

#   def delete(self, node):
#     pass
    
#   def get_max(self):
#     pass


#another example---------------------------------------------------
#RUN USING PYTHON, (not 3)
# A complete working Python program to demonstrate all 
# insertion methods 

# A linked list node 
class Node: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.next = None
		self.prev = None

# Class to create a Doubly Linked List 
class DoublyLinkedList: 
    
	# Constructor for empty Doubly Linked List 
	def __init__(self): 
		self.head = None

	# Given a reference to the head of a list and an 
	# integer, inserts a new node on the front of list 
	def push(self, new_data): 

		# 1. Allocates node 
		# 2. Put the data in it 
		new_node = Node(new_data) 

		# 3. Make next of new node as head and 
		# previous as None (already None) 
		new_node.next = self.head 

		# 4. change prev of head node to new_node 
		if self.head is not None: 
			self.head.prev = new_node 

		# 5. move the head to point to the new node 
		self.head = new_node 

	# Given a node as prev_node, insert a new node after 
	# the given node 
	def insertAfter(self, prev_node, new_data): 

		# 1. Check if the given prev_node is None 
		if prev_node is None: 
			print ("the given previous node cannot be NULL")
			return

		# 2. allocate new node 
		# 3. put in the data 
		new_node = Node(new_data) 

		# 4. Make net of new node as next of prev node 
		new_node.next = prev_node.next

		# 5. Make prev_node as previous of new_node 
		prev_node.next = new_node 

		# 6. Make prev_node ass previous of new_node 
		new_node.prev = prev_node 

		# 7. Change previous of new_nodes's next node 
		if new_node.next is not None: 
			new_node.next.prev = new_node 

	# Given a reference to the head of DLL and integer, 
	# appends a new node at the end 
	def append(self, new_data): 

		# 1. Allocates node 
		# 2. Put in the data 
		new_node = Node(new_data) 

		# 3. This new node is going to be the last node, 
		# so make next of it as None 
		new_node.next = None

		# 4. If the Linked List is empty, then make the 
		# new node as head 
		if self.head is None: 
			new_node.prev = None
			self.head = new_node 
			return

		# 5. Else traverse till the last node 
		last = self.head 
		while(last.next is not None): 
			last = last.next

		# 6. Change the next of last node 
		last.next = new_node 

		# 7. Make last node as previous of new node 
		new_node.prev = last 

		return

	# This function prints contents of linked list 
	# starting from the given node 
	def printList(self, node): 

		print ("\nTraversal in forward direction")
		while(node is not None): 
			print " %d " % (node.data), 
			last = node 
			node = node.next

		print ("\nTraversal in reverse direction")
		while(last is not None): 
			print " %d " % (last.data), 
			last = last.prev 

# Driver program to test above functions 

# Start with empty list 
llist = DoublyLinkedList() 

# Insert 6. So the list becomes 6->None 
llist.append(6) 

# Insert 7 at the beginning. 
# So linked list becomes 7->6->None 
llist.push(7) 

# Insert 1 at the beginning. 
# So linked list becomes 1->7->6->None 
llist.push(1) 

# Insert 4 at the end. 
# So linked list becomes 1->7->6->4->None 
llist.append(4) 

# Insert 8, after 7. 
# So linked list becomes 1->7->8->6->4->None 
llist.insertAfter(llist.head.next, 8) 

print ("Created DLL is: "), 
llist.printList(llist.head) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
