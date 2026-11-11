class Solution:
    def minOperations(self, s: str) -> int:
        s_list = list(s)
        sorted_s = sorted(s_list)
        
        # 1. 이미 정렬된 상태
        if s_list == sorted_s:
            return 0
            
        n = len(s)
        # 2. 불가능한 경우 (길이가 2인데 정렬되지 않은 상태)
        if n == 2:
            return -1
            
        min_char = sorted_s[0]
        max_char = sorted_s[-1]
        
        # 3. 1번만에 정렬이 가능한 경우
        # 가장 작은 값이 이미 맨 앞에 있거나, 가장 큰 값이 이미 맨 뒤에 있는 경우
        if s_list[0] == min_char or s_list[-1] == max_char:
            return 1
            
        # 4. 3번이 필요한 최악의 경우
        # '유일한' 최댓값이 맨 앞에 있고, '유일한' 최솟값이 맨 뒤에 있는 경우
        if (s_list[0] == max_char and s_list.count(max_char) == 1 and 
            s_list[-1] == min_char and s_list.count(min_char) == 1):
            return 3
            
        # 5. 그 외의 모든 경우는 2번 연산으로 해결 가능
        return 2