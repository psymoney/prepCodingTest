**[Programmers] Coding Test Practice: 모의고사**
[문제보기](https://programmers.co.kr/learn/courses/30/lessons/42840)

*풀이 접근 방법:*
1. 각각의 수포자가 찍는 방식은 반복되는 패턴이 존재한다. (예: 1번은 1,2,3,4,5,...)
2. 각 패턴을 circular linked list와 같이 순환하는 구조로 구현 -> itertools 라이브러리의 cycle 함수 이용
3. 반복문으로 주어진 답안 목록의 원소를 각각의 패턴과 비교하며 점수 산출
4. 산출된 점수 배열을 해당 배열의 최댓값과 비교하며 최댓값과 동일한 인덱스에 정수 1을 더하여 최종 반환 배열에 담는다.

*내가 작성한 코드*
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

*겪었던 어려움:*
1. 2번째 풀이 접근방법 중 순환하는 자료 구조를 직접 구현해야 해야하나 하는 염러가 있었음. 하지만 구글링으로 해당 기능을 구현하는 라이브러리를 찾을 수 있었음.   참고자료: https://stackoverflow.com/questions/23416381/circular-list-iterator-in-python
