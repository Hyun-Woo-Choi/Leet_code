class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        answer = 0
        
        for right, char in enumerate(s):
            # 이전에 본 문자이고, 그 위치가 현재 윈도우 범위(left 이상) 내에 있다면
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            
            # 현재 문자의 최신 위치 기록
            seen[char] = right
            
            # 현재 윈도우의 길이로 최대값 갱신
            answer = max(answer, right - left + 1)
            
        return answer

        