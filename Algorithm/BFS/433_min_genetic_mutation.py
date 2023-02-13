from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        valids = {valid for valid in bank}
        mutated = set()
        n = len(startGene)
        queue = deque([(startGene, 0)])
        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps
            for i in range(n):
                for c in ['A', 'C', 'G', 'T']:
                    mutation = gene[:i]+c+gene[i+1:]
                    if mutation in valids and mutation not in mutated:
                        mutated.add(mutation)
                        queue.append((mutation, steps+1))
        return -1


if __name__ == '__main__':
    startGene, endGene, bank = "AACCGGTT", "AAACGGTA", [
        "AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"]
    print(f"{startGene , endGene , bank}")
    print('----------Answer Below----------')
    print(Solution().minMutation(startGene, endGene, bank))
