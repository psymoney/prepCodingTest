[Programmers] Coding Test Practice: 모의고사
============================================
[문제보기](https://programmers.co.kr/learn/courses/30/lessons/42840)

#### 풀이 접근 방법:
1. 각각의 수포자가 찍는 방식은 반복되는 패턴이 존재한다. (예: 1번은 1,2,3,4,5,...)
2. 각 패턴을 circular linked list와 같이 순환하는 구조로 구현 -> itertools 라이브러리의 cycle 함수 이용
3. 반복문으로 주어진 답안 목록의 원소를 각각의 패턴과 비교하며 점수 산출
4. 산출된 점수 배열을 해당 배열의 최댓값과 비교하며 최댓값과 동일한 인덱스에 정수 1을 더하여 최종 반환 배열에 담는다.

#### 내가 작성한 코드:
```
from typing import Sequence
from itertools import cycle


def solution(answers: Sequence) -> Sequence:
    pool1 = cycle([1, 2, 3, 4, 5])
    pool2 = cycle([2, 1, 2, 3, 2, 4, 2, 5])
    pool3 = cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    
    scores = [0, 0, 0]
    
    for answer in answers:
        if answer == next(pool1):
            scores[0] += 1
        if answer == next(pool2):
            scores[1] += 1
        if answer == next(pool3):
            scores[2] += 1
            
    maxScore = max(scores)
    answer = []
    
    for i, score in enumerate(scores):
        if score == maxScore:
            answer.append(i+1)
            
    return answer
```

#### 겪었던 어려움:
1. 2번째 풀이 접근방법 중 순환하는 자료 구조를 직접 구현해야 해야하나 하는 염러가 있었음. 하지만 구글링으로 해당 기능을 구현하는 라이브러리를 찾을 수 있었음.   참고자료: https://stackoverflow.com/questions/23416381/circular-list-iterator-in-python


#### 다른 풀이와 비교
##### #1:
```
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
```
점수 산출하는 과정에서 같은 접근을 했지만 구현이 다르다.
내 코드는 라이브러리에 의존하는 반면, 위 코드는 answers 반복 인덱스를 패턴 배열의 길이로 나눈 나머지를 이용해 배열을 순환시킨다.
내부 라이브러리의 로직도 모르고 사용한 만큼 라이브러리 의존보다 이런 방법을 통해 구현할 수 있게 개선해야겠다.
##### #2:
```
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
```
같아보이지만 아주 짧게 구현된 코드.
감탄이 나온다. 패턴도 배열에 담아 이중 for과 enmerate으로 이렇게 구현할 수 있을거란 생각은 할 수가 없었다...
괴물들...
