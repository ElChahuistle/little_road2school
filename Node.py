from __future__ import annotations


class Node:
    def __init__(self, number: int = None):
        self.number = number
        self.left = None
        self.right = None

    def set_value(self, number: int):
        self.__init__(number)

    def get_value(self) -> int:
        return self.number

    def set_left_node(self, node: Node) -> Node:
        self.left = node
        return self

    def set_right_node(self, node: Node) -> Node:
        self.right = node
        return self

    def get_left_node(self) -> Node:
        return self.left

    def get_right_node(self) -> Node:
        return self.right

    def empty_right_node(self) -> bool:
        return self.right is None if True else False

    def empty_left_node(self) -> bool:
        return self.left is None if True else False


class NodePP(Node):
    def __init__(self, number: int = None):
        super().__init__(number)
        self.left_height = 0
        self.right_height = 0

    def get_left_height(self):
        return self.left_height

    def get_right_height(self):
        return self.right_height

    def set_left_height(self, number: int) -> NodePP:
        self.left_height = number
        return self

    def set_right_height(self, number: int) -> NodePP:
        self.right_height = number
        return self

    def add_left_height(self) -> NodePP:
        return self.set_left_height(self.get_left_height() + 1)

    def subtract_left_height(self) -> NodePP:
        return self.set_left_height(self.get_left_height() - 1)

    def add_right_height(self) -> NodePP:
        return self.set_right_height(self.get_right_height() + 1)

    def subtract_right_height(self) -> NodePP:
        return self.set_right_height(self.get_right_height() - 1)

    def set_left_node(self, node: NodePP = None) -> NodePP:
        if node:
            self.add_left_height()
        else:
            self.subtract_left_height()

        self.left = node

        return self

    def set_right_node(self, node: NodePP = None) -> NodePP:
        if node:
            self.add_right_height()
        else:
            self.subtract_right_height()

        self.right = node

        return self

    def is_balanced(self) -> bool:
        return abs(self.get_left_height() - self.get_right_height()) > 1 if False else True
