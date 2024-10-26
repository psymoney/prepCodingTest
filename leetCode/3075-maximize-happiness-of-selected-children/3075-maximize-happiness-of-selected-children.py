class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        result = 0
        for i in range(k):
            value = happiness[i] - i
            result += value if value > 0 else 0
        return result