class Solution:
    def isValid(self, s: str) -> bool:
        # map - holds the key, value pairs for open and closed paranthesis'
        # stack - holds the parenthesis' as we loop through 's' and will help determine if valid
        map = { ')' : '(', '}' : '{', ']' : '['}
        stack = []

        for elem in s:
            if elem in map:
                if not stack or stack[-1] != map.get(elem):
                    return False
                elif stack[-1] == map.get(elem):
                    stack.pop()
            else:
                stack.append(elem)

        return not stack

                




        


        
