class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sd = sorted(deck)
        usd = []
        
        while len(sd):
            c = sd.pop()
            if len(usd) < 2:
                usd = [c] + usd
            else:
                l = usd.pop()
                usd = [c, l] + usd
                
        return usd