class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(index,arr):
            if len(arr)==len(nums):
                ans.append(arr)
                return

            for i in range(0,len(nums)):
                if i != index and nums[i] not in arr:
                    cpy=arr.copy()
                    cpy.append(nums[i])
                    backtrack(i, cpy)
        for i in range(0,len(nums)):
            backtrack(i,[nums[i]])
        return ans
        