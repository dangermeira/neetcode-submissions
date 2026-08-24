class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        clean = list(unique)

        if len(clean) < 2:
            return len(clean)

        max_streak = 1
        streak = 1

        for i in range(1, len(clean)):
            if clean[i] == clean[i - 1] + 1:
                streak += 1
            else:
                streak = 1
            if streak > max_streak:
                max_streak = streak
        return max_streak

