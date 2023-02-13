class Solution:
    palin_table = dict()
    longest_palin = None

    def _is_palin(self, s: str) -> bool:
        if s[0] == s[-1]:
            if len(s) % 2 == 1:
                if len(s) == 3:
                    self.palin_table[s] = True
                    return True
                else:
                    if self.palin_table.get(s[1:len(s)-1]):
                        self.palin_table[s] = True
                        return True
            else:
                if len(s) == 2:
                    self.palin_table[s] = True
                    return True
                else:
                    if self.palin_table.get(s[1:len(s)-1]):
                        self.palin_table[s] = True
                        return True
        else:
            return False

    def _find_palin(self, first, start, s):
        for n in range(start, len(s)+1, 2):
            left, right = 0, n
            new_palin = 0
            while right < len(s)+1:
                sub_string = s[left:right]
                if self._is_palin(sub_string):
                    if len(sub_string) > len(self.longest_palin):
                        self.longest_palin = sub_string
                        if first and (len(self.longest_palin) == len(s)):
                            return 'limit ok'
                    new_palin += 1
                left += 1
                right += 1
            if new_palin == 0:
                break
        return 'ok'

    def longestPalindrome(self, s: str) -> str:
        self.longest_palin = s[0]
        if len(s) == 1:
            return self.longest_palin
        start_1st, start_2nd = 2, 3
        if len(s) % 2 == 1:
            start_1st, start_2nd = 3, 2
        if self._find_palin(True, start_1st, s) == 'limit ok':
            return self.longest_palin
        self._find_palin(False, start_2nd, s)
        return self.longest_palin


if __name__ == '__main__':
    s = "aacabdkacaa"
    print(f"{s}")
    print('-------------------------------------------------')
    print(Solution().longestPalindrome(s))
