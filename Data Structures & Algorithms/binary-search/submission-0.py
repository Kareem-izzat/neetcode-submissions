class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid=int(len(nums)/2)
        start=0
        end=len(nums)-1

        while start<=end:
            if nums[mid]==target:
                return mid
            elif  nums[mid]>target:
                end=mid-1

            else:
                start=mid+1
            mid=(start+end)//2
        return -1
        