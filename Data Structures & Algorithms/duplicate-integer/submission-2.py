class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        trackNum = {}
        for num in nums:
            if trackNum.get(num) is None:
                trackNum[num] = 1
            else:
                return True
        return False
        