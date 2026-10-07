class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""
        prefix_length = 0


        for i in range(len(strs[0])):
            first_char = strs[0][i]

            for j in range(1, len(strs)):

                if len(strs[j]) <= i:
                    return prefix

                if first_char != strs[j][i]:
                    return prefix
            
            prefix += first_char

        
        return prefix



            