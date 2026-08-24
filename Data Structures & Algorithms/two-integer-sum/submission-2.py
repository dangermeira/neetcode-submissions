class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index, value in enumerate(nums):
            difference = target - value

            if difference in map:
                return [min(map.get(difference), index), max(map.get(difference), index)]
            else:
                map[value] = index
