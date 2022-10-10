# Suited For
Software Engineer 1, Software Engineer 2 and Senior Software Engineer

## Difficulty Level
Easy 

### Given Problem statement:

Given an array of numbers, write a function that determines which numbers are happy.

#### Definition
A happy number is number that eventually leads to 1 after a sequences of steps.

 * Starting with any positive integer, replace the number by the sum of the squares of its digits.
 * Repeat the process until the number either equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

```js

Input:
[7,105,13,1,4,0,-2,784]


Output:
    7,13,1,784,

```

### Approach:
The above problem can be solved by coding the process described in definition.

```js
* Watch for edge cases on 1, 4 and 0.
```

### Sample Solution:
```js
import java.util.*;

public class HappyNumber {
    public static void main(String [ ] args) {
        List<Integer> input = new ArrayList<>();

        input.add(7);
        input.add(105);
        input.add(13);
        input.add(1);
        input.add(4);
        input.add(0); 
        input.add(-2);
        input.add(784);

        for(Integer i : input) {
            if (isHappy(i)) {
                System.out.println(i + ",");
            }
        }
    }

    public static int happify(int n) {
        int sum = 0;

        while (n > 0) {
            sum += sqr(n % 10);
            n /= 10;
        }

        return sum;
    }

    public static int sqr(int n) {
        return (n * n);
    }

    public static boolean isHappy(int n) {
        if (n == 1) {
            return true;
        } else if (n == 4 || n == 0){
            return false;
        } else {
            return isHappy(happify(n));
        }
    }
}
```

### Solving Time
Approx 10 - 15 mins


### Reference:
https://en.wikipedia.org/wiki/Happy_number
