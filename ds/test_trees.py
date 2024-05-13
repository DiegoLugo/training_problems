import unittest
from Tree import Node


class TestTree(unittest.TestCase):
    head: Node = Node(
        value=20,
        right=Node(
            value=50,
            right=Node(
                value=100,
                right=None,
                left=None,
            ),
            left=Node(
                value=30,
                right=Node(
                    value=45,
                    right=None,
                    left=None,
                ),
                left=Node(
                    value=29,
                    right=None,
                    left=None,
                )
            ),
        ),
        left=Node(
            value=10,
            right=Node(
                value=15,
                right=None,
                left=None,
            ),
            left=Node(
                value=5,
                right=Node(
                    value=7,
                    right=None,
                    left=None,
                ),
                left=None,
            )
        )
    )

    head2: Node = Node(
        value=20,
        right=Node(
            value=50,
            right=Node(
                value=100,
                right=None,
                left=None,
            ),
            left=Node(
                value=30,
                right=None,
                left=Node(
                    value=29,
                    right=Node(
                        value=45,
                        right=None,
                        left=None,
                    ),
                    left=None,
                )
            ),
        ),
        left=Node(
            value=10,
            right=Node(
                value=15,
                right=None,
                left=None,
            ),
            left=Node(
                value=5,
                right=Node(
                    value=7,
                    right=None,
                    left=None,
                ),
                left=None,
            )
        )
    )

    def test_pre(self):
        self.assertEqual(self.head.traversePreOrder(self.head), [
            20,
            10,
            5,
            7,
            15,
            50,
            30,
            29,
            45,
            100,
        ])

    def test_in(self):
        self.assertEqual(self.head.traverseInOrder(self.head), [
            5,
            7,
            10,
            15,
            20,
            29,
            30,
            45,
            50,
            100,
        ])

    def test_post(self):
        self.assertEqual(self.head.traversePostOrder(self.head), [
            7,
            5,
            15,
            10,
            29,
            45,
            30,
            100,
            50,
            20,
        ])

    def test_bfs(self):
        self.assertEqual(self.head.breadthFirstSearch(self.head, 45), True)
        self.assertEqual(self.head.breadthFirstSearch(self.head, 7), True)
        self.assertEqual(self.head.breadthFirstSearch(self.head, 69), False)

    def test_compare_trees(self):
        self.assertEqual(self.head.compareTrees(self.head, self.head), True)
        self.assertEqual(self.head.compareTrees(self.head, self.head2), False)


if __name__ == '__main__':
    unittest.main()
