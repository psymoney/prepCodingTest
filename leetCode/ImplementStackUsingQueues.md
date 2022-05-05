[LeetCode] ImplementStackUsingQueues
====================================================
[문제보기](https://leetcode.com/problems/implement-stack-using-queues/solution/)

### 풀이 접근 방법:
1. ```list``` 하나를 ```Queue``` 객체 하나로 사용
2. ```push()``` 메서드는 ```List.append()```메서드 활용
3. ```pop()``` 메서드는 리스트를 순환하며 배열의 첫 번째 원소를 ```List.append()``` 메서드로 가장 마지막 위치에 삽입한 뒤, 해당 위치의 원소를 제거하는 연산을 반복한다. 해당 과정에서 최초 배열의 가장 마지막 위치에 해당하는 원소를 만나면 해당 원소를 배열에서 삭제하고 해당 원소를 반환한다
4. ```top()``` 메서드는 배열의 가장 마지막 원소를 반환
5. ```empty()``` 메서드는 ```len(List)```가 0이면 ```True```값을, 그렇지 않다면 ```False```값을 반환

### 내가 작성한 코드:
```python
from queue import Queue

class MyStack:

    def __init__(self):
        self.q_a = []

    def push(self, x: int) -> None:
        self.q_a.append(x)
        return None

    def pop(self) -> int:
        i = 0
        while i < len(self.q_a):
            if i == len(self.q_a) - 1:
                a = self.q_a[0]
                self.q_a.pop(0)
                return a
            i += 1
            self.q_a.append(self.q_a[0])
            self.q_a.pop(0)

    def top(self) -> int:
        return self.q_a[len(self.q_a)-1]

    def empty(self) -> bool:
        if len(self.q_a) == 0:
            return True
        else:
            return False
        
```
