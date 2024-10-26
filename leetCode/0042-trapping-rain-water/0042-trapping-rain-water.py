class Solution:
    def trap(self, height: List[int]) -> int:
        left = [height[0]] + [0] * (len(height) - 1)
        right = [0] * (len(height) - 1) + [height[-1]]
        water = 0
        
        for i in range(1, len(height)):
            left[i] = max(height[i], left[i - 1])
        
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(height[i], right[i + 1])
            
        for i in range(len(height)):
            water += min(left[i], right[i]) - height[i]
            
        return water
        