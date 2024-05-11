from queue import PriorityQueue


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        class Fraction:
            def __init__(self, x, y):
                self.numerator = y
                self.denominator = x
                self.value = arr[y] / arr[x]
                
            def __gt__(self, other):
                return self.value > other.value
            
            def __lt__(self, other):
                return self.value < other.value
            
            def __eq__(self, other):
                return self.value == other.value
            
        pq = PriorityQueue()
        for x in range(len(arr)):
            pq.put(Fraction(x, 0))
            
        ans = None
        
        while k > 0:
            ans = pq.get()
            if ans.numerator + 1 < len(arr):
                pq.put(Fraction(ans.denominator, ans.numerator + 1))
            k -= 1
            
        return [arr[ans.numerator], arr[ans.denominator]]
        
        
        