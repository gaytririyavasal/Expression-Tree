#  File: ExpressionTree.py

#  Description: The following program creates an expression tree based upon a given expression. At the end, the result, prefix version, and postfix version of the expression are printed.

#  Student Name: Gaytri Riya Vasal

#  Course Name: CS 313E

#  Unique Number: 86439

#  Date Created: 7/2/22

#  Date Last Modified: 7/4/22

import sys

operators = ['+', '-', '*', '/', '//', '%', '**'] # Establish list of operators

class Stack(object): # The following class defines a Stack object
    
    def __init__(self):
        self.stack = [] # Self.stack is initialized as an empty list

    def push(self, data):
        self.stack.append(data) # Data is appended to the stack by pushing

    def pop(self):
        if not self.is_empty():
            return self.stack.pop() # The last value of the stack is returned
        else:
            return None # If the stack is empty, return None, as there is no value to return

    def is_empty(self):
        return len(self.stack) == 0 # If the length of the stack is 0, the stack is empty

class Node(object): # The class below defines a node
    
    def __init__(self, data=None, lChild=None, rChild=None): # Data, lChild, and rChild are set to None by default if not inputted
        
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree(object): # The following class works with the expression tree
    
    def __init__(self):
        self.root = None # Initialize self.root at None

    # This function takes in the input string expr and
    # creates the expression tree
    
    def create_tree(self, expr):

        self.root = Node() # Set self.root to a Node object
        currentnode = self.root # Initially set current node to self.root
        treestack = Stack() # Create stack and assign it to treestack variable

        lstexpr = expr.split() # Split all elements of expression and store them in lstexpr
        
        for item in lstexpr: # Traverse each element of the list
            
            if item == '(': # If token is a left parenthesis, add new node as left child, push current node on the stack, and equate current node to the left child
                
                currentnode.lChild = Node()
                treestack.push(currentnode)
                currentnode = currentnode.lChild

            elif item == ')': # If token is a right parenthesis, equate current node to the parent node
                
                if not treestack.is_empty():
                    currentnode = treestack.pop()

            elif item in operators: # If token is an operator, set the current node’s data value equal to the operator, push current node on the stack, add new node as the right child, and equate current node to right child
                
                currentnode.data = item
                treestack.push(currentnode)
                currentnode.rChild = Node()
                currentnode = currentnode.rChild

            else: # If token is an operand, assign the current node’s data value to the operand and equate the current node to the parent node
                
                currentnode.data = item
                currentnode = treestack.pop()

    # This function applies an operator to values 'x' and 'y' and then returns the result
    
    def process(self, operator, x, y):
        
        return eval(x + operator + y)

    # This function should evaluate the tree's expression
    # Returns the value of the expression after being calculated
    
    def evaluate(self, aNode):

        if aNode.data is None: # If the tree is empty, 0 should be returned
            return 0

        if aNode.lChild is None and aNode.rChild is None: # If this is a leaf node, return the float of the node's data
            return float(aNode.data)

        l_child_sum = str(self.evaluate(aNode.lChild)) # Evaluate left tree
        r_child_sum = str(self.evaluate(aNode.rChild)) # Evaluate right tree

        return self.process(aNode.data, l_child_sum, r_child_sum) # Apply the operator at the root to the values set in the previous lines

    # This function should generate the preorder notation of the tree's expression
    # Returns a string of the expression written in preorder notation
    
    def pre_order(self, aNode):
        
        po_str = '' # Initialize po_str to an empty string
        
        if aNode != None: # If the root is not None, add data and a white space to po_str; also recursively traverse left and right subtree and add to po_str
            
            po_str += aNode.data
            po_str += ' '
            po_str += self.pre_order(aNode.lChild)
            po_str += self.pre_order(aNode.rChild)

        return po_str # Return final value of po_str

    # This function should generate the postorder notation of the tree's expression
    # Returns a string of the expression written in postorder notation
    
    def post_order(self, aNode):
        
        po_list = [] # Initialize po_list to an empty list
        
        po_str = '' # Initialize po_str to an empty string
        
        if aNode != None: # If the root is not None, recursively traverse left and right subtree and append values to po_list accordingly; afterwards, append data to po_list
            
            po_list.append(self.post_order(aNode.lChild))
            po_list.append(self.post_order(aNode.rChild))
            po_list.append(aNode.data)
            
        for element in po_list: # Traverse each element in po_list
            
            if element is not None: # If the element is not None, add it to po_str
                po_str += element

        po_list = po_str.split() # Split all elements in po_str
        
        po_str2 = '' # Initialize po_str2 to an empty string
        
        for element in po_list: # Traverse each element in po_list
            
            po_str2 += element # Add element to po_str2
            po_str2 += ' ' # Add white space to po_str2
            
        return po_str2 # Return final output of po_str2

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
