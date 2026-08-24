class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = {}
        list_freq = []

        for num in nums:
            if num not in bucket:
                bucket[num] = [num]
            else:
                bucket[num].append(num)

        for i in range(0, k):
            most_vals = 0
            temp_key = 0
            for key in bucket:
                if len(bucket[key]) > most_vals and key not in list_freq:
                    most_vals = len(bucket[key])
                    temp_key = key
            list_freq.append(temp_key)

        return list_freq

