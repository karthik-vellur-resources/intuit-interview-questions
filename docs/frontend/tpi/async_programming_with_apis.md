
# Async programming with REST APIs - Share with Candidate - Public

## Description


Given two APIs like below. Write a function that returns all cities in a country.
```
API 1 —> http://www.example.com/states/<country>
Ex: http://www.example.com/states/USA —> ['CA', 'AZ', 'NY', ...]

API 2 —> http://www.example.com/cities/<state>
Ex1: http://www.example.com/cities/CA —> ['San Francisco', 'Los Angeles', 'San Diego', ...]
Ex2: http://www.example.com/cities/AZ —> ['Tucson', 'Phoenix', 'Tempe', ...]
```
getCities('USA') should return an array of all cities in USA.

```  
function getCities(country) {
	let cities = [];
	// Your logic goes here
	return cities;
}
```

## Links to Extra Files or References

`Add any extra content that doesn't fit into this doc`

## Preparation Instructions to be Shared in Advance

`Use Javascript/Typescript and any IDE or in browser interview tools like coderpad, glider etc`

# Intuit Internal ONLY Do Not Share with Candidate

Estimated time to complete: 15-20 minutes

Please note that although a strong candidate knocks off the solution in 15-20 minutes, this question gives a strong signal on many aspects of front end skills by asking more questions on top of this with additional complexities.

### Skills tested by this question

- Problem solving
- knowledge of working with APIs
- Asynchronous programming paradigm
- Ability to write clean code with error handling
- Ability to write tests and cover all edge case scenarios as well



### Common Clarification Questions/FAQ
Intentionally the API contracts given above are very vague, so that the candidate asks the right set of questions to clarify the details.

Some questions expected from the candidate

- Should the function return the actual data or a promise?
- Should I use native promises or async/await?  
- What are the HTTP methods(GET / POST)
- What are the expected response codes by the services
- Do we have a variant of the service that takes a bulk input instead of single input so that we can optimize the API calls

All of the above questions give a signal that the candidate is well versed in dealing with the APIs. This also helps to level the candidate. The depth of the questions indicate the seniority/experience of the candidate.

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

Solution 1
```
function getCities(country) {
  return getStatesByCountry(country)
    .then((states) => {
        const promisesList = states.map((state) => {
            return getCitiesByState(state);
        });
        return Promise.all(promisesList);
    })
  .then((citiesArrayByStateList) => {
     let cities = [];
     citiesArrayByStateList.map((citiesArrayByState) => {
        cities = [...cities, ...citiesArrayByState];
     });
    return cities;
  });
}

const getStatesByCountry = (country) => {
	return fetch(`http://www.example.com/states/${country}`);
}

const getCitiesByState = (state) => {
	return fetch(`http://www.example.com/cities/${state}`);
}

getCities('USA').then((allCities) => {
  console.log('allCities --> ', allCities);
});

/*

Sample code to mimic the APIs and verify if the code is working correctly when run.

const getStatesByCountry = (country) => {
  const tempData = ['CA', 'AZ', 'NY'];
  return Promise.resolve(tempData);
}

const getCitiesByState = (state) => {
  const tempData = ['San Francisco', 'Los Angeles', 'San Diego'];
  return Promise.resolve(tempData);
}
*/

```

### Time Complexity:

The problem intentionally has the second API to take only one input at a time. We expect the candidate to optimize that constraint by making API calls in parallel. Also it is expected from the candidate on how the approach would change depending on the scale(ie. the first API call returning thousands of records. A strong and experienced candidate talks about throttling the API calls etc.

### How to Assess Candidate / Expected Answer by Level


A strong SWE2 candidate should be able to converge on the brute force solution within 15 minutes and show progress towards optimal solution with hints.
A strong SSE candidate should be able to converge on the optimal solution within 20 minutes with no hints.
A strong Staff candidate should be able to converge on the production ready code with all error handling within 20 minutes with no hints.

Although we expect a working solution(within a given time) in order to pass the interview, we also assess how they approach the problem and solve(because it's an important skill to write code that is easy for the team to contribute and extend)

### Variation/Similar problems

The same question can be extended to test for other front end skills required to perform at intuit like working experience of using React.js, css skills etc.

- How does the implementation change if the API2 in the problem is changed into a bulk API that accepts multiple states as input.
- Write a React component with a select choice button of the country and when selected display a list of all citities (helps to test the React/Redux skills as well)
- Add styling to make the page responsive.
- Write a polyfill for `fetch` (helps further to test the skills of core js & browser fundamentals - https://github.com/github/fetch)

## Additional notes

The question is designed to keep the problem statement simple, so that they can demonstrate their skills without too much getting entangled understanding the problem. This question is inspired from a widely asked Systems design question of 'Desing a system for URL shortnening' (Problem statement is simple and yet enables the interviewer to get into depth within the time constraints)

## Tags

`easy`, `phonescreen`, `sse,`, `swe2`, `frontend`

