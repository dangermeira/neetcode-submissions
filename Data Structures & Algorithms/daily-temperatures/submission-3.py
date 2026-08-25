class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # holds [index, temp]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                day = stack.pop()
                res[day[0]] = i - day[0]
            stack.append([i, t])
        return res