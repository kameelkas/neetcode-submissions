class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = [] # Array to hold answers
        frequencyNums = Counter(nums) # Needed to check if the third value needed for the 3 sum is available to use
        # Double for loop to track 2/3 numbers. Should satisfy O(N^2)
        for i in range(len(nums)):
            for j in range(len(nums)):
                flag = False # This will tell us if a sum is possible with these 2 nums
                if i == j: # Skip since we can't use same index
                    continue
                
                thirdNum = 0 - (nums[i] + nums[j]) # We see what we need our third number to be to make the sum
                # We check if the thirdNum is a repeat and if so, do we have enough distinct numbers in our nums array to make 
                # the addition work. We set the flag to tell us if the sum is possible or not
                if thirdNum == nums[i] == nums[j]:
                    flag = True if frequencyNums[thirdNum] > 2 else False
                elif thirdNum == nums[i]:
                    flag = True if frequencyNums[thirdNum] > 1 else False
                elif thirdNum == nums[j]:
                    flag = True if frequencyNums[thirdNum] > 1 else False
                else:
                    flag = True if frequencyNums[thirdNum] > 0 else False

                if flag == False:
                    continue

                # Once we know that all the nums needed to make the sum exist in the nums array, we'll make the list
                # entry, sort it, and append to our ans array if it doesn't already exist there
                listToAppend = sorted([thirdNum, nums[i], nums[j]])
                if listToAppend not in ans:
                    ans.append(listToAppend)
            
        return ans




                