class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        placements = {}
        for idx, athlete in enumerate(sorted(score, reverse=True)):
            if idx == 0:
                placements[str(athlete)] = 'Gold Medal'
            elif idx == 1:
                placements[str(athlete)] = 'Silver Medal'
            elif idx == 2:
                placements[str(athlete)] = 'Bronze Medal'
            else:
                placements[str(athlete)] = str(idx + 1)
                
        results = []
        for e in score:
            results.append(placements[str(e)])
        return results
            
        