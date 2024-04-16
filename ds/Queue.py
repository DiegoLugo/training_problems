class Node:
    value: any
    next: any

    def __init__(self, value) -> None:
        self.value = value
        self.next = None

# FIFO
class Queue:
    __head: Node
    __tail: Node
    length: int

    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.length = 0

    def enqueue(self, item: any) -> None:
        new_node = Node(value=item)
        self.length += 1
        if not self.__tail:
            self.__head = self.__tail = new_node
        self.__tail.next = new_node
        self.__tail = new_node

    def deque(self) -> any | None:
        if not self.__head:
            return None
        self.length -= 1
        dequed = self.__head
        if self.length == 0:
            self.__tail = None
        dequed.next = None
        self.__head = self.__head.next
        return dequed.value

    def peek(self) -> any | None:
        return self.__head.value if self.__head else None
