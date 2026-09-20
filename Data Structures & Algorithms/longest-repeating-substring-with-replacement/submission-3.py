class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        L = 0
        R= 0

        max_res = 0

        count_Dict = {}


        val = 0
            
        while R < len(s):

            if s[R] in count_Dict:
                count_Dict[s[R]] += 1
            else:
                count_Dict[s[R]] = 1

            val = max(count_Dict.values())

            while (R - L + 1) - val > k:
                count_Dict[s[L]] -= 1
                L += 1
                val = max(count_Dict.values())

            max_res = max(max_res, R - L + 1)

            R += 1
        
        return max_res