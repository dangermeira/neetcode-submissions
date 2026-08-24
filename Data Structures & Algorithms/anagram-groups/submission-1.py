class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = []
        bucket = {}

        for i in range(0, len(strs)):
            ordered_list = sorted(strs[i])
            ordered_string = "".join(ordered_list)

            if ordered_string not in bucket:
                bucket[ordered_string] = [strs[i]]
            else:
                bucket[ordered_string].append(strs[i])

        return list(bucket.values())
                

            
                