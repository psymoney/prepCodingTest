[LeetCode] Shorted Unsorted Continuous Subarray
====================================================
[문제보기](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)
### 문제
정수 배열 ```nums```가 주어졌을때, 하위 배열의 오름차순 정렬이 전체 배열을 오름차순으로 정렬하게끔 하는 연속적인 하위 배열을 찾아서 해당 배열의 길이를 반환하라.

### 제약조건
1. ```1 <= nums.length <= 10^4```
2. ```-10^5 <= nums[i] <= 10^5```

### 풀이 접근 방법: 
연속적인 하위 배열의 정렬만으로 전체 배열의 정렬이 가능하므로, 하위 배열의 첫번째 원소 값과 마지막 원소 값은 정렬된 전체 원소의 값과 다를 것이라는게 처음 생각한 가설이었다.    
따라서, 정렬된 배열과 원본 배열의 시작, 끝 인덱스를 비교하며 각각의 값이 일치하지 않는 인덱스간의 차이가 하위 배열의 길이가 될 것이라 생각했다.     
이하 해당 알고리즘 주요 내역
1. ```nums``` 배열을 오름차순 정렬한 ```sorted_nums```를 생성, 이하 알고리즘 주요 조건 분기
2. (1) ```len(nums) == 1```이면, 0 반환
3. (2) ```sorted_nums == nums```이면, 0 반환
4. (3) 반복문 중 ```sorted_nums[i] != nums[i]```일때, ```a = i```이며, 그렇지 않다면 ```i += 1```이다. 다른 값을 찾으면 인덱스에 대한 조작을 하지 않음으로써 반복문 수행 조건에 영향을 주지 않는다
5. (4) 반복문 중 ```sorted_nums[j] != nums[j]```일때, ```b = j```이며, 그렇지 않다면 ```j -= 1```이다.
6. ```a```와 ```b```가 모두 ```None```이 아닌 경우, 조건문을 빠져나온다
7. 

### 내가 작성한 코드:
```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = nums.copy()
        sorted_nums.sort()
        i = 0
        j = len(nums) - 1
        a = None
        b = None
        
        if len(nums) == 1:
            return 0
        
        if sorted_nums == nums:
            return 0
        
        while i < j:
            if sorted_nums[i] != nums[i]:
                a = i
            else:
                i += 1
            if sorted_nums[j] != nums[j]:
                b = j
            else:
                j -= 1
            if a is not None and b is not None:
                break
                
        return b-a+1
        
```

### 개선할 점:
첫 번째 주요 분기인 ```if len(nums) == 1```은 의미가 없는 분기이다.    
배열의 길이가 1이라면, 정렬된 배열과 원배열은 동일하므로 두 번째 주요 분기에서 처리가 가능하기 때문이다.
따라서 해당 코드는 삭제 가능

### 다른 풀이와 비교:
