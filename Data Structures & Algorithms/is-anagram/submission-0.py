class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_set = set()
        for i in s:
            s_set.add(i)
        
        for i in t:
            if i not in s_set:
                return False


        return True


            
        