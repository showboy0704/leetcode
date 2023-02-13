class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_table =dict()
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagrams_table:
                anagrams_table[sorted_s].append(s)
            else:
                anagrams_table[sorted_s]=[s]
            
        return list(anagrams_table.values())
        


if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(f"{strs}")
    print('----------Answer Below----------')
    print(Solution().groupAnagrams(strs))
