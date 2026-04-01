class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        curr=nums[0]
        maxi=nums[0]
        for i in range(1,len(nums)):
            if curr < nums[i] and curr<0:
                curr = nums[i]
            else:
                curr+=nums[i]
            if curr>maxi:
                maxi=curr
        return maxi