# """
# Node class to keep track of
# the data internal to individual nodes
# """
# class Node:
#   def __init__(self, key):
#     self.key = key
#     self.left = None
#     self.right = None

# """
# A tree class to keep track of things like the
# balance factor and the rebalancing logic
# """
# class AVLTree:
#   def __init__(self, node=None):
#     self.node = node
#     # init height to -1 because of 0-indexing
#     self.height = -1
#     self.balance = 0

#   """
#   Display the whole tree. Uses recursive def.
#   """
#   def display(self, level=0, pref=''):
#     self.update_height()  # Update height before balancing
#     self.update_balance()
    
#     if self.node != None: 
#       print ('-' * level * 2, pref, self.node.key,
#         f'[{self.height}:{self.balance}]',
#         'L' if self.height == 0 else ' ')
#       if self.node.left != None:
#         self.node.left.display(level + 1, '<')
#       if self.node.right != None:
#         self.node.right.display(level + 1, '>')

#   """
#   Computes the maximum number of levels there are
#   in the tree
#   """
#   def update_height(self):
#     pass

#   """
#   Updates the balance factor on the AVLTree class
#   """
#   def update_balance(self):
#     pass

#   """
#   Perform a left rotation, making the right child of this
#   node the parent and making the old parent the left child
#   of the new parent. 
#   """
#   def left_rotate(self):
#     pass

#   """
#   Perform a right rotation, making the left child of this
#   node the parent and making the old parent the right child
#   of the new parent. 
#   """
#   def right_rotate(self):
#     pass

#   """
#   Sets in motion the rebalancing logic to ensure the
#   tree is balanced such that the balance factor is
#   1 or -1
#   """
#   def rebalance(self):
#     pass
    
#   """
#   Uses the same insertion logic as a binary search tree
#   after the value is inserted, we need to check to see
#   if we need to rebalance
#   """
#   def insert(self, key):
#     pass

# Python code to insert a node in AVL tree 

# Generic tree node class 
class TreeNode(object): 
	def __init__(self, val): 
		self.val = val 
		self.left = None
		self.right = None
		self.height = 1

# AVL tree class which supports the 
# Insert operation 
class AVL_Tree(object): 

	# Recursive function to insert key in 
	# subtree rooted with node and returns 
	# new root of subtree. 
	def insert(self, root, key): 
	
		# Step 1 - Perform normal BST 
		if not root: 
			return TreeNode(key) 
		elif key < root.val: 
			root.left = self.insert(root.left, key) 
		else: 
			root.right = self.insert(root.right, key) 

		# Step 2 - Update the height of the 
		# ancestor node 
		root.height = 1 + max(self.getHeight(root.left), 
						self.getHeight(root.right)) 

		# Step 3 - Get the balance factor 
		balance = self.getBalance(root) 

		# Step 4 - If the node is unbalanced, 
		# then try out the 4 cases 
		# Case 1 - Left Left 
		if balance > 1 and key < root.left.val: 
			return self.rightRotate(root) 

		# Case 2 - Right Right 
		if balance < -1 and key > root.right.val: 
			return self.leftRotate(root) 

		# Case 3 - Left Right 
		if balance > 1 and key > root.left.val: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 

		# Case 4 - Right Left 
		if balance < -1 and key < root.right.val: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 

		return root 

	def leftRotate(self, z): 

		y = z.right 
		T2 = y.left 

		# Perform rotation 
		y.left = z 
		z.right = T2 

		# Update heights 
		z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

		# Return the new root 
		return y 

	def rightRotate(self, z): 

		y = z.left 
		T3 = y.right 

		# Perform rotation 
		y.right = z 
		z.left = T3 

		# Update heights 
		z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

		# Return the new root 
		return y 

	def getHeight(self, root): 
		if not root: 
			return 0

		return root.height 

	def getBalance(self, root): 
		if not root: 
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right) 

	def preOrder(self, root): 

		if not root: 
			return

		print("{0} ".format(root.val), end="") 
		self.preOrder(root.left) 
		self.preOrder(root.right) 


# Driver program to test above function 
myTree = AVL_Tree() 
root = None

root = myTree.insert(root, 10) 
root = myTree.insert(root, 20) 
root = myTree.insert(root, 30) 
root = myTree.insert(root, 40) 
root = myTree.insert(root, 50) 
root = myTree.insert(root, 25) 

"""The constructed AVL Tree would be 
			30 
		/ \ 
		20 40 
		/ \	 \ 
	10 25 50"""

# Preorder Traversal 
print("Preorder traversal of the", 
	"constructed AVL tree is") 
myTree.preOrder(root) 
print() 

# This code is contributed by Ajitesh Pathak 
