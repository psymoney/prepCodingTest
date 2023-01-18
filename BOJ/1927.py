import sys
input = sys.stdin.readline

heap = [None]

n = int(input())

def insert_heap(v):
    heap.append(v)
    cur = len(heap) - 1
    next = cur // 2
    while next > 0:
        if heap[next] > heap[cur]:
            heap[next], heap[cur] = heap[cur], heap[next]
            cur = next
            next = next // 2
        else:
            break
          
def print_and_pop():
    if len(heap) == 1:
        print(0)
        return
    print(heap[1])
    heap[1], heap[len(heap) - 1] = heap[len(heap) - 1], heap[1]
    heap.pop(len(heap) - 1)
    parent = 1
    child = 2
    while child <= len(heap) - 1:
        if child < len(heap) - 1 and heap[child] > heap[child + 1]:
            child += 1
        if heap[parent] < heap[child]:
            break
  
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child *= 2
        

for _ in range(n):
    x = int(input())
    if x == 0:
        print_and_pop()
    else:
        insert_heap(x)
