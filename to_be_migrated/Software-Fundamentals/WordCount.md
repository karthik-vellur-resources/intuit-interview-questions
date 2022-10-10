# Implement Word Count
### Find the total number of words in a given String using any programming language

# Suited For
Senior Software Engineer and below

## Difficulty Level
Easy to medium

## Description
Create a program in a language of your choice that counts the number of words
in a given string.

#### Example

input:  " this     is a  test  "

output:  4

## Hints

* Read characters individually
* Maintain word count for current state
* Beware of edge cases


## Follow up questions

* What would need to change to create a word histogram?
* How would you distribute this program?


## Solution (works as is in Coderpad)
```
import java.io.*;
import java.util.*;


class Solution {
  public static void main(String[] args) {
    String input = " this     is a  test  ";
    String cleanedInput = input.trim();
    int count = 0;

    if(cleanedInput.length() > 0){
      count++;
      char[] inputAsArray = cleanedInput.toCharArray();
      char previous = inputAsArray[0];

      for(char c : inputAsArray) {
        if(Character.isWhitespace(c) && previous != ' '){
          count++;
        }
        previous = c;
      }
    }
    System.out.println("final count is: " + count);
  }
}
```

*Time Complexity*:
O(n)

*Space Complexity*:
O(n)