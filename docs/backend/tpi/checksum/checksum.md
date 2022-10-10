# Checksum

This question can be a multi-part question.  At the end of the first question, you should know if the candidate displays technical proficiency at their level.  If you feel like you need more info about the candidate's skills, have them work on Part 2.  

**Note:** Please keep in mind the candidate's experience.  If it's obvious that the candidate struggled with the basics in part 1, don't force them into part 2; it's harder.   

## Tags

Level Options: `swe1`, `swe2`, `sse`, `staff`

Role Category: `backend`, `fullstack`

Difficulty Options: `easy`

Interview Type Options: `phonescreen`

## Part 1 - Share with Candidate - Public

### Description

In this problem, you will build an application which calculates the checksum of a data set.  The input comes in the form of a table.  For each row in the table, determine the difference between the largest value and the smallest value; the checksum is the sum of all those differences.

### Example

Input table:
```
5 1 9 5
7 5 3
2 4 6 8
```

- The first row's largest and smallest values are `9` and `1`.  The difference is `8`.
- The second row's largest and smallest values are `7` and `3`.  The difference is `4`.
- The third row's largest and smallest values are `8` and `2`.  This row's difference is `6`.

In this example, the checksum would be `8 + 4 + 6 = 18`

### Notes/Tips

- Make sure to talk through your thought process!  We're interested in hearing how you approach the problem
- We're looking for code quality, but be aware of time
- Use the programming language you're most comfortable with
- Think about edge cases
- Remember, we want you to succeed!  Feel free to ask any questions and work with your assessor if you get stuck 👍

### Input
```
798 1976 1866 1862 559 1797 1129 747 85 1108 104 2000 248 131 87 95
201 419 336 65 208 57 74 433 68 360 390 412 355 209 330 135
967 84 492 1425 1502 1324 1268 1113 1259 81 310 1360 773 69 68 290
169 264 107 298 38 149 56 126 276 45 305 403 89 179 394 172
3069 387 2914 2748 1294 1143 3099 152 2867 3082 113 145 2827 2545 134 469
3885 1098 2638 5806 4655 4787 186 4024 2286 5585 5590 215 5336 2738 218 266
661 789 393 159 172 355 820 891 196 831 345 784 65 971 396 234
4095 191 4333 161 3184 193 4830 4153 2070 3759 1207 3222 185 176 2914 4152
131 298 279 304 118 135 300 74 269 96 366 341 139 159 17 149
1155 5131 373 136 103 5168 3424 5126 122 5046 4315 126 236 4668 4595 4959
664 635 588 673 354 656 70 86 211 139 95 40 84 413 618 31
2163 127 957 2500 2370 2344 2224 1432 125 1984 2392 379 2292 98 456 154
271 4026 2960 6444 2896 228 819 676 6612 6987 265 2231 2565 6603 207 6236
91 683 1736 1998 1960 1727 84 1992 1072 1588 1768 74 58 1956 1627 893
3591 1843 3448 1775 3564 2632 1002 3065 77 3579 78 99 1668 98 2963 3553
2155 225 2856 3061 105 204 1269 171 2505 2852 977 1377 181 1856 2952 2262
```

## Part 2 - Share with Candidate - Public

### Description

Awesome job on Part 1!  Now we're going to focus on the **evenly divisible values** in our input table.  The goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number.  Find these numbers on each line, divide them, then add each line's result.

For example, in this table:

```
5 9 2 8
9 4 7 3
3 8 6 5
```

- In the first row, the only two numbers that evenly divide are `8` and `2`; the result of this division is `4`.
- In the second row, the two numbers are `9` and `3`; the result is `3`.
- In the third row, the result is `2`.

In this example, the sum of the results would be `4 + 3 + 2 = 9`.

What is the sum of each row's result in the input provided for Part 1?


## Intuit Internal ONLY Do Not Share with Candidate

Answer to part 1: `41919`

Answer to part 2: `303`

### Common Clarification Questions

- Should I expect decimal numbers in the input?
  - No.  Just the input you see above
- In Part 2, are there **only** two divisible numbers per line?
  - Yes

### Assessing the Candidate

With this question, we're assessing code quality, not puzzle solving ability.  Think about the following questions when assessing the candidate, but keep in mind the level the candidate is applying for.

- Is the code well organized?
- Are the object names reasonable?
- Did the candidate take an OOP approach?
- Did the candidate ask clarifying questions?
- Did the candidate discuss edge cases?
- What level of mastery did the candidate display for their chosen language?
- Did the candidate seem confident in their approach and are they able to justify it?
- Is the approach they used the most efficient?  If not, could they identify a more efficient path?
- If part 2 was given to the candidate, was a major refactor needed from part 1?  

### Solutions

#### Part 1

A good approach would be to tokenize the input string such that it becomes a list of integers. Then find the max and min of each list of integers and calculate the difference between the max and min. Return the sum of the differences from each list.

Python Sample 1 (OOP approach):
```
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

Python Sample 2 (itertools approach):
```
import io, itertools 
with io.StringIO(s) as f:
    lines = [[int(n) for n in l.split()] for l in f]

print(sum(max(l)-min(l) for l in lines))
```

Javascript:
```
let input = document.getElementsByTagName('pre')[0].innerHTML;
let rows = input.match(/[^\r\n]+/g);
rows = rows.map(row => row.match(/\w+/g).map(el => +el));

let array_max = (row) => Math.max.apply(null, row);
let array_min = (row) => Math.min.apply(null, row);

let sum = rows.reduce((acc, row) => acc + array_max(row) - array_min(row), 0);

console.log(sum);
```

#### Part 2

An approach on this part would be to iterate through each of the rows, then divide all the items in the row to find the remainder that equals 0.

Python:
```
with io.StringIO(s) as f:
    lines = [[int(n) for n in l.split()] for l in f]

ans2 = sum(b//a for l in lines for a,b in itertools.combinations(sorted(l),2) if b%a==0)
```

### References

- Advent of Code: https://adventofcode.com/2017/day/2
- Reddit solutions: https://www.reddit.com/r/adventofcode/comments/7h0rnm/2017_day_2_solutions/


