# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        finish = n
        bad_point = 2**31 - 1

        while start < finish:
            check_point = (start + finish) // 2

            if isBadVersion(check_point) is True:
                finish = check_point
            else:
                start = check_point + 1

        return start 