class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # sorting enables two things: skipping duplicates and using two pointers

        for i, a in enumerate(nums):  # a is our "pivot" (first number of the triplet)
            if a > 0:
                break  # array is sorted, so if pivot > 0, every triplet from here sums > 0

            if i > 0 and a == nums[i - 1]:
                continue  # skip duplicate pivots so we don't produce repeat triplets

            # two-pointer search for pairs that sum to -a
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1  # sum too big -> move right pointer left to shrink it
                elif threeSum < 0:
                    l += 1  # sum too small -> move left pointer right to grow it
                else:
                    res.append([a, nums[l], nums[r]])
                    # move BOTH pointers: any other pair with this l or this r
                    # can't also sum to -a (we'd need the same partner again)
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1  # skip duplicate left values to avoid repeat triplets

        return res