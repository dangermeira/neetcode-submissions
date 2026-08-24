class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            excluded = nums[:i] + nums[i + 1:]
            output.append(math.prod(excluded))

        return output