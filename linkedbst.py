"""
File: linkedbst.py
Author: YOUR NAME GOES HERE
"""

from utils.abstractcollection import AbstractCollection
from utils.bstnode import BSTNode
from math import log
from utils.linkedstack import LinkedStack
from utils.linkedqueue import LinkedQueue

class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)
        
    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s
        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        return self.preorder()

    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        modCount = self.getModCount()
        lyst = list()
        def recurse(node):
            if node != None:
                lyst.append(node.data)
                recurse(node.left)
                recurse(node.right)
        recurse(self._root)
        # return iter(lyst)
        for item in lyst:
            yield item
            if modCount != self.getModCount():
                raise AttributeError("Mutations not allowed in a for loop") 
            
        #pre order task 2 using a stack or queue
        # queue = LinkedQueue()
        # lyst = []
        # probe = self._root
        # while True:
        #     if probe != None:
        #         queue.add(probe)
        #         probe = probe.left
        #     elif not queue.isEmpty():
        #         probe = queue.last
        #         lyst.append(queue.pop())

        # probe = self._root
        # while True:
        #     if probe.left.left == None:
        #         queue.add(probe.left)
        #         queue.add(probe.right)
        #         while not queue.isEmpty():
        #             lyst.append(queue.pop())
        #     elif probe != None: 
        #         queue.add(probe)
        #         probe = probe.left
        #     elif queue.isEmpty():
        #         probe = probe.right

        stack = LinkedStack()
        lyst =[]
        probe = self._root
        while True:
            if probe.left.left ==None:
                lyst.append(probe.data)
                lyst.append(probe.left.data)
                lyst.append(probe.right.data)
                if stack.isEmpty():
                    return lyst
                probe = stack.pop()
                probe= probe.right
            else:
                stack.push(probe.data)
                lyst.append(probe.data)
                probe = probe.left

                


        

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        modcount = self.getModCount()
        lyst = [] 
        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)
        recurse(self._root)
        return iter(lyst)
        for item in lyst:
            yield item
            if modCount != self.getModCount():
                raise AttributeError("Mutations not allowed in a for loop") 
            

        #code try for stack . Task 2
        stack =LinkedStack()
        modCount = self.getModCount()
        probe = self._root
        lyst= []
        while True: 
            if probe != None:
                stack.push(probe)
                probe = probe.left
            elif not stack.isEmpty():
                probe = stack.pop()
                lyst.append(probe)
                yield probe.data
                if modCount != self.getModCount():
                    raise AttributeError("Mutations not allowed in a for loop") 
                probe = probe.right
            else:
                break 






    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        modcount = self.getModCount()
        lyst = [] 
        def recurse(node):
            if node != None:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node.data)
        recurse(self._root)
        return iter(lyst)
        for item in lyst:
            yield item
            if modCount != self.getModCount():
                raise AttributeError("Mutations not allowed in a for loop") 

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        modcount = self.getModCount()
        lyst=[]
        def recurse(node, level):
            if node != None:
                lyst.append((node.data, level))
                recurse(node.left, level+1)
                recurse(node.right, level+1)
        recurse(self._root, 0)
        lyst.sort(key=lambda a: a[1])
        final_lyst=[]
        for item in lyst:
            final_lyst.append(item[0])
        return iter(final_lyst)
    

        #queue try. Given by professor
        modCount = self.getModCount()
        queue = LinkedQueue()
        if not self.isEmpty():
            queue.add(self._root)

        while not queue.isEmpty():
            temp = queue.pop()
            yield temp.data
            if modCount != self.getModCount():
                raise AttributeError("Mutations not allowed")
            if temp.left != None:
                queue.add(temp.left)
            if temp.right != None:
                queue.add(temp.right)


        
            

            


    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""
        def recurse(node):
            if node is None:
                return None
            elif  item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)
        return recurse(self._root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self.resetSizeAndModCount()

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item's position 
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal, 
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
            # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1
        self.incModCount()

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        # Helper function to adjust placement of an item
        def liftMaxInLeftSubtreeToTop(top):
            # Replace top's datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top's left subtree
            #       has been removed
            # Post: top.data = maximum value in top's left subtree
            parent = top
            currentNode = top.left
            while not currentNode.right == None:
                parent = currentNode
                currentNode = currentNode.right
            top.data = currentNode.data
            if parent == top:
                top.left = currentNode.left
            else:
                parent.right = currentNode.left

        # Begin main part of the method
        if self.isEmpty(): return None
        
        # Attempt to locate the node containing the item
        itemRemoved = None
        preRoot = BSTNode(None)
        preRoot.left = self._root
        parent = preRoot
        direction = 'L'
        currentNode = self._root
        while not currentNode == None:
            if currentNode.data == item:
                itemRemoved = currentNode.data
                break
            parent = currentNode
            if currentNode.data > item:
                direction = 'L'
                currentNode = currentNode.left
            else:
                direction = 'R'
                currentNode = currentNode.right
                
        # Return None if the item is absent
        if itemRemoved == None: return None
        
        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not currentNode.left == None \
           and not currentNode.right == None:
            liftMaxInLeftSubtreeToTop(currentNode)
        else:
            
        # Case 2: The node has no left child
            if currentNode.left == None:
                newChild = currentNode.right
                
        # Case 3: The node has no right child
            else:
                newChild = currentNode.left
                
        # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = newChild
            else:
                parent.right = newChild
            
        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self._size -= 1
        self.incModCount()
        if self.isEmpty():
            self._root = None
        else:
            self._root = preRoot.left
        return itemRemoved

    def replace(self, item, newItem):
        """Precondition: item == newItem.
        Raises: KeyError if item != newItem.
        If item is in self, replaces it with newItem and
        returns the old item, or returns None otherwise."""
        if item != newItem: raise KeyError("Items must be equal")
        probe = self._root
        while probe != None:
            if probe.data == item:
                oldData = probe.data
                probe.data = newItem
                return oldData
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    def height(self):
        """Returns the height of the tree (the length of the longest path
        from the root to a leaf node).
        When len(t) < 2, t.height() == 0."""
        def recurse(node):
            if node == None:
                return 0
            else:
                return 1 + max(recurse(node.left), recurse(node.right))
        height = recurse(self._root)
        if not self.isEmpty():
            height -= 1
        return height

    def isBalanced(self):
        """Returns True if the tree is balanced or False otherwise.
        t is balanced iff t.height() < 2 * log2(len(t) + 1) - 1."""
        height = self.height()
        if self.height() < 2 * math.log2(len(self) + 1) - 1:
            return True
        else:
            return False
    

    def rebalance(self):
        """Rebalances the tree."""
        if not self.isBalanced():
            items = sorted(self.inorder_traversal())
            self.clear()
            return self.rebuild()
            
 

    def rebuild(self, items, star, end):
        """Add items from list to tree. Visits midpoint to add items
           then recurses with the left half of the list and then right"""
        if start > end:
            return None
        mid = (start + end) // 2
        node = BSTNode(items[mid])
        node.left = self._rebuild(items, start, mid -1)
        node.right = self._rebuild(items, mid + 1, end)
        return node
        
