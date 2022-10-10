# Checksum
### Calculate a "checksum" given a grid of integers expressed as a string

Estimated time to complete: 20-25 minutes

## Tags
`Tags: easy medium phonescreen onsite swe2 sse backend frontend fullstack`

## Description
Calculate a "checksum" given a grid of integers expressed as a string.

Example:
- Input: `"5 1 9 5\n7 5 3\n2 4 6 8"`
- Output: `18` because `(9 - 1) + (7 - 3) + (8 - 2) = 8 + 4 + 6 = 18`

### Approach:
Tokenize the input string such that it becomes a list of list of integers. Then find the max and min of each list of integers and calculate the difference between the max and the min. Return the sum of the differences from each list.


### Sample Solution:

```python
class NumberGrid:
    def __init__(self, input_string):
        self.rows = self.parse_string(input_string)

    def parse_string(self, input_string):
        return [[int(num) for num in row_string.split()] for row_string in input_string.split('\n')]

    def checksum(self):
        return sum([self.max_min_diff(row) for row in self.rows])

    def max_min_diff(self, row):
        return max(row) - min(row)

print(NumberGrid("5 1 9 5\n7 5 3\n2 4 6 8").checksum())
```

### Time Complexity:
O(n) where n is number of integers in the input string

### Repeat above more approaches if there are alternatives
The logic should be similar to the above but what's of interest is how the candidate organizes and codes up his/her solution.

### Variation/Similar problems
A layering question is to change the code to support a different method of computing the checksum and observe how easy/hard it is for the candidate's written solution. Ask about the SOLID principles and tradeoffs between inheritance and dependency injection.

## Rubric / How to Assess Candidate
The main thing to look for is quality of code organization and structure. Also the ability to justify their approach.

### Expected Solving Time
15 minutes for coding and 5-10 minutes for layering questions. A strong SWE2 can implement a working solution but may require a major overhaul in their code when layering questions are asked. A strong SSE candidate can justify their reasoning on how their code is structured and be able to modify the code in an elegant way.

### Reference:
https://adventofcode.com/2017/day/2
