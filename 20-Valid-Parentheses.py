

class Solution:
    def isValid(self, s: str) -> bool:  

        # Create our stack datastructure 
        stack = []

        # Loop through each character in the string 
        for c in s:  

            # If the string is a starting element, add to our stack 
            if c in ["{", "(", "["]: 
                stack.append(c)
            
            # Else if the character is a right element and the left element is one before it, remove from stack as valid 
            elif c == ')' and stack[-1] == '(' and len(stack) != 0: 
                stack.pop()

            elif c == ']' and stack[-1] == ']' and len(stack) != 0: 
                stack.pop()

            elif c == '}' and stack[-1] == '{' and len(stack) != 0: 
                stack.pop()
        
            # Else, the character is invalid and return false
            else: 
                return False


        # Lastly, make sure the stack is empty
        return stack == []

solution = Solution()

# Test cases: 
s = "()" 
print(f"Result: {solution.isValid(s)}")

