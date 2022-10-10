# Linked List Intersection
### Design and implement a data structure for [Least Recently Used (LRU)](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU) cache



Estimated time to complete: 30 minutes

Tags: medium phonescreen onsite sse swe2 backend fullstack

## Description
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: `get` and `put`.

`get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
`put(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Example:
```java
LRUCache cache = new LRUCache(2); // 2 is capacity of the cache. 

cache.put(1, 4);
cache.put(2, 5);
cache.get(1); // returns 4
cache.get(5); // returns -1
cache.put(3, 6); // removes key 2
cache.get(2); // retruns -1
```

### Approach:

Implementation of LRU cache requires leveraging multiple data structures. 
It needs to keep track of access and insertion order of elements and provide quick access to elements.

Following two data structures can be used to design the LRU Cache.
1. Queue: A queue implemented using doubly linked list. The maximum elements in the queue will be equal to the capacity
of the cache. The most recently accessed cache element will be at front while the least accessed element will be at the
end.
2. Map: A hash map storing the key value pairs for each entry in cache. With key being the positive integer and value 
addressing the queue node corresponding to the key.

### Sample Solution:

```java
// Java program to get intersection point of two linked list

// define doubly linked list node
import java.io.*;
import java.util.*;

class Node {
  int key;
  int value;
  Node prev;
  Node next;

  public Node(int key, int value) {
    this.key = key;
    this.value = value;
  }
}

class LRUCache {
  Node head;
  Node tail;
  HashMap<Integer, Node> map;
  int cap;

  public LRUCache(int capacity) {
    this.cap = capacity;
    this.map = new HashMap<>();
  }

  public int get(int key) {
    if (map.containsKey(key)) // Key Already Exist, just update the access order by moving the node to front.
    {
      Node Node = map.get(key);
      removeNode(Node);
      addAtFront(Node);
      return Node.value;
    }
    return -1;
  }

  public void put(int key, int value) {
    if (map.containsKey(key)) // key already exists. remove and move to front.
    {
      Node Node = map.get(key);
      Node.value = value;
      removeNode(Node);
      addAtFront(Node);
    } else {
      Node newnode = new Node(key, value);
      if (map.size() >= cap) // maximum capacity reached. remove least accessed element
      {
        map.remove(tail.key);
        removeNode(tail);
        addAtFront(newnode);
      } else {
        addAtFront(newnode);
      }

      map.put(key, newnode);
    }
  }

  public void addAtFront(Node node) {
    node.next = head;
    node.prev = null;
    if (head != null)
      head.prev = node;
    head = node;
    if (tail == null)
      tail = head;
  }

  public void removeNode(Node node) {

    if (node.prev != null) {
      node.prev.next = node.next;
    } else {
      head = node.next;
    }

    if (node.next != null) {
      node.next.prev = node.prev;
    } else {
      tail = node.prev;
    }
  }

}

class Solution {
  public static void main(String[] args) {
    LRUCache cache = new LRUCache(2); // 2 is capacity of the cache. 
    
    cache.put(1, 4);
    cache.put(2, 5);
    System.out.println(cache.get(1)); // returns 4
    System.out.println(cache.get(5)); // returns -1
    cache.put(3, 6); // removes key 2
    System.out.println(cache.get(2)); // retruns -1
  }
}

```

### Time Complexity:
Time Complexity: O(1) for `get` and `put`
Auxiliary Space: O(n)

### Alternate Approach:

Method 1(Use LinkedHashMap): Ideally, we'd like candidate to not use a composite data structure from language library. 
But this is also a valid approach to implement LRUCache. 
[LinkedHashMap](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedHashMap.html) in Java is based on Hash table 
and LinkedList that provides insertion or access order of keys inserted or accessed in the Map. Initializing LinkedHashMap
with [access order](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedHashMap.html#LinkedHashMap-int-float-boolean-) would provide the LRU capability out of the box.

```java
public class LRUCache {
        private LinkedHashMap<Integer, Integer> map;
        private final int CAPACITY;
        public LRUCache(int capacity) {
            CAPACITY = capacity;
            map = new LinkedHashMap<Integer, Integer>(capacity, 0.75f, true){
                protected boolean removeEldestEntry(Map.Entry eldest) {
                    return size() > CAPACITY;
                }
            };
        }
        public int get(int key) {
            return map.getOrDefault(key, -1);
        }
        public void set(int key, int value) {
            map.put(key, value);
        }
    }
```

### Variation

For senior candidates, the problem can be extended to include thread safety.
1. What would happen when cache is shared by multiple threads trying to `get` and `put`?
2. How to make the cache thread safe? 
If time permits, interviewer can ask questions on unit tests for the code implemented.

## Rubric / How to Assess Candidate

1. A candidate with strong Java background should be able to suggest the alternative solution along with the primary 
solution.
2. A strong SWE2 candidate should be able to figure out the right data structures to use within 15 mins and complete 
implementation in other 15 to 20 mins.
3. A strong SSE candidate should be able to figure out the right data structures in 10 mins and complete 
implementation in other 15 to 20 mins. This leaves time to ask questions on multi threading.

### Expected Solving Time
30 mins 

### Reference:
https://leetcode.com/problems/lru-cache/

