class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = maxCount = 0
        for num in nums:
            count = count + 1 if num == 1 else 0
            if maxCount < count:
                maxCount = count
        return maxCount

