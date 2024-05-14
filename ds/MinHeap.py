class MinHeap:
    length: int = 0
    data: list
    
    def __init__(self):
        self.length = 0
        self.data = []

    def insert(self, value: int) -> None:
        pass

    def delete(self) -> int:
        pass

    def _heapifyUp(self):
        pass

    def _heapifyDown(self):
        pass

    def _parent(self, idx: int) -> int:
        return (idx - 1) // 2

    def _leftChild(self, idx: int) -> int:
        return (idx * 2) + 1

    def _rightChild(self, idx: int) -> int:
        return (idx * 2) + 2
    