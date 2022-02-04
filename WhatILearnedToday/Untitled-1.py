class TreeNode():
    def __init__(self,data, left,right):
        self.data = data
        self.left = left
        self.right = right

#Bottoms Up
node1 = TreeNode(1, None, None)
node3 = TreeNode(3, None, None)
node2 = TreeNode(2, node1, node3)

node6 = TreeNode(6, None, None)
node9 = TreeNode(9, None, None)
node7 = TreeNode(7, node6, node9)

root = TreeNode(4, node2, node7)

    #        4
    #      /   \
    #     2     7
    #    / \   / \
    #   1   3 6   9

#
#Recursion
#DFS
#Base Case: if root is False
#Recursion Function: if current node exists 
#return .data of current node + recursive result

def sum(root):
    if root == None:
        return 0
    
    return root.data + sum(root.left) + sum(root.right)
