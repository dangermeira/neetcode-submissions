class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDupe = set()

        for num in nums:
            if num in noDupe:
                return True
            noDupe.add(num)

        return False
        