from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = list(Counter(nums).most_common())
        output = []

        for i in range(0, k):
            output.append(num_count[i][0])

        return output

        

