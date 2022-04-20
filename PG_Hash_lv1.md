[Programmers] Coding Test Practice: 완주하지 못한 선수
====================================================
[문제보기](https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3)

### 풀이 접근 방법:
1. participant의 원소를 Key로 가지며 해당 원소의 인원의 수를 Value로 갖는 dictionary 'participants' 생성
2. completion의 원소를 돌며 해당하는 participants의 value를 1씩 감소시키고, 만약 해당 value가 0이라면 key, value 쌍을 dictionary에서 제거
3. 단 한 명만의 선수만이 완주하지 못하므로, 결과적으로 value 값이 1인 하나만의 key, value 쌍이 남게된다.

### 내가 작성한 코드:
```
def solution(participant, completion):
    answer = ''
    participants = {}
    for p in participant:
        try:
            participants[p] += 1
        except KeyError:
            participants[p] = 1
            
    for c in completion:
        participants[c] -= 1
        if participants[c] == 0:
            del participants[c]
    answer = list(participants)[0]
    
            
    return answer
```

### 겪었던 어려움:
1. 예전에 한번 풀려고 했던 문제여서 그런지 완전탐색으로 구현된 solution 함수가 존재 했었다.   테스트 코드는 통과하는 함수였지만 시간복잡도가 O(n^2)였으므로, n의 최댓값이 100,000인 성능테스트를 통과하지 못하는 코드였다.   딱히 문제점은 아니지만, 기존 솔루션이 작성되어 있는 경우 접근법을 기존 코드에서 찾으려는 이상한 습관이 생기는것 같아 주의가 필요하다.
