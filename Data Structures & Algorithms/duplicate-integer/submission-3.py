class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for num in nums:
            if num not in table:
                table[num] = 1
            else:
                table[num] += 1
            if table[num] > 1:
                return True
        return False


        