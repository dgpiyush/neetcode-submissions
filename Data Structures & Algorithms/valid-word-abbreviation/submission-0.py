class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        s = 0 
        j =  0

        c = ''

        ans = True

        while(len(word)-1 >= j ):

            if(abbr[s].isnumeric()):
                c = c + abbr[s]
                s+=1
            
                continue
            else:
                if(c):
                    j += int(c)
                    c= ''
                


            if(abbr[s] != word[j]):
                ans = False
                return ans

            j += 1
            s += 1
        
        return ans
            
        