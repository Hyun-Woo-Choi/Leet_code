class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = [abs(a -b) for a, b in zip(nums1, nums2)]
        total_k = k1 + k2

        if sum(diffs) <= total_k:
            return 0
        
        low, high = 0, max(diffs)
        target = high

        while low <= high:
            mid = (low + high) // 2
            
            needed = sum(d - mid for d in diffs if d > mid)
            
            if needed <= total_k:
                target = mid
                high = mid -1
            else:
                low = mid + 1

        rem_k = total_k

        for i in range(len(diffs)):
            if diffs[i] > target:
                rem_k -= (diffs[i] - target)
                diffs[i] = target
        
        for i in range(len(diffs)):
            if rem_k == 0:
                break
            if diffs[i] == target and diffs[i] > 0:
                diffs[i] -= 1
                rem_k -= 1
        
        return sum(d * d for d in diffs)
        
