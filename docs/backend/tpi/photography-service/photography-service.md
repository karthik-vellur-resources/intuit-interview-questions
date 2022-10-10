# Photography service App design 

## Tags

Level Options: `intern`, `swe1`, `swe2`

Role Category: `backend`

Difficulty Options: `easy`

Interview Type Options: `phonescreen`, `onsite`

## Share with Candidate - Public

### Description

Design an app using appropriate data structures and algorithms -  where users can specify for what type of event and location they need a photographer. You can refer to  https://www.thumbtack.com/​  as an example.

We want two functionalities -

- You will design a method which saves these photographer profiles in some in memory data store. A profile consists of location, rates and types of events handled by that photographer.

- a search functionality which will return a list of profiles for a user’s specific needs using the data store designed above.

Example events: Wedding, Rehearsal dinner, Bridal Shower, Birthday Parties, Corporate Events 

Feel free to ask questions and document any assumptions.

### Example

#### Input
```
eventType: Wedding
location San Jose, CA
```

#### Output
```
"Dream Weddings", location='San Jose, CA', rate=$150, eventType: Wedding, Rehearsal Dinner, Bridal Shower
"Memorable Moments", location='San Jose, CA', rate=$180, eventType: Wedding, Reception
"Beautiful weddings ", location='San Jose, CA', rate=$100, eventType: Wedding
```


### Preparation Instructions to be Shared in Advance

* You can use any programming language & IDE of your choice

## Intuit Internal ONLY Do Not Share with Candidate

**Move to Part 2 based on performance in Part 1**

### Layering question

**Part 2:**
Add a feature to rank photographers based on user reviews.


### Further layering questions (if the above is too easy)
1. As part of a user’s search preference, include the date and duration of their event
2. As part of a user’s search preference, include the maximum cost they will pay
3. Implement a distance function based on city, state, and zip code


### Estimated time to complete
* ~ 15-20 minutes to come up with a design

* ~25-30 minutes to code

### Common Clarification Questions/FAQ

Clarifications when asked:
 
* Profile
    * Only given by photographers
    * Don’t need to go in depth on each element of the profile
    * For now, could be a link to their own website (this app doesn’t have to store any
photo galleries; just links are sufficient)
* Rates
    * Only given by photographers
    * Can charge different rates for different types of events (this is probably a layering
    question, keep it simple initially)
    * All events are charged hourly
    * Assume all rates are always in U.S. dollars
* Location
    * U.S.-only app
    * For now, let the candidate decide if it should include city, state, and/or zip code
    * Some candidates may start with a city name; that’s ok too
* Events
    * Example events: Wedding, Rehearsal dinner, Bridal Shower, Birthday Parties, Corporate Events
* Don’t worry about user login or any HTML/CSS
* Don’t worry about databases or hosting the service/app. We need only java classes and
methods
*   For each search operation, a user must give two preferences: event type and location.

*   For now, ignore duration as a preference.

*   If the candidate asks you to determine weights for ranking results, ask them how they
would determine it if they were building this app themselves. If they’re having trouble, you may suggest that:
    *   Any photographer not in the user’s area (e.g. different city or more than 60 miles away) has a lower ranking
    *   Any photographer who does not support the user’s preferred event type has a lower ranking

*   A user review may include a user, a rating, and a comment.
*   Alternatively, the aggregate review rating can be attached to a photographer profile.

### Solution

#### Approach

* Create data structures to capture photographer profiles
* Write an algorithm to sort the list of pre-created photographer profiles with ‘relevance’ to
the user preference.
    *   Example: Uses a comparator function on a list of photographer profiles so that results are sorted in some way (e.g. location match/proximity, number of eventType matches, lowest rates)
    *   A function that simulates user search by taking inputs on user preferences, matches the relevant photographers, and returns results
    *   May use a mock dataset
    *   May use a placeholder for checking a DB or calling another API
    *   Uses relevant data structures for search results to return a profile with location, rates and/or types of events handled by each photographer


#### Time Complexity
`
Depends on the algorithm and approach used by the candidate.
`

* O(p) - If candidate chooses to save photographer profiles in a map/dict with eventType as key. `p` is the number of photographers in the input `location` with the desired `eventType`

### How to Assess Candidate / Expected Answer by Level

**INTERN:** 
```
* Candidate asks questions to ensure understanding of the problem statement
* Candidate asks questions to get clarification on requirements
* Uses suitable data structures to represent photographer’s profile that includes location,
event types covered, and their rates
* Comes up with a suitable algorithm to show relevant search results based on user’s
preferences on location, event types and rates
* Results should be ordered by relevance, with most relevant result first
* Design is extensible/abstract enough to work for different types of events, rates, etc. e.g.
professional events vs. family events, or weddings vs. graduations
* Describes basic test cases -- gives expected input and output
```

**SWE1 & SWE2** 
All the above plus below - 
```
* Comes up with and codes a viable solution with little guidance
* Sees where their solution might fail; are cognizant of their solution’s limitations
* Able to quickly explain choice of data structures
* Writes/describes tests covering edge cases with little to no prompting
* Can discuss time and space complexity of chosen/coded algorithms
```