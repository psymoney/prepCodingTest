class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        usd = []
        
        while len(deck):
            c = deck.pop()
            if len(usd) < 2:
                usd = [c] + usd
            else:
                l = usd.pop()
                usd = [c, l] + usd
                
        return usd