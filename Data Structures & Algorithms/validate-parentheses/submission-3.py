class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for elem in s:
            if elem in pairs:
                if not stack or stack[-1] != pairs[elem]:
                    return False
                stack.pop()
            else:
                stack.append(elem)

        return not stack
                




        


        
