class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        answer = []

        for i in range(numRows):
            temp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(answer[i - 1][j - 1]+answer[i - 1][j])
            
            answer.append(temp)
        
        return answer

        # a11 = 1
        # a21 = a11 a22 = a11
        # a31 = a21 a32 = a21+ a22 , a33 = a22
        # a41 = a31 a42 = a31 + a32 , a43 = a32 + a33, a44 = a33


        