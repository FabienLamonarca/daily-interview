class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def display_node(node):
    print(node.value)
    if node.left:
        display_node(node.left)
    if node.right:
        display_node(node.right)


def invert(node):
    left = node.left
    right = node.right

    node.right = left
    node.left = right

    if node.right:
        invert(node.right)

    if node.left:
        invert(node.left)

root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')

display_node(root)
# a b d e c f
invert(root)
print("invert:")
display_node(root)
