class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsAsSet = set(nums)
        if len(numsAsSet) != len(nums):
            return True
        return False
        