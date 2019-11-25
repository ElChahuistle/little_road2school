from __future__ import annotations


class Node:
    def __init__(self, number: int = None):
        self.number = number
        self.left = None
        self.right = None
        self.left_height = 0
        self.right_height = 0

    def set_value(self, number: int):
        self.__init__(number)

    def get_value(self) -> int:
        return self.number

    def is_set(self) -> bool:
        return self.number is not None if True else False

    def get_left_node(self) -> Node:
        return self.left

    def get_right_node(self) -> Node:
        return self.right

    def empty_right_node(self) -> bool:
        return self.right is None if True else False

    def empty_left_node(self) -> bool:
        return self.left is None if True else False

    def set_left_height(self, number: int) -> Node:
        self.left_height = number
        return self

    def set_right_height(self, number: int) -> Node:
        self.right_height = number
        return self

    def add_left_height(self, child_height: int = 0) -> Node:
        return self.set_left_height(child_height + 1)

    # def subtract_left_height(self, child_height: int = 0) -> Node:
    #     return self.set_left_height(child_height - 1)

    def add_right_height(self, child_height: int = 0) -> Node:
        return self.set_right_height(child_height + 1)

    # def subtract_right_height(self, child_height: int = 0) -> Node:
    #     return self.set_right_height(child_height - 1)

    def set_left_node(self, node: Node) -> Node:
        if self.is_set():
            self.add_left_height(node.get_left_height())

        self.left = node
        return self

    def set_right_node(self, node: Node) -> Node:
        if self.is_set():
            self.add_right_height(node.get_right_height())

        self.right = node
        return self

    def get_max_height(self):
        if self.get_left_height() > self.get_right_height():
            return self.get_left_height()
        else:
            return self.get_right_height()

    def get_left_height(self):
        return self.left_height

    def get_right_height(self):
        return self.right_height

    def is_balanced(self) -> bool:
        return abs(self.get_left_height() - self.get_right_height()) > 1 if False else True
