class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seq_table = dict()
        seqs = []
        left, right = 0, 9
        while right <= len(s):
            seq = s[left:right+1]
            if seq_table.get(seq):
                if seq_table[seq] == 1:
                    seqs.append(seq)
                seq_table[seq] += 1
            else:
                seq_table[seq] = 1
            left += 1
            right += 1
        return seqs


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(f"{s}")
    print(Solution().findRepeatedDnaSequences(s))
