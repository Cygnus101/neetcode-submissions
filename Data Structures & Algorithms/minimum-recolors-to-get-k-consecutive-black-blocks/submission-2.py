class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_t = float("inf")

        L = 0
        for R in range(k, len(blocks) + 1):
            min_c = 0
            for i in range(L, R):
                if blocks[i] == "W":
                    min_c +=1
            if min_c < min_t:
                min_t = min_c
            L+=1

        return min_t