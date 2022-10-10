# Suited For
Software Engineer 1, Software Engineer 2

## Difficulty Level
Easy to Medium

### Given Problem statement:

Given a stack of integers, sort it in ascending order using another temporary stack.


```js
Input : [34, 3, 31, 98, 92, 23]
Output : [3, 23, 31, 34, 92, 98]

Input : [3, 5, 1, 4, 2, 8]
Output : [1, 2, 3, 4, 5, 8]
```

### Approach:
1. Create a temporary stack say tmpStack.
2. While input stack is NOT empty do this:
   - Pop an element from input stack call it temp
   - while temporary stack is NOT empty and top of temporary stack is greater than temp,
     pop from temporary stack and push it to the input stack
   - push temp in temporary stack
3. The sorted numbers are in tmpStack

### Sample Solution:

```js
// Java program to sort a stack using
// a auxiliary stack.
import java.util.*;

class SortStack
{
    // This function return the sorted stack
    public static Stack<Integer> sortstack(Stack<Integer>
                                             input)
    {
        Stack<Integer> tmpStack = new Stack<Integer>();
        while(!input.isEmpty())
        {
            // pop out the first element
            int tmp = input.pop();

            // while temporary stack is not empty and
            // top of stack is greater than temp
            while(!tmpStack.isEmpty() && tmpStack.peek()
                                                 > tmp)
            {
                // pop from temporary stack and
                // push it to the input stack
            input.push(tmpStack.pop());
            }

            // push temp in tempory of stack
            tmpStack.push(tmp);
        }
        return tmpStack;
    }

    // Driver Code
    public static void main(String args[])
    {
        Stack<Integer> input = new Stack<Integer>();
        input.add(34);
        input.add(3);
        input.add(31);
        input.add(98);
        input.add(92);
        input.add(23);

        // This is the temporary stack
        Stack<Integer> tmpStack=sortstack(input);
        System.out.println("Sorted numbers are:");

        while (!tmpStack.empty())
        {
            System.out.print(tmpStack.pop()+" ");
        }
    }
}
```

### Time Complexity:
Time complexity of the above solution is O(n^2).

### Alternate Approach:

NA


### Variation/similar problems

Sort a stack using recursion
Find maximum in stack in O(1) without using additional stack
Reverse string using Stack
Reverse a number using stack

### Solving time
20 to 30 mins

### Reference:
https://www.geeksforgeeks.org/sort-stack-using-temporary-stack/