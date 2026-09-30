class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = ""
        lw_length = 0
        for i in s:
            if i != " ":
                last_word += i
                lw_length = len(last_word)
            else:
                last_word = ""

        return lw_length