class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()
        cards = []
        while deck:
            card = deck.pop()
            if not cards:
                cards.append(card)
            else:
                cards = [card, cards[-1]]+cards[:len(cards)-1]
        return cards


if __name__ == '__main__':
    deck = [17, 13, 11, 2, 3, 5, 7]
    print(f"{deck}")
    print('----------Answer Below----------')
    print(Solution().deckRevealedIncreasing(deck))
