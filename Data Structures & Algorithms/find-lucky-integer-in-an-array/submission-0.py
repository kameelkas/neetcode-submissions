class Solution:
    def findLucky(self, arr: List[int]) -> int:
        tracker = 0 # tracks the largest number that matches criteria. We can initialize to 0 since 0 can't appear 0 times in the array and be the candidate
        freq_table = Counter(arr) # hash map of values to freq of arr
        for k, v in freq_table.items():
            if k == v and k > tracker:
                tracker = k
        
        if tracker == 0:
            return -1
        else:
            return tracker