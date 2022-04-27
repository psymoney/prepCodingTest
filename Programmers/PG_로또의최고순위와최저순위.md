[Programmers] Coding Test Practice: 로또의 최고 순위와 최저 순위
====================================================
[문제보기](https://programmers.co.kr/learn/courses/30/lessons/77484#fn1)

### 풀이 접근 방법:
1. lottos의 원소 중 값이 0이 아닌 원소의 값이 win_nums 원소의 값과 동일할때, 동일한 숫자의 갯수를 num_mathing이라 하면 num_matching은 맞출 수 있는 추천 숫자의 최솟값이다.
2. lottos의 원소 중 값이 0인 원소의 갯수를 num_zero라 할때, 맞출 수 있는 추천 숫자의 최댓값은 num_matching + num_zero이다.
3. num_matching + num_zero, num_matching 각각의 값에 부합하는 등수를 answer 배열에 담고 반환한다.

### 내가 작성한 코드:
```python
def solution(lottos, win_nums):
    answer = []
    num_matching = 0
    num_zero = 0
    
    for wn in win_nums:
        if wn in lottos:
            num_matching += 1
    for n in lottos:
        if n == 0:
            num_zero += 1
            
    for n in [num_matching + num_zero, num_matching]:
        if n == 6:
            answer.append(1)
        elif n == 5:
            answer.append(2)
        elif n == 4:
            answer.append(3)
        elif n == 3:
            answer.append(4)
        elif n == 2:
            answer.append(5)
        else:
            answer.append(6)
    
    return answer
```

### 겪었던 어려움:
앞서 풀었던 문제들 대비 너무 쉬워서 바로 나오는 풀이가 맞는건지, 내가 간과하고 있는게 없는지 신경쓰였다.   
문제가 쉬웠던 만큼 굳이 다른 풀이를 가져와서 비교하진 않겠지만, 확인했던 답안 중 참고할만한 내용은 다음과 같다.
```python 
# lottos 배열에서 0 값의 갯수 찾기: for loop 대체 함수. 
# 하지만 해당 함수의 시간 복잡도는 O(n)으로 for loop과 동일 -> 가독성 측면
num_zero = lottos.count(0)
```
```
# 등수 반환 배열 활용하기: 맞춘 갯수를 인덱스로 하는 순위 배열로 바로 찾기 
rank = [6,6,5,4,3,2,1]
answer = [rank[num_zero + num_matching], rank[num_matching]]
```
