class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, currentNum = 0, nums[0] # currentNum is the current number we are on in the array, count is the count of the currentNum we are on
        for num in nums:
            if num == currentNum:
                count += 1
            else:
                if count == 0:
                    currentNum = num
                    count += 1
                else:
                    count -= 1
        return currentNum