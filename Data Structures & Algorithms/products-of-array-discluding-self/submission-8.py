class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = 1
        output = [1]*len(nums)
        for i in range(1, len(nums)):
            output[i] *= output[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix *= nums[i+1]
            output[i] *= suffix
        return output
