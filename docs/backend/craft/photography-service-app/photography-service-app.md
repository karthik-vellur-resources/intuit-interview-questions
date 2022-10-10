# Photographer Microservice

## Tags

Level Options: `senior`, `staff`, `principal`

Role Category: `backend`, `fullstack`

Difficulty Options: `medium`

Interview Type Options: `onsite` `craft-demo`  

## Share with Candidate - Public

### Description (For backend candidates)

Your assignment is to create a microservice which serves the contents of `photographers.json` through a REST API. 

The service should expose three REST endpoints:

- `GET /api/photographers` - returns the list of all photographers.
- `GET /api/photographers/{photographerID}` - returns a single photographer by ID.
- `GET /api/photographers/event/{eventType}` - returns a list of photographers for the specified event type.

Examples of event_types:

- wedding
- birthdays
- wildlife
- sports


The above APIs should only return high-level characteristics of the photographer data. For example - name, contact, avatar, event_types etc. 

Please create unit tests that cover the core logic.

With time permitting, package the application for distribution. Some examples of this:

- Docker image (preferred)
- Tomcat WAR
- Static binary

### Description (For fullstack candidates)

You are building a responsive web application that serves the contents of `photographers.json` through a REST API. The application will contain the following:

#### Backend 

Your backend service should expose 1 REST endpoint:

- `GET /api/photographers` - returns the list of all photographers.


#### Frontend 

Your responsive web application should have:

- A photographer card widget that includes:
      - photographer firstname & lastname
      - avatar
      - event_type
      - location: {city, state}
- A widget to display the photographer cards.
- A widget to accept a event type & zip code information. This widget will enable us to filter data in `photographers.json` based on event type & zip code.

Finally, please create unit tests that cover the core logic.



### Links to Extra Files or References

[photographers.json](https://drive.google.com/file/d/1G4tgUar8auGoRtqS15qJXbYiLl1rT9Np/edit)

### Preparation Instructions to be Shared in Advance

You are free to choose whatever programming language you are comfortable with, SDKs, web frameworks, databases, and online 
resources to complete this exercise.

## Intuit Internal ONLY Do Not Share with Candidate

Estimated time to complete:

- 15-20 minutes to come up with a design.
- 45-70 minutes to code.

### Common Clarification Questions/FAQ
- For the database, you can use In-memory database, you are welcome to use a persistent data store of your choice. You are encouraged
but not required to take advantage of a service code-generation framework of your choice when performing this exercise.

- The problem statement is very open about the coding language, framework and database. It is allowed to use anything to make the 
API working. We set the expectation that the code/API should work and they have their good reasons about the decisions they make 
during the exercise.
- The `photographer.json` contains some sensitive information. If the candidate asks clarification on how to handle it, you can suggest that the candidate encrypt the sensitive data using any library of their choice. This is a good question - please note down and let the assessor panel know if the candidate asks how to handle sensitive data.

### Solution

#### Approach
##### JSON Parser
The most common approach is to read the json file to extract the photographers information. If they
can find a library to help with the process is a bonus point, but we won't set that expectation. Since the information is static, 
we expect they parse the json file just once during the program start, and can ask follow up question on this.

Q: Assuming this json file is updated every 15 minutes with new photographer data? How would your design solve for this?

Points:  If the candidate uses the database, the file hash to compare to tell if the json has been changed is a good approach. If the candidate uses 
the in-memory structure, the same hash idea is still valid, they can use the SpringBoot **@Scheduled** annotation. Other option open for discussion, is using AWS lambda to keep the photographer data updated

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

##### Handling sensitive information

The photographer data in the JSON file contain sensitive(fake) information like social_insurance_number, gender, credit_card information. Bonus points for the candidate if they ask clarifying question on how to handle this data. Ideally, they should encrypt this data in to the database of their choice.


##### Unit Tests 
There are a lot of places can add unit tests.

- Unit test for the json loader with simpler sample data
- Unit test for the three APIs


### How to Assess Candidate / Expected Answer by Level

* A __Senior__ candidate should be able to:

    - Have a working JSON parser/loader.
    - The three required APIs should be working, but okay to give 1 hint from the accessors to debug the problem during the demo time to make it working
    - The three required APIs should return the correct results. 
    - Very good implementation of the three API's; i.e using the appropriate data structures, code reuse, appropriate class and 
    methods definitions, exception handling and logging.
    - Candidates high level understanding of the different database technologies. It is okay to have a partial view and incomplete understanding in certain areas.
    - Candidates identifies that the photographer json data contains some sensitive information. They discuss how to handle saving this data.

* A __Staff__ candidate should be able to:

    - Have a working JSON parser/loader.
    - Very good implementation of the three API's; i.e using the appropriate data structures, code reuse, appropriate class and 
    methods definitions, exception handling and logging.
    - The dockerfile, jar, or war file is produced.
    - Candidates identifies that the photographer json data contains some sensitive information. They discuss how to handle saving this data and save the encrypted data.
    - Apply good design patterns when appropriate. 
    - The three required APIs should return the correct results. 
    - Candidates in-depth level understanding of the different database technologies.
    - The unit tests to cover the core logic, CVS parser and the API

* A __Principal__ candidate should be able to: 
    - All expectations of Staff.
    - Design elegant and scalable solution.
    - Able to identify edge cases and resolve them creatively. 
