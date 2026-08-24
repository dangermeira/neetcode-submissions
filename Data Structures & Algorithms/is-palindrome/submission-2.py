class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join([char for char in s if char.isalnum()]).lower()

        for i in range(len(clean) // 2):
            if clean[i] != clean[len(clean) - i - 1]:
                return False
        return True
            

        