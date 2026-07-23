class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        keepTrack = defaultdict(int) # initialize and fill dict with freq counts
        for num in nums:
            keepTrack[num] += 1

        nums.sort(reverse=True) # if freq are equal, sort in descending order. Sort in descending order first so that when we sort based on freq, the sort() will keep this relative order for numbers with same frequency counts
        nums.sort(key=lambda x: keepTrack[x]) # sort based on frequency counts
        return nums
