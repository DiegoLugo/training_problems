#1823. Find the Winner of the Circular Game
#https://leetcode.com/problems/find-the-winner-of-the-circular-game/
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circular_list = [x for x in range(1, n + 1)]
        current_position = 0
        while len(circular_list) > 1:
            current_position = (current_position + (k - 1)) % len(circular_list)
            circular_list.pop(current_position)
        return circular_list.pop()


if __name__ == '__main__':
    print(Solution().findTheWinner(5, 2))
    #print(Solution().findTheWinner(6, 5))
