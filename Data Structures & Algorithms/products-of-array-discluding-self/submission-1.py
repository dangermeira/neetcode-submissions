class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range (len(nums)):
            sum = 1
            for j in range(len(nums)):
                if j != i:
                    sum *= nums[j]
            output.append(sum)

        return output