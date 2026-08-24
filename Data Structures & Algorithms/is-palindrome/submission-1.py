class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for char in s:
            if char.isalnum():
                newStr += char.lower()

        for i in range(0, round(len(newStr) / 2)):
            if newStr[i] != newStr[len(newStr) - i - 1]:
                return False
        return True
            

        