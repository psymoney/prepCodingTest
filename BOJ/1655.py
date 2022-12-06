from heapq import heappush, heappop
import sys


class MedianSelector:
    max_h = []
    min_h = []

    def insert(self, v):
        if len(self.max_h) == len(self.min_h):
            heappush(self.max_h, -v)
        else:
            heappush(self.min_h, v)
            
        if self.min_h and -self.max_h[0] > self.min_h[0]:
            self.swap()

    def swap(self):
        max_top = heappop(self.max_h)
        min_top = heappop(self.min_h)
        heappush(self.max_h, -min_top)
        heappush(self.min_h, -max_top)

    def get_median(self):
        return -self.max_h[0]
        
    
    
N = int(sys.stdin.readline())
median_selector = MedianSelector()

for _ in range(N):
    i = int(sys.stdin.readline())
    median_selector.insert(i)
    print(median_selector.get_median())
