# Player DB Microservice

## Tags
Level Options: `swe2`, `senior`, `staff`, `principal`

Role Category: `backend`,`fullstack`

Difficulty Options: `medium`

Interview Type Options: `craft`  

## Share with Candidate - Public

### Description (For backend candidates)

Your assignment is to create a microservice which serves the contents of `Player.csv` through a REST API. 

The service should expose two REST endpoints:

- `GET /api/players` - returns the list of all players.
- `GET /api/players/{playerID}` - returns a single player by ID.

Please create unit tests that cover the core logic.

With time permitting, package the application for distribution. Some examples of this:

- Docker image (preferred)
- Tomcat WAR
- Static binary

### Description (For fullstack candidates)

You are building a responsive web application that serves the contents of `Player.csv` through a REST API. The application will contain the following:

#### Backend

The service should expose 1 REST endpoint:

- `GET /api/players` - returns the list of all players.

#### Frontend 

Your responsive web application should have:

- A player card widget that includes:
      - player nameGiven
      - height & weight
      - debut
      - location: {birthCity, birthState}
- A widget to display the player cards.

Finally, please create unit tests that cover the core logic.


### Links to Extra Files or References

[Player.csv](http://drive.google.com/file/d/1fIbUzvHjE2SuDLkwohDgfD7dWL54ZeUQ)

### Preparation Instructions to be Shared in Advance

You are free to choose whatever programming language you are comfortable with, SDKs, web frameworks, databases, and online 
resources to complete this exercise.

## Intuit Internal ONLY Do Not Share with Candidate

Estimated time to complete:
- 15-20 minutes to come up with a design.
- 45-60 minutes to code.

### Common Clarification Questions/FAQ
- For the database, you can use In-memory database, you are welcome to use a persistent data store of your choice. You are encouraged
but not required to take advantage of a service code-generation framework of your choice when performing this exercise.

- The problem statement is very open about the coding language, framework and database. It is allowed to use anything to make the 
API working. We set the expectation that the code/API should work and they have their good reasons about the decisions they make 
during the exercise.

- The playerID is unique can be used as a primary key

- The retroID and bbrefID columns correlate the player data to external data sets. Specifically the csv data is from the Lahman dataset and the retroID correlates the Lahman dataset to the retrosheet.org dataset, whereas the bbrefID correlates the Lahman dataset to the baseball-reference.com dataset. For the purposes of the problem, the data can be considered metadata about the player and returned as is in the API responses. 

### Solution

#### Possible Approaches
##### CSV Parser
The most common approach is to read the csv file line by line and seperate the string with comma to extract the information. If they
can find a library to help with the process is a bonus point, but we won't set that expectation. Since the information is static, 
we expect they parse the csv file just once during the program start, and can ask follow up question on this.

Q: Assuming the CSV file is huge and there is a requirement that the server has to be serving the traffic in 3 seconds upon start, 
what could be the optimization here? The CVS file could be changed once a month.

Points: The key point is to eliminate the unneccessary parsing/processing time with the quite static information. If the candidate 
uses the database, the file hash to compare to tell if the CSV has been changed is a good approach. If the candidate uses 
the in-memory structure, the same hash idea is still valid, the difference is to expect a binary dump saved after the first 
paring, and reload the binary dump instead of the parsing the CSV again.

##### Databases

The popular choices are in-memory hashmap, MySQL, MongoDB. We see the candidate will throw the SQL/NoSQL/Cassendra/MongoDB/MySQL/Postgres
on table with only words. Please immediately follow up on the detail. If the candiate cannot provide the detail about the database 
characteristics but keeps talking only about the keywords, it is a very bad sign. HashMap is acutally a good choice due to the time
constraint for the demo. The performance-wise is a very reasonable. If the candidate uses a real database, follow up on the reason
and choice.

Q: What makes you pick the (blank)?

Q: If you have more time, will you choose a different persistence layer? Why that one? What could be the benefits?

Q: You mentioned about the SQL and NoSQL. Could you share your experience with us?

Q: You mentioned about (blank). (MongoDB, Cassandra and etc,) Could you share your experience with us?


##### Unit Tests
There are a lot of places can add unit tests.

- Unit test for the CSV loader with simpler sample data
- Unit test for the two APIs
- Since it is quite a tiny service, it is feasible to run the real web server, and test against it in automatic way

### How to Assess Candidate / Expected Answer by Level
A __Senior__ candidate should be able to: 
- Have a working CSV parser/loader.
- The two required APIs should be working, but okay to give 1 hint from the accessors to debug the problem during the demo time to make it working
- The two required APIs should return the correct results. 
- The dockerfile, jar, or war file is produced.
- Candidates high level understanding of the different database technologies. It is okay to have a partial view and incomplete understanding in certain areas.

A __Staff__ candidate should be able to: 
- Have a working CSV parser/loader.
- Very good implementation of the two API's; i.e using the appropriate data structures, code reuse, appropriate class and 
methods definitions, etc.
- Apply good design patterns when appropriate. 
- The two required APIs should return the correct results. 
- Candidates in-depth level understanding of the different database technologies.
- The unit tests to cover the core logic, CVS parser and the API

A __Principal__ candidate should be able to: 
- All expectations of Staff.
- Design elegant and scalable solution.
- Able to identify edge cases and resolve them creatively. 
