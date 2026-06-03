class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # this will allow us to use a 2 pointer approach from either end and keep checking till either pointer reaches 
        # the point in the array where the sign flips/gets to the value zero as anything past that will not make a sum of 0
        ans = [] # Array to hold answers
        frequencyNums = Counter(nums) # Needed to check if the third value needed for the 3 sum is available to use
        left, right = 0, len(nums) - 1 # initialize 2 pointers to each end
        while right > -1 and nums[right] >= 0: 
            left = 0 # reset left pointer back to start of the list for new positive num value
            while left < len(nums) and nums[left] <= 0:
                thirdNum = 0 - (nums[right] + nums[left]) # We see what we need our third number to be to make the sum
                if sorted([thirdNum, nums[right], nums[left]]) in ans:
                    left += 1
                    continue # don't bother going through this iteration if we've already seen this triplet and know it's valid
                
                flag = False # This will tell us if a sum is possible with these 3 nums
                
                # We check if the thirdNum is a repeat and if so, do we have enough distinct numbers in our nums array to make 
                # the addition work. We set the flag to tell us if the sum is possible or not
                if thirdNum != nums[right] and thirdNum != nums[left]:
                    flag = True if frequencyNums[thirdNum] > 0 else False
                elif thirdNum == nums[right] and thirdNum == nums[left]:
                    flag = True if frequencyNums[thirdNum] > 2 else False
                elif thirdNum == nums[right] or thirdNum == nums[left]:
                    flag = True if frequencyNums[thirdNum] > 1 else False

                if flag == False:
                    left += 1
                    continue

                # Once we know that all the nums needed to make the sum exist in the nums array, we'll make the list
                # entry, and append (we don't need to check if already in ans as we skipped any iterations that were in ans above)
                ans.append(sorted([thirdNum, nums[right], nums[left]]))

                left += 1 # move to next negative num
            right -= 1 # move to next positive num
            
        return ans




                