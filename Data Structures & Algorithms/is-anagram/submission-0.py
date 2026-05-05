class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #make sure length of both inputs is same.
            return False    #if not sorting's not required.

        return sorted(s) == sorted(t) 