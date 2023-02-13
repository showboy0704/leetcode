class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ''
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            word += (word1[i]+word2[j])
            i+=1
            j+=1
        if i == len(word1):
            word += word2[j:]
        elif j == len(word2):
            word += word1[i:]
        return word


if __name__ == '__main__':
    word1, word2 = "abc", "pqr"
    print(f"{word1 , word2}")
    print('----------Answer Below----------')
    print(Solution().mergeAlternately(word1, word2))
