# Suited For
Staff/Principal/Above

## Difficulty Level
4 out of 5

## Assessing the Candidate
This is a long problem with many parts. We do **not** expect a good
candidate to get through the entire problem, or to perfectly solve
each section. See the Grading Rubric below for details. This is a
Design Question first and foremost, and it is OK for a Candidate to
write their code in pseudo-code, as long as the core ideas are correct
and accurate.

There are five Main Points:
1. Use a Dict-of-Queues data structure to Put/Get Items on the correct sub-Queue in O(1) expected time.
2. Design a simple set of Message Classes that support an Operation Field and a Data Field
3. Know that sockets exist and what a Server Loop does
4. Know how to dispatch Threads to handle multiple Requests concurrently
5. Use multiple Locks (one for the Dict, one for-each Queue) to Lock the Data Structures at the greatest level of Granularity

A Candidate is scored on how many of the above Points they correctly answer.

**You as the interviewer should help the Candidate work through each
  Section.** Please make sure that **you** understand each part of the
  Problem before asking. Your goal is to help the Candidate work
  through the entire Design Problem without giving them the solution.

### Grading Rubric
| Points Total      | Grade | Notes |
| ----------- | ----------- | ----------- |
| 1      | F       | Candidate should not advance |
| 2   | D        | Candidate should only advance if done well on other Problems |
| 3   | C        | Pass, Candidate should advance |
| 4   | B        | Pass, Candidate is doing great |
| 5   | A        | Pass++, very good sign |

NOTE: I have never seen anyone score 5, and only a few people score 4.

### Given Problem statement:
A MessageQueue is a Server with (at minimum) this API:

1. Put(Key, DataObject): Put/register a DataObject on the
MessageQueue. The DataObject is placed at the end of the Queue.

2. Get(Key): Retrieve the DataObject at the Head of the Queue
associated with the Key. Return None if no DataObject exists.

We really want to implement our own MessageQueue, so let's design one
from scratch and write some code for each main component.

### Approach:
1. PART 1: Data Structures
Every Server is basically a Network Interface over some Data
Structures. What Data Structure should we use to support the stated
design?

We have some performance requirements; we need Put(K, DO) to run in
O(1) amortized time, and Get(K) to run in O(1) amortized time.

Sketch a Data Structure and write a function for each of `Put(K, DO)`
and `Get(K)` that interacts with your Data Structure.

2. PART 2: Message Design
We send Messages to a MessageQueue for the different supported
Operations. Design a Message format as a Class or JSONObject. What
fields do we need to support both the `Put(K, DO)` and `Get(K)`
operations?

You can assume that both the `byte[] serializeToBytes(Message
message)` and `Message marshallFromBytes(byte[] bytes)` functions
exist and will be used to convert your Message format to/from bytes.

3. PART 3: Server Loop
Sockets are the standard Software Object to receive bytes over a
Network. We want a Binary Protocol for our MessageQueue, and already
have an IntuitProtocolSocket with these four functions:
- bind((HOST, PORT)): bind (register) to the given network Host and Port.
- listen(): the Socket is now ready to accept Client connections
- IntuitProtocolSocket, Address = accept(): accept a connection from a Client. Block until a Client makes a Request.
- Message receive(): receive a Message.

Write a Server Loop using the IntuitProtocolSocket and its
functions. Make sure that we can handle multiple connections.

4. PART 4: Manipulate the Data Structure
Now that we have a Server Loop, enhance it so that the `Get(K, DO)`
and `Put(K)` functions are called when the appropriate Message is
received. Write the code to examine a Message and dispatch to the
correct function.

5. PART 5: Threading
Our Message Queue Server can only handle one Message at a time. This
is not good! Let's enhance our Server Loop to handle multiple Messages
using Threading. Write code to create a new Thread for each Message,
and handle any Data Structure manipulation in it.

6. PART 6: Synchronization and the GIL
Enhance your code to use a single Global Intuit Lock (GIL) to prevent
concurrent Writes to your Data Structure. What are some drawbacks of
using the single GIL?

Let's enhance our locking scheme. Propose and implement a more
fine-grained Locking Scheme that supports this scenario: a Write
Message for an Image must not block a Write Message for a Tax Return.

#### Naive Algorithm / Warning Signs
1. Using a single Queue for the Data Structure (need Queue-per-Type)
2. Using complex classes for the Message, a simple JSON Object is sufficient
3. Not creating/running a Thread for a Message
4. Not using a Lock-per-Queue-per-Type, just using the GIL
5. No familiarity or unable to work with simple Socket API

#### Optimal Algorithm
See Sample Solution

### Sample Solution:
```python
import queue
import threading
import socket
import json

# Table-of-Queues. This is the Data Structure in the Server. We're not
# using a Heap anywhere because we don't need to support
# Priorities/Run-Levels

GIL = threading.Lock()


class MQRecord:
    def __init__(self):
        self.Q = queue.Queue()
        self.L = threading.Lock()


QUEUE_TABLE = {
    "tax_return": MQRecord(),
    "qbo_invoice": MQRecord(),
    # Etc. Pre-allocate queues based on popular/most-requsted Types
}


def put(K, DO):

    with GIL:
        if K not in QUEUE_TABLE:
            QUEUE_TABLE[K] = MQRecord()

    record = QUEUE_TABLE[K]

    with record.L:
        record.Q.put(DO)


def get(K):

    record = QUEUE_TABLE.get(K, None)

    if not record:
        return None

    with record.L:
        if not record.Q.empty():
            return record.Q.get()
        else:
            return None


class Request:
    PUT = 0
    GET = 1

    def __init__(self, K, V, operation):
        self.K = K
        self.V = V
        self.operation = operation

    # See simple_mq.py for implementation of to/from bytes

class Response:
    def __init__(self, K, V, error=None):
        self.K = K
        self.V = V
        self.error = error

    # See simple_mq.py for implementation of to/from bytes

def handle_connection(conn, addr):
    with conn:
        # Just assume a RequestMessage is less than 4096 bytes
        message = Request.from_bytes(conn.recv(4096))
        if message.operation == Request.GET:
            K = message.K
            data = get(K)
            response = Response(K, data)
        elif message.operation == Request.PUT:
            K = message.K
            V = message.V
            put(K, V)
            response = Response(K, True)

        conn.sendall(response.to_bytes())


def server_loop(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        while True:
            # Just wait until a connection comes in, dispatch to Thread
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_connection, args=(conn, addr))
            thread.start()

```

### Time Complexity:
O(1) on average

### Alternate Approach:
- RabbitMQ
- Redis
- ActiveMQ

### Variation/similar problems
- Implement an HTTP Server
- Implement a File Server

### Solving Time
> 1 hour, this problem has multiple parts and requires end-to-end
  knowledge of Systems.

### Reference:
- [Redis Queue](https://redislabs.com/ebook/part-2-core-concepts/chapter-6-application-components-in-redis/6-4-task-queues/6-4-1-first-in-first-out-queues/)
- [ActiveMQ](https://activemq.apache.org/)
- [Celery Distributed Task Queue](http://www.celeryproject.org/)