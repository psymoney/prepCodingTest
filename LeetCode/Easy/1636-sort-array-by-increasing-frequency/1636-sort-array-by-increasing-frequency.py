from collections import defaultdict

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency: dict = defaultdict(int)
        
        for e in nums:
            frequency[str(e)] += 1
            
        return sorted(nums, key=lambda x: (frequency[str(x)], -x))