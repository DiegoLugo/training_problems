class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    head: Node
    tail: Node
    length: int

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insertAt(self, item: any, index: int) -> None:
        if index > self.length:
            return Exception("damn")
        if index == self.length:
            return self.append(item)
        if index == 0:
            return self.prepend(item)
        node = Node(item)
        self.length += 1
        curr = self.head
        for i in range(0, index):
            curr = curr.next
        node.next = curr
        node.prev = curr.prev
        curr.prev.next = node
        curr.prev = node
        return

    def removeAt(self, index: int) -> any:
        node = self.getAt(index)
        if node:
            self.length -= 1
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if self.head == node:
                self.head = node.next
            if self.tail == node:
                self.tail = node.prev
            return node.val
        return None

    def remove(self, item: any) -> any:
        curr = self.head
        while curr is not None:
            if curr.val == item:
                break
            curr = curr.next

        if curr is None:
            return None

        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None
            return curr.val

        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        if curr == self.head:
            self.head = curr.next
        if curr == self.tail:
            self.tail == curr.prev
        return curr.val

    def append(self, item: any) -> None:
        node = Node(item)
        self.length += 1
        if self.length == 1:
            self.head = self.tail = node
            return
        
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        return

    def prepend(self, item: any) -> None:
        node = Node(item)
        self.length += 1
        if self.head:
            node.next = self.head
            self.head.prev = node
        if self.head is None:
            self.tail = node
        self.head = node
        return

    def get(self, index: int) -> any:
        node = self.getAt(index)
        if node:
            return node.val
        return None

    def getAt(self, index: int) -> Node | None:
        curr = self.head
        for i in range(0, index):
            if curr is None:
                break
            curr = curr.next
        return curr
