class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)


if __name__ == '__main__':
    s, t = "anagram", "nagaram"
    print(f"{s , t}")
    print('----------Answer Below----------')
    print(Solution().isAnagram(s, t))
