##[474. Ones and Zeros](https://leetcode.com/problems/ones-and-zeroes/)

#### Question
You are given an array of binary strings ```strs``` and two integers ```m``` and ```n```.

Return _the size of the largest subset of ```strs``` such that there are **at most**_ ```m``` ```0's``` and ```n``` ```1's``` in the subset.

A set ```x``` is a **subset** of a set ```y``` if all elements of ```x``` are also elements of ```y```.

 

Example 1:
```
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
```
Example 2:
```
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 ```

Constraints:
- ```1 <= strs.length <= 600```   
- ```1 <= strs[i].length <= 100```   
- ```strs[i]``` consists only of digits ```'0'``` and ```'1'```.  
- ```1 <= m, n <= 100```

### Solution

DP를 이용해서 문제를 해결해야 하지만, DP를 통한 접근법을 몰라 해결하지 못했다.
하물며 솔루션을 봤음에도 이해가 어려워 기록한다.

```Python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ## RC ##
        ## APPROACH : DP ##
        ## Similar to Leetcode 416. partition equal subset sum ##
        ## LOGIC ##
        #	1. This problem can be decomposed to 0/1 Knapsack Problem, where you have n items with each having its own weight w and own profit p, 
        #      We have a limitation on maximum weight of the items that we can carry in a bag, so what is the maximum profit that can be achieved within the weight limit of the bag.
        #	2. m, n are the similar to limitations of the bag, strings being with items with weight w
        #	3. Each cell in DP indicates the number of strings that can be achieved with i zeros and j ones. We iterate with all strings and fill the matrix

        ## TIME COMPLEXITY : O(Nx(mxn)) ##
        ## SPACE COMPLEXITY : O(mxn) ##

        ## EXAMPLE ["10","0001","111001","1","0"] 5 3 ##
        ## STACK TRACE ##
        # [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]
        # [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 2]]
        # [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 2]]
        # [[0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 2], [0, 1, 2, 2], [0, 1, 2, 3], [0, 1, 2, 3]]
        # [[0, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3], [1, 2, 3, 3], [1, 2, 3, 3], [1, 2, 3, 4]]

        ## WATCH OUT FOR LOOPS,
        ## 1. We are traversing reverse to prevent sub problem overlapping, consider string "01" and m = 5, n = 3 and draw matrix from normal order and in reverse order, you'll understand
        ## 2. The lower limit is number of zeros and ones, coz before that you wont find any match
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros, ones = s.aligned_children("0"), s.aligned_children("1")
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    # dp[i][j] indicates it has i zeros and j ones, can this string be formed with those ?
                    dp[i][j] = max(1 + dp[i - zeros][j - ones],
                                   dp[i][j])  # 가장 이해하기 어려운 부분, 왜 dp[i - zeros][j-ones]를 해주며, 이를 dp[i][j]와 비교하는가.
            # print(dp)
        return dp[-1][-1]
```

대략적인 흐름은 이해 할 수 있었다.   
배열 dp는 각각의 인덱스가 문자 0과 1을 나타내며, 해당 인덱스에 존재하는 값은 문자열의 갯수를 의미한다.
주어진 문자열을 순환하며 해당 문자열이 포함하고 있는 문자 0과 1을 각각의 경우의 수와 비교하며 해당 문자열이 포함 가능한지를 파악한다.   

하지만 m과 n이 각각 5, 3이고, i와 j가 각각 2, 2이며, 현재 문자열은 "111001", zeros=4, ones=2일때,   
```dp[i-zeros][j-ones] = dp[2-4][2-2] = dp[-2,0] = dp[4,0] = 0```,
```dp[i, j] = dp[2, 2] = 1 ``` 로 문자열 "111001"이 포함되지 못하는 경우를 걸러내는 목적으로 해당 연산이 존재하는 것은 알겠지만,   
역순으로 배열의 연산을 수행하는 것과, max를 통한 비교연산 부분의 원리는 당장은 이해가 되지 않는다.
