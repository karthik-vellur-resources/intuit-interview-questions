# Pareto Frontier

## Tags


Difficulty Options: `medium`

Interview Type Options: `phonescreen` `onsite`

Level Options: `swe2` `sse` `staff` `pe` 

Role Category Options: `backend` `data` `fullstack`

## Share with Candidate - Public

### Description
Given a set of 2d points, find the pareto frontier of that set.
Let the pareto frontier be the set of all points which are pareto optimal.

A point p<sub>i</sub> is pareto optimal if ∄ p<sub>j</sub> s.t. p<sub>i</sub> ≠ p<sub>j</sub> ∧ p<sub>i</sub>.x < p<sub>j</sub>.x ∧ p<sub>i</sub>.y < p<sub>j</sub>.y

for copy/paster usage the following may be easier:

A point p_i is pareto optimal if there does not exist a second point p_j s.t. p_i \neq p_j \and p_i.x < p_j.x \and p_i.y < p_j.y

A point p_i is pareto optimal if ∄ p_j s.t. p_i ≠ p_j ∧ p_i.x < p_j.x ∧ p_i.y < p_j.y

## Intuit Internal ONLY (Do not share with candidate)

Estimated time to complete: `40 minutes`

### Common Clarification Questions/FAQ
Some expected questions:
```
- clarification as to what defines a pareto optimal point or a pareto frontier
- clarification as to the type and range of values present in the point pairs (Integers, all possible integers)
- Can there be duplicates [can the point (3,3) appear twice?]\(no, the input is a set)
```

### Solution

Sort the values largest to smallest along one axis, resolving ties using the other axis. Track the highest value seen on the second axis, take points largest to smallest from the list, add them to the frontier set if the second axis value is > tracked value. update the tracked value:

Pseduocode:
```
frontier(set):
	output = ∅
	sorted = sort(set) p_1.x > p_2.x || p1.x == p2.x and p1.y > p2.y
	output.append(sorted[0])
	tracked_y = sorted[0].y
	for (p in sorted.drop(1)):
		if (p.y > tracked_y):
			output.append(p)
			tracked_y = p.y
	return output
```

#### Possible Approaches

There are several approaches that can be taken:
- Bruteforcing (simply compare all points pairwise)
- Dynamic Programming (the approach for more than 2d pareto froniter discover)
- Sorting based approach for efficent optimization of the 2d case
#### Sample Solution

```python
def frontier(data):
	frontier = set()
	sorted_data = sorted(data, reverse=True) #sorted resolves ties in the desired way by default
	frontier.add(sorted_data[0])
	max_y = sorted_data[0][1]
	for p in sorted_data[1:]:
		if p[1] > max_y:
			frontier.add(p)
			max_y = p[1]
	return frontier
```

Some example cases:
```python
input_1 = {(2, -2), (1, 3), (1, 2), (1, 1), (-1, 1)}
output_1 = {(2, -2), (1, 3)}


input_2 = {(2,2), (4,4), (3,5)}
output_2 = {(4, 4), (3, 5)}

input_3 = {(2,2), (4,4), (3,5), (1,7)}
output_3 = {(4, 4), (1, 7), (3, 5)}


input_4 = {(5,5), (3,2), (2,3), (-1, 4), (4,-1)}
output_4 = {(5, 5)}
```

Cases 2-4 are resonably good examples of frontier calculation. Case 1 is a good test case.

#### Time Complexity
`O(n log(n))` using the optimal method, `O(n^2)` brute forcing, and a ratehr variable output using DP strategies.

### How to Assess Candidate / Expected Answer by Level
**ALL LEVELS**
```
* Candidate asks clarifying questions to establish understanding of a Pareto Frontier
* Candidate asks clarifying questions to establish the range of valid inputs
* Candidate comes up with at least the brute force method without prompting
* Candidate arrives at Sorting based method with no more hints than that the problem is solvable in O(n log(n))
* Candidate writes some edge case tests without prompting
* Code is simple, readable, and maintainable
```
### Reasonable Extensions:
If candidates fly through the question and you wish to go further (without code) you can ask the candidate some follow up questions:
```
- what would it take to extend this solution to a 3rd dimension
- what if theres so much data you want to run the algorithm on more than one computer
- What if instead of operating on the set X, you had to operate on the set F(X) for some input function?
- How would various approaches scale with differnt kinds of scale (# of dimensions, # of points)

```