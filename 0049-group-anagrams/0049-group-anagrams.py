from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 기본값이 list인 딕셔너리 생성
        anagrams = defaultdict(list)
        
        for s in strs:
            # 1. 문자열을 정렬한 뒤 다시 하나의 string으로 합침
            sorted_str = "".join(sorted(s))
            
            # 2. 정렬된 문자열을 키로 하여 원본 문자열 append
            anagrams[sorted_str].append(s)
            
        # 3. 딕셔너리의 value들만 2차원 리스트로 반환
        return list(anagrams.values())