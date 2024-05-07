# 27. Remove Element
# https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ocurrences = 0
        i = len(nums) - 1
        j = 0
        while i >= j:
            if nums[i] == val:
                i -= 1
                ocurrences += 1
            else:
                aux = nums[i]
                nums[i] = nums[j]
                nums[j] = aux
                j += 1
        return (len(nums)-ocurrences)


if __name__ == '__main__':
    print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
