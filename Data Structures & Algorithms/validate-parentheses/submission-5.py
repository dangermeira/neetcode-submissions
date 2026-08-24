class Solution:
    def isValid(self, s: str) -> bool:
        pairs = { ')' : '(', '}' : '{', ']' : '[' }
        stack = []

        for elem in s:
            if elem in pairs:
                if not stack or pairs.get(elem) != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(elem)
                
        return not stack

                




        


        
