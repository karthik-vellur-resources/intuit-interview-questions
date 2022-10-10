---
name: Implement a Fixed Size Queue
difficulty: Medium
level:
  - Senior SWE
  - Staff SWE
---

# Implement Fixed Size Queue

## Tags

Level Options: `swe2`, `sse`, `staff`

Role Category: `backend`

Difficulty Options: `easy`

Interview Type Options: `phonescreen`, `onsite`

## Share with Candidate - Public

### Description
Implement a queue with a fixed size limit. It must allocate and initialize, only once, all the 
memory that it will use.  It should provide methods or functions to enqueue and dequeue in a 
FIFO manner. It should also give the ability to peek at the next element to be dequeued.

## Intuit Internal ONLY Do Not Share with Candidate
### Hints

* Use an Array to store values in the queue
* Use variables to store the state of the queue

### Follow up questions

* Is your solution thread safe? If not, what do you need to do to make it thread safe?


### Possible Solution (works as is in Coderpad)
```java
import java.io.*;
import java.util.*;


class Solution {

  public static void main (String[] args){

    Queue q = new Queue(5);

    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);

    System.out.println("Front element is: " + q.peek());
    q.dequeue();
    System.out.println("Front element is: " + q.peek());

    System.out.println("Queue size is " + q.size());

    q.dequeue();
    q.dequeue();

    if (q.isEmpty())
      System.out.println("Queue Is Empty");
    else
      System.out.println("Queue Is Not Empty");
  }

  static class Queue {
    private int arr[];               // array to store queue elements
    private int front;               // front points to front element in the queue
    private int rear;                // rear points to last element in the queue
    private final int capacity;      // maximum capacity of the queue
    private int count;               // current size of the queue

    Queue(int size) {
      arr = new int[size];
      capacity = size;
      front = 0;
      rear = -1;
      count = 0;
    }

    public void dequeue() {
      if (isEmpty()) {
        System.out.println("UnderFlow\nProgram Terminated");
        System.exit(1);
      }

      System.out.println("Removing " + arr[front]);

      front = (front + 1) % capacity;
      count--;
    }

    public void enqueue(int item) {
      if (isFull()) {
        System.out.println("OverFlow");
        throw new RuntimeException("Queue OverFlow");
      }

      System.out.println("Inserting " + item);

      rear = (rear + 1) % capacity;
      arr[rear] = item;
      count++;
    }

    public int peek() {
      if (isEmpty()) {
        System.out.println("UnderFlow");
        throw new RuntimeException("Queue UnderFlow");
      }
      return arr[front];
    }

    public int size() {
      return count;
    }

    public Boolean isEmpty() {
      return (size() == 0);
    }

    public Boolean isFull(){
      return (size() == capacity);
    }

  }
}
```
