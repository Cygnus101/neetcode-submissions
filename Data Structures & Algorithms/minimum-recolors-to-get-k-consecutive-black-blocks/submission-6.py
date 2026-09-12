class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = []
        L = 0
        R = k

        min_counter = 0
        
        
        for i in range(R):
            if blocks[i] == "W":
                min_counter+=1
            window.append(blocks[i])

        new_counter = min_counter
        
        while R < len(blocks):
            
            window.append(blocks[R])
            if blocks[R] == "W":
                new_counter+=1
            if blocks[L] == "W":
                new_counter-=1
            if new_counter < min_counter:
                min_counter = new_counter
            

            window.pop(0)
            L+=1
            R+=1

        return min_counter


