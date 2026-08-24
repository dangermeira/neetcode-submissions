from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            label = "".join(sorted(word))
            groups[label].append(word)

        return list(groups.values())


                

            
                