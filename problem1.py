
#Binary Tree Level Order Traversal 

#(https://leetcode.com/problems/binary-tree-level-order-traversal/)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node:
    def __init__(self, data, level):
        self.data = data
        self.next = None
        self.level = level
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == self.tail == None
    
    def dequeue(self):
        # if the LL is empty
        if self.isEmpty():
            return None
        #if the head and the tail point in the same node (only 1 node present)
        elif self.head == self.tail:
            node = self.head
            self.head = None
            self.tail = None
            return node
        node = self.head
        self.head = self.head.next
        return node
    
    def enqueue(self, node):
        if self.isEmpty():
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node
        return

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        output = [ ]
        
        queue = Queue()
        root_node = Node(root, 0)
        queue.enqueue( root_node )
        
        while not queue.isEmpty():
            node = queue.dequeue()
            node_level = node.level
            
            if node_level >= len(output):
                output.append([])
            #print(output)
            output[node_level].append( node.data.val )
            
            if node.data.left:
                queue.enqueue( Node(node.data.left, node_level + 1) )
            
            if node.data.right:
                queue.enqueue( Node(node.data.right, node_level + 1) )
                
        return output
            
        