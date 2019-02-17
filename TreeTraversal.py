''' 


'''

def inOrder(node):
    if node != None:
        inOrder(node.left)
        visit(node)
        inOrder(node.right)

def preOrder(node):
    if node != None:
        visit(node) # visit the current node first ("pre") before children
        preOrder(node.left)
        preOrder(node.right)

def postOrder(node):
    if node != None:
        postOrder(node.left)
        postOrder(node.right)
        visit(node) # we want to visit the node after ("post") checking children