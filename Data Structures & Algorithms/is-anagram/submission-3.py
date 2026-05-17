class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        # this solution is o(nlogn) space is o(1)
        s_sort = "".join(sorted(s))
        t_sort = "".join(sorted(t))
        return s_sort == t_sort

    

        return total_char_ascii_count_in_s == total_char_ascii_count_in_t


    


            
        