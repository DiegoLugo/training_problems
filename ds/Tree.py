class Node():
    def __init__(self, value= int | None, left=None, right=None) -> None:
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
