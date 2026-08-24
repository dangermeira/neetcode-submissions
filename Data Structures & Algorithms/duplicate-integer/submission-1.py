class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for x in nums:
            if x in my_set:
                return True
            my_set.add(x)
        return False