class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        majority = int(len(nums)/2)
        for i in range(0, len(nums)):
            if nums[i] not in counter:
                counter[nums[i]] = 0
            counter[nums[i]] += 1
            if counter[nums[i]] > majority:
              return nums[i]
        
if __name__ == '__main__':
    print(Solution().majorityElement([3,2,3]))