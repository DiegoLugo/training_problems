class Node():
    def __init__(self, value=int | None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def walkPreOrder(self, node, path) -> list:
        if node is None:
            return path

        path.append(node.value)
        self.walkPreOrder(node.left, path)
        self.walkPreOrder(node.right, path)

        return path

    def traversePreOrder(self, node) -> list:
        return self.walkPreOrder(node, [])

    def walkInOrder(self, node, path) -> list:
        if node is None:
            return path

        self.walkInOrder(node.left, path)
        path.append(node.value)
        self.walkInOrder(node.right, path)

        return path

    def traverseInOrder(self, node) -> list:
        return self.walkInOrder(node, [])

    def walkPostOrder(self, node, path) -> list:
        if node is None:
            return path

        self.walkPostOrder(node.left, path)
        self.walkPostOrder(node.right, path)
        path.append(node.value)

        return path

    def traversePostOrder(self, node) -> list:
        return self.walkPostOrder(node, [])

    def breadthFirstSearch(self, node, item) -> bool:
        queue = [node]

        while len(queue) > 0:
            next = queue.pop(0)
            if next.value == item:
                return True
            if next.left:
                queue.append(next.left)
            if next.right:
                queue.append(next.right)
        return False

    def compareTrees(self, a, b) -> bool:
        if (a is None and b is None):
            return True
        if (a is None or b is None):
            return False
        if (a.value != b.value):
            return False

        return self.compareTrees(a.left, b.left) and self.compareTrees(a.right, b.right)
