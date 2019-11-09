from BinaryTree import Node


top_root = Node(100)
left_node = Node(50)
right_node = Node(200)
left_left_node = Node(25)
left_left_left_node = Node(12)

left_left_node.set_left_node(left_left_left_node)
left_node.set_left_node(left_left_node)

right_left_node = Node(150)
right_right_node = Node(250)
right_node.set_left_node(right_left_node)
right_node.set_right_node(right_right_node)

top_root.set_left_node(left_node)
top_root.set_right_node(right_node)

max_depth = 0


def print_tree(root: Node, depth: int):
    if root:
        print_tree(root.get_left_node(), depth + 1)
        print('Value (Depth) -> %i (%i)' % (root.get_value(), depth))
        print_tree(root.get_right_node(), depth + 1)

    if max_depth < depth:
        max_depth = depth


if __name__ == '__main__':
    top_depth = 0
    print_tree(top_root, top_depth)
