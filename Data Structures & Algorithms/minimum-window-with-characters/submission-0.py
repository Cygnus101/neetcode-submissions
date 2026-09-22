class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window = {}
        countt= {}

        for t_i in t:
            countt[t_i] = 1 + countt.get(t_i, 0)

        need = len(countt)
        have = 0
    
        res, reslen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countt and window[c] == countt[c]:
                have+=1
            
            while have == need:
                if reslen > r - l + 1:
                    res = [l, r]
                    reslen = r - l + 1


                window[s[l]] -=1        #pop

                if s[l] in countt and window[s[l]] < countt[s[l]]:
                    have-=1
                l+=1
        l,r = res      
        return s[l: r+1] if reslen != float("infinity") else  ""

                
