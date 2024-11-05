[LeetCode] Sort Array By Parity
====================================================
[문제보기](https://leetcode.com/problems/sort-array-by-parity/)

### 풀이 접근 방법:
1. ```nums``` 배열을 돌며 짝수 원소를 배열 ```answer```에 담음
2. ```nums``` 배열을 돌며 홀수 원소를 배열 ```answer```에 담음
3. ```answer``` 반환

### 내가 작성한 코드:
```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        answer = []
        for n in nums:
            if n % 2 == 0:
                answer.append(n)
                
        for n in nums:
            if n % 2 != 0:
                answer.append(n)
        return answer
        
```

### 반성할 점:
문제를 푸는거에만 집중하고 얼마나 효과적으로 문제를 해결하는지는 전혀 고려하지 않았다.    
리트코드의 코테 난이도를 체감해보려 쉬운 문제를 풀긴 했지만, 너무 쉽다고만 생각하고 바로 생각나는 방법만 적용해서 끝내버렸기에    
알고리즘의 효율성은 전~혀 고려되지 않았다.    
다른 풀이를 보면 정말 부끄러워진다.    
열심히 하자...

### 다른 풀이와 비교:
#### #1:
```python
i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] % 2 == 0:
            i += 1
        elif nums[j] % 2 != 0:
            j -= 1
        else:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1
    return nums
```
배열을 양쪽에서 접근해오면서    
1) 왼쪽 원소가 짝수일 땐, 왼쪽 인덱스를 1만큼 증가시키고      
2) 오른쪽 원소가 홀수일 땐, 오른쪽 인덱스를 1만큼 증가시킨다
3) 왼쪽과 오른쪽의 원소들이 각각 홀수와 짝수일때는, 각 원소의 값을 교환하고 각 인덱스 값을 1씩 증가시킨다.
4) 해당 과정을 왼쪽 인덱스가 오른쪽 인덱스의 값과 일치하거나 커질때까지 반복한다.
시간복잡도는 O(n), 공간은 O(1)이다.
