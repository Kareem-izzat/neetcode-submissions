class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        end=len(digits)-1
        carry=0
        if digits[end]!=9:
            digits[end]+=1
        else:
            digits[end]=0
            carry=1

        while carry and end>=1:
            end-=1
            if digits[end] != 9:
                digits[end] += 1
                carry=0
            else:
                digits[end] = 0
                carry = 1
        if carry and end==0:
            digits.insert(0,1)
        return digits
                