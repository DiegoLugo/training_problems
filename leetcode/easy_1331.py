# 1331. Rank Transform of an Array
# https://leetcode.com/problems/rank-transform-of-an-array
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedset = sorted(set(arr))

        ranks = {num: rank + 1 for rank, num in enumerate(sortedset)}
        #result = [ranks[num] for num in arr]
        return [ranks[num] for num in arr]
    
if __name__ == '__main__':

    print(Solution().arrayRankTransform([40,10,20,30]))