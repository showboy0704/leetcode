class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            sub_prefix=''
            for j in range(min(len(prefix), len(s))):
                if prefix[j] == s[j]:
                    sub_prefix = prefix[:j+1]
                else:
                    break
            prefix =sub_prefix   

        return prefix


if __name__ == '__main__':
    strs = ["cir","car"]
    print(f"{strs}")
    print('----------Answer Below----------')
    print(Solution().longestCommonPrefix(strs))
