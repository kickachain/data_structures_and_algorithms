# fastest on leetcode
class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        bra={"(":")","[":"]","{":"}"}
        for i in s:
            if i in bra.keys():
                st.append(i)
            elif i in bra.values():
                if not st or bra[ st.pop()] !=i:
                    return False
        return not st


# brute force
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
# Time complexity: O(n2)
# Space complexity: O(n)


# stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
# Time complexity: O(n)
# Space complexity: O(n)


# my solution
class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ["(", "[", "{"]
        closed_brackets = [")", "]", "}"]
        stack = []
        # loop through each bracket in input
        for bracket in s:
            # if its an open bracket
            if bracket in open_brackets:
                # add to top of stack
                stack.append(bracket)
            elif bracket in closed_brackets:
                # If the stack is empty, it's not valid
                if not stack:
                    return False

                last_open_bracket = stack.pop()

                if open_brackets.index(last_open_bracket) != closed_brackets.index(bracket):
                    return False
        return len(stack) == 0