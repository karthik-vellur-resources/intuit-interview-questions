# Suited For
Senior or Above

## Difficulty Level
3 on a 1-5 scale, 5 being hardest

### Given Problem statement:
Web Services like AWS and Intuit impose Rate Limits on how many
Requests per Second a Client can make. For example, you can only poll
the AWS CloudFormation Status Service less than 30 times/second.

Design a solution for a Rate-Limiting Scheme under these conditions:
1. A single DataCenter/region
2. We have different Web Services and want to impose different rate-limits on them
3. Each Client has a Client Id
4. Each Client has a different Rate-Limit per Web Service

Be sure to explain any issues you can think of! For example, what if
1000 Clients all make simultaneous calls to the same Web Service?

BONUS:
Extend this solution to a multi-DataCenter/Region solution. Discuss
additional architecture designs and trade-offs you have to make, and
how you solve them. Example: how do you deal with drift?

### Approach:
Single-DC: use Redis to synchronize Request Rates, specifically
INCR. See [the RateLimiter
Pattern](https://redis.io/commands/INCR#pattern-rate-limiter-1). Each
Rate is mapped to a Key of the form Hash(ClientId, WebServiceId,
Timestamp) and then checked against the current value in Redis as
above.

Multi-DC: lots of fun here, main issues are with time drift. At
minimum, be aware of NTP for syncing Server clocks and some sort of
fast data replication scheme. Multi-Master MySQL Asynchronous
Replication IS fast enough, but has some issues scaling beyond 4
regions or so. Cassandra/other 'eventually-consistent' schemes may be
too slow.

#### Naive Algorithm
Any solution that simply tries to check a Counter against a
non-synchronized Resource. Example: 'I store a counter in memory
on-server', not good because what about other Servers?

#### Optimal Algorithm
As above, use Redis INCR or Memcached [CAS](https://github.com/memcached/memcached/wiki/Commands#cas)

### Sample Solution:
As above

### Time Complexity:
N/A

### Alternate Approach:
Anything that is a synchronized counter over a network

### Variation/similar problems
N/A

### Solving Time
45 Minutes. This is an architectural discussion, but requires
knowledge of Resource Synchronization, Hashing, Web APIs, etc.

### Reference:
As above