class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for detail in details:
            age = int(detail[-4])*10 + int(detail[-3])
            if age>60:
                counter+=1

        return counter