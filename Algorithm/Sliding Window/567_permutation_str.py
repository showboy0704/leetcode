from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        table, win, matched = Counter(s1), len(s1), 0

        for i in range(len(s2)):
            if s2[i] in table:
                table[s2[i]] -= 1
                if table[s2[i]] == 0:
                    matched += 1
            if i >= win and s2[i-win] in table:
                if table[s2[i-win]] == 0:
                    matched -= 1
                table[s2[i-win]] += 1

            if matched == len(table):
                return True

        return False


if __name__ == '__main__':
    s1, s2 = "ab", "eidbaooo"
    print(f"{s1, s2}")
    print('----------Answer Below----------')
    print(Solution().checkInclusion(s1, s2))
