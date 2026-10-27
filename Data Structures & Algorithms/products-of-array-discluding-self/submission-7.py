class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        suffix = 1
        #prefix multiplication
        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]
        for j in range(len(nums)-2, -1,-1):
            suffix *= nums[j+1]
            output[j] *= suffix
        return output