[Programmers] Coding Test Practice: 숫자 문자열과 영단어
===========================================
[문제보기](https://programmers.co.kr/learn/courses/30/lessons/81301)

#### 풀이 접근 방법:
1. while 반복을 통해 ```s[0]```이 숫자 문자인지 확인한다
2. ```s[0]```이 숫자 문자인 경우, ```answer```에 해당 문자를 더하고 해당 문자를 ```s```에서 제거한다
3. ```s[0]```이 숫자 문자가 아닌 경우, 파이썬의 문자열 내장함수인 ```string.find(num)```이 0을 반환하는 영문 숫자를 찾는다.
4. ```s.find(num) == 0```인 경우, ```s```문자열에서 ```num```의 문자열 길이만큼 앞 문자를 제거한다.
5. ```answer```에 ```num```에 해당하는 숫자를 더한다.

#### 내가 작성한 코드:
```python
def solution(s):
    answer = ''
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while s != '':
        if s[0] in nums:
            answer += s[0]
            s = s[1:]
        for num in words:
            if s.find(num) == 0:
                s = s[len(num):]
                answer += str(words.index(num))
                break
            
    return int(answer)
```

### 겪은 문제:
풀이법을 쉽게 생각해냈으나, 코드로 구현하는 과정에서 syntax 에러를 빈번하게 겪었다.   
최초 코드에서는 문자열 슬라이싱을 ```s = s[len:]```가 아닌 ```s[len:]```으로만 적용하여 무한루프가 돌았다.    
```answer += str(word.index(num))``` 또한 우변의 결과를 문자열로 변환하지 않아 문자열 + 정수 연산으로 인한 에러가 발생하였다. 
