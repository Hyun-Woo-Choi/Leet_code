class Solution:
    def countAndSay(self, n: int) -> str:

        # if n is 1, default 1
        current_str = "1"

        for _ in range(1, n):
            next_str = ""
            initial_num = current_str[0]
            count = 0

            for num in current_str:
                if num == initial_num:
                    count += 1
                else:
                    next_str += str(count) + initial_num
                    initial_num = num
                    count = 1
            next_str += str(count) + initial_num

            current_str = next_str
        return current_str
