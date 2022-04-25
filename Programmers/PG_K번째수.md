[Programmers] Coding Test Practice: K번째수
===========================================
[문제보기](https://programmers.co.kr/learn/courses/30/lessons/42748)

#### 풀이 접근 방법:
1. 제한사항 확인 -> array 최대 길이 100, commands 최대 길이 50: 완전탐색 경우의 수 50,000
2. 풀이 순서: 1) array 배열 깊은 복사, 2) 배열 자르기, 3) 배열 정렬, 4) k번째 수 answer에 담기

#### 내가 작성한 코드:
```
import copy

def solution(array, commands):
    answer = []
        
    for idx,command in enumerate(commands):
        answer.append(copy.deepcopy(array))
        del answer[idx][command[1]:]
        del answer[idx][:command[0]-1]
        answer[idx].sort()
        answer[idx] = answer[idx][command[2]-1]
        
    return answer
```
개선할 수 있는 부분 충분히 생각해서 개선해보기
