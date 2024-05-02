class Node:
    value: any
    prev: any

    def __init__(self, value) -> None:
        self.value = value
        self.prev = None

# FIFO


class Stack:
    __head: Node
    length: int

    def __init__(self) -> None:
        self.__head = None
        self.length = 0

    def push(self, item: any) -> None:
        self.length += 1
        new_node = Node(value=item)
        if not self.__head:
            self.__head = new_node
            return
        new_node.prev = self.__head
        self.__head = new_node

    def pop(self) -> any | None:
        if not self.__head:
            return None
        self.length -= 1
        popped = self.__head
        popped.prev = None
        self.__head = self.__head.prev
        return popped.value

    def peek(self) -> any | None:
        return self.__head.value if self.__head else None
