class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        position = 0
        move = 0

        while position < n - 1:
            distance = nums[position]

            # 여기서 바로 끝까지 갈 수 있으면 한 번이면 끝
            if position + distance >= n - 1:
                return move + 1

            best_reach = -1
            nxt = position
            for i in range(position + 1, position + distance + 1):
                if i + nums[i] > best_reach:
                    best_reach = i + nums[i]
                    nxt = i

            position = nxt
            move += 1

        return move