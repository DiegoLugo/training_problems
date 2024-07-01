#1550. Three Consecutive Odds
#https://leetcode.com/problems/three-consecutive-odds/
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        for number in arr:
            if number%2 != 0:
                count += 1
            else: 
                count = 0
            if count == 3:
                return True
        return False
    
if __name__ == '__main__':
    print(Solution().threeConsecutiveOdds([2,6,4,1]))
    # print(Solution().threeConsecutiveOdds([1,1,1,0,0,1]))