class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        trackNum = set()
        for num in nums:
            if num in trackNum:
                return True
            trackNum.add(num)
        return False
        