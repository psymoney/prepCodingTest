class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = 0
        local_sum = 0
        prev = 0

        for v in nums:
            if v > prev:
                local_sum += v
            else:
                answer = max(answer, local_sum)
                local_sum = v
            
            prev = v
        answer = max(answer, local_sum)

        return answer
        