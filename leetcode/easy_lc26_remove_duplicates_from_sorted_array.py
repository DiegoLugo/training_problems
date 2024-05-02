class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        index = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
        print(nums)
        return index


if __name__ == '__main__':
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
