class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        keepTrack = defaultdict(int) # keeps track of occurences of each num in nums
        for num in nums:
            keepTrack[num] += 1
        
        return max(keepTrack, key=keepTrack.get)