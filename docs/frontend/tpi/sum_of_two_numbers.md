# Return indices of two numbers such that they add up to target - Share with Candidate - Public

## Description

Given an array of integers nums and an integer target, write a function that returns indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.


```
    Example:
    Input: nums = [7,5,3,8,10,1,9], target = 6
    Output: [1,5]
```

## Preparation Instructions to be Shared in Advance

`Use Javascript/Typescript and any IDE or in browser interview tools like coderpad, glider etc`

# Intuit Internal ONLY Do Not Share with Candidate

Estimated time to complete: 10-15 minutes

Please note that although a strong candidate knocks off the solution in 15-20 minutes, this question gives a strong signal on many aspects of front end skills by asking more questions on top of this with additional complexities.

### Skills tested by this question

- Problem solving
- knowledge of working with Arrays and Maps.
- Ability to write clean code with error handling
- Ability to write tests and cover all edge case scenarios as well

## Solution

### Approach:

For a seasoned front end engineer who works on async programming calling APIs would easily solve this. We expect the solution to be production ready with all possible scenarios thought through and error handling done. 

One ideal approach to be followed is below, however, depending on the situation some steps can be skipped but we look for a 360 degree approach towards the problem.

1. Candidate asks all the clarifying questions needed.
2. Candidate thinks through the solution loud and presents what is the approach they are taking.
3. Candidate writes the pseudo code or breaks down the problem into smaller pieces to tackle individually.
4. Candidate writes clear interfaces for the broken down functions and little documentation on what the function does.
5. Candidate analyses whether the template he wrote above solves the problem as expected.
6. Candidate NOW writes the actual code.
7. Candidate runs then code and makes sure it works for all cases including edge cases.
8. Candidate proactively suggests to write tests and write few tests.

Catches:
- Candidate who rushes to write the code and writes some hasty solution without considering all scenarios.
- Candidate when stuck is not open to take the hints given by the interviewer (not a good team player).
- Candidate who sticks to only one way to writing the code and is not open to make the code extensible for other engineers to contribute.

### Sample Solution:

There are different variants of solution depending on the approach the candidate takes. 

### Solution 1 - Brute force approach
This solution is to just iterate the array using two loops to find if the sum is equal to the target.
```
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function solution(nums, target) {
  if (nums.length < 2) {
    return [];
  }
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
  return [];
}
```

### Time complexity
Lets say array has n elements then - 

For 1st element - we will check for (n - 1) elements
For 2nd element - we will check for (n - 2) elements
For 3rd element - we will check for (n - 3) elements 
and so on...

Thus, the total iterations would be - [(n - 1) + (n - 2) + (n - 3) + ... + 2 + 1]
If we simplify the above expression we will get -

n * (n - 1) / 2 = n2 - 2n ≈ n2

Thus, our time complexity would be - O(n2).

### Space complexity
Since we are not using any extra data structure hence our space complexity would be O(1).


### Solution 2

- Loop through the array
- Check if we have encountered the current element before
- If we have, we will return the index of this element and the index of the difference of the target and the current element. We will only encounter this element before only if we have saved the difference of target and the element which when added to the current element gives the target itself.
- If we haven’t, the we will save the difference of the target and current element.
- Repeat the process
- We store the difference as key and the corresponding index as value in a Map.

```
function getIndices(nums, target) {
    // Array to store the result
    result = [];
    // Map to store the difference and its index
    index_map = new Map();
    // Loop for each element in the array
    for (let i = 0; i < nums.length; i++) {
        let difference = target - nums[i];
        if (index_map.has(difference)) {
            result[0] = i;
            result[1] = index_map.get(difference);
            break;
        } else {
            index_map.set(nums[i], i);
        }
    }
    return result;
};
```

### Time Complexity
Since we are iterating the array only once, the time complexity would be O(n).

### Space Complexity
Since we need a Map of the size of the array, the space complexity would be O(n).

### How to Assess Candidate

Generally this problem can be used for SWE2.

A strong candidate should be able to solve this relatively quickly using approach similar to solution 2 mentioned.

## Tags

`easy`, `phonescreen`, `swe2`, `frontend`
