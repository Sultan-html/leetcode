from typing import List

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(st: str) -> List[str]:
            stack: List[str] = []
            for char in st:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack
        
        return process_string(s) == process_string(t)

sol = Solution()
print(sol.backspaceCompare("ab#c", "ad#c")) 
print(sol.backspaceCompare("ab##", "c#d#"))
print(sol.backspaceCompare("a#c", "b"))     