class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_one = {}
        map_two = {}

        for ch in s:
            map_one[ch] = map_one.get(ch, 0) + 1

        for ch in t:
            map_two[ch] = map_two.get(ch, 0) + 1

        for key in map_one:
            if len(map_one) != len(map_two):
                return False
            if map_one.get(key, 0) != map_two.get(key, 0):
                return False

        return True

        