# Find the length of the longest consecutive subsequence in a list
### Given a list of numbers find the length of the longest increasing consecutive subsequence

# Suited For
Software Engineer 1

## Difficulty Level
Easy

## Description
Create a program in a language of your choice that finds the length of the longest consecutive subsequence in a given list of numbers

#### Example

Input: [0, 23, 1, 0, 4, 8, 99]

Output:  4

## Hints

* Ensure that you're only counting increasing numbers
* Beware of edge cases


## Follow up questions

* How would you handle finding the length of the longest increasing subsequence that doesn't have to be consecutive?


## Solution (works as is in Coderpad)
```javascript
function longestSubsequence(numbers) {
  if (numbers.length === 0) {
    return 0
  }

  let longestSequence = 1
  let currentSequence = 1

  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > numbers[i - 1]) {
      currentSequence += 1
      if (currentSequence > longestSequence) {
        longestSequence = currentSequence
      }
    } else {
      currentSequence = 1
    }
  }

  return longestSequence
}
```

*Time Complexity*:
`O(n)`

*Space Complexity*:
`O(1)`