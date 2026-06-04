class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = maxCount = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            maxCount = max(count, maxCount)
            
        return maxCount
