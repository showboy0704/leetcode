class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        l = 0
        r = l+len(str(k))
        count = 0
        while l < len(s):
            while s[l:r] and int(s[l:r]) > k:
                r -= 1
            if l == r:
                return -1
            else:
                count += 1
                l = r
                r = l+len(str(k))
        return count
