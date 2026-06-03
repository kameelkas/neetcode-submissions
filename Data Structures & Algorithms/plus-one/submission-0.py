class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        if digits[length - 1] != 9:
            digits[length - 1] += 1
            return digits
        
        carryOver = False
        for i in reversed(range(len(digits))):
            if (carryOver == True) and digits[i] == 9:
                digits[i] = 0
            elif (carryOver == False) and digits[i] == 9:
                digits[i] = 0
                carryOver = True
            elif (carryOver == True) and digits[i] != 9:
                digits[i] += 1
                carryOver = False
                break
        
        if carryOver == True:
            newNum = [0] * (length + 1)
            newNum[0] = 1
            return newNum
        else:
            return digits