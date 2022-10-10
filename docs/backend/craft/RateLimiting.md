# Rate Limiting

## Tags

Level Options: `senior`, `staff`, `principal`

Role Category: `backend`

Difficulty Options: `medium`

Interview Type Options: `phonescreen` `craft-demo`  

## Share with Candidate - Public

### Description

Implement a rate-limiting algorithm that can be used to restrict the number of calls to a web service, using either fixed window counter or sliding window counter approach (check https://www.figma.com/blog/an-alternative-approach-to-rate-limiting/)

Given a function signature with the following parameters: unique key string, time period in seconds, and a maximum number of calls per period,
 implement an algorithm that determines if more calls can or cannot be be made within the current time period. The start code is as follow:
```java
import java.io.*;
import java.util.*;

class Solution {
  public static void main(String[] args) {
    
    //Return false
    System.out.println(rateLimit("device_info", 30, 3));
    System.out.println(rateLimit("device_info", 30, 3));
    System.out.println(rateLimit("device_info", 30, 3));
    
    //Return true
    System.out.println(rateLimit("device_info", 30, 3));    
  }
  
  public static boolean rateLimit(String key, int intervalInSecs, int maxLimit) {
      // Return "true" if no more requests are allowed, and "false" otherwise
      return false;
    }
  }
}

``` 

```
Input:
    // The rate-limiting function allows maximum of 3 requests in a 30sec period 
    System.out.println(rateLimit("device_info", 30, 3));
    System.out.println(rateLimit("device_info", 30, 3));
    System.out.println(rateLimit("device_info", 30, 3));
    System.out.println(rateLimit("device_info", 30, 3));
        
Output:
     false
     false
     false
     true
```

### Preparation Instructions to be Shared in Advance

* You can use any programming language & IDE of your choice

## Intuit Internal ONLY Do Not Share with Candidate

Estimated time to complete: ~30 minutes for a strong SSE candidate


### Common Clarification Questions/FAQ
1. You do not have to address or deal with multi-threading or a distributed system implementation

### Solution

The above problem can be solved by
```
Fixed window counter approach:
1. Create a bucket class, which holds the current time period, and the number of requests allowed for this period
2. Create a collection (HashMap) that holds the buckets for different keys (resources)
3. On function call, get the current key bucket, see if it has expired or not found, and create a new one if this is the case
4. See if the bucket is already full, if "yes", return "true"(block the request), if "no" add another request to the bucket counter and return "false"
5. Bonus point for considering and implementing a synchronization
```

```
Sliding window (alternative) counter approach:
1. Define a queue
2. Add a current timestamp to the queue
3. Get rid of the older timestamps in the queue
4. Count the number of elements in the queue, make a decision if to block or not
5. Bonus point for considering and implementing a synchronization
```

#### Sample Solution

```java
import java.io.*;
import java.util.*;

class Solution {
  public static void main(String[] args) {
    
    //false
    System.out.println(rateLimit("device_info", 30, 3));
    System.out.println(rateLimit("device_info", 30, 3));
    System.out.println(rateLimit("device_info", 30, 3));
    
    //true
    System.out.println(rateLimit("device_info", 30, 3));
  }
  
  static class Tuple {
    long scaleSeconds;
    int  numberRequests;
  }
    
  static HashMap<String, Tuple> cache = new HashMap<String, Tuple>();
  
  public static boolean rateLimit(String key, int intervalInSecs, int maxLimit) {
    // Fixed window counter solution
    // 1. Get the current bucket, see if it has expired, if "yes", create one
    // 2. See if the bucket is already full, if "yes", return "true", 
    // 3. if the bucket is not full, increment the bucket counter and return "false"
    long currTimeSecs = System.currentTimeMillis() / 1000;
    long scaleSeconds = currTimeSecs / intervalInSecs;
    
    if(cache.containsKey(key)){
      Tuple tuple = cache.get(key);
      
      if(tuple.scaleSeconds == scaleSeconds){
        // Bucket found for this period 
        if(tuple.numberRequests >= maxLimit){
          // Block
          return true; 
        }
        tuple.numberRequests += 1;
        return false;
      } else {
        // The bucket has expired, replace with a new one
        tuple = new Tuple();
        tuple.scaleSeconds = scaleSeconds;
        tuple.numberRequests = 1;
        
        cache.put(key, tuple);
        // Do not block
        return false;
      }
      
    } else {
      // Bucket not found, create a new one
      Tuple tuple = new Tuple();
      tuple.scaleSeconds = scaleSeconds;
      tuple.numberRequests = 1;
      
      cache.put(key, tuple);
      
      // Do not block
      return false;
    }
  }
}
```

### How to Assess Candidate / Expected Answer by Level

A strong SSE candidate should be able to clearly identify and convey the main steps and come up with a working algorithm or close to working algorithm with a few hints within 30 minutes.

### Variation / Similar problems

- [Distributed Systems Rate Limiting]({{ config.repo_url }}/blob/master/to_be_migrated/DistributedSystems/RateLimiting.md)

### References

- [Rate Limiting](https://www.figma.com/blog/an-alternative-approach-to-rate-limiting/)
