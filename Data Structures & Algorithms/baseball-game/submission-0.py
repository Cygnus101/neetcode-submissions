class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sumo = 0
        scores = []
        for i in range(len(operations)):
            if operations[i] == "+":
                a = int(scores[-1]) + int(scores[-2])
                sumo+=a
                scores.append(a)
            elif operations[i] == "D":
                a=int(scores[-1])*2
                sumo+=a
                scores.append(a)
            elif operations[i] == "C":
                sumo-=int(scores[-1])
                scores.pop()
            else:
                scores.append(operations[i])
                sumo+=int(scores[-1])


        return sumo