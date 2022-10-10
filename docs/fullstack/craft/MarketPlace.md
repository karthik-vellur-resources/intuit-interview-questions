# Market Place

## Tags

Level Options: `swe2`, `senior`, `staff`

Role Category: `fullstack`

Difficulty Options: `medium`, `hard`

Interview Type Options: `craft-demo`, `onsite`

## Share with Candidate - Public

### Description

You are building a Market Place where people can post contract jobs to be performed.  The jobs are bid on in an auction format similar to eBay but for jobs/tasks instead products.

The Market Place has two actors:

1. Poster: Person looking for someone to complete a specific job/task.
2. Bidder: Self-employed individual that is bidding on work at a fixed price.
 
### Product Requirements

* The site has a home page that:
	* Displays the 10 most recently published job postings.
	* Displays the top 10 most active and open jobs (measured by number of bids).
	* Includes a link to publish a new job posting.

* The site has a page allowing new jobs to be posted that:
	* Displays a form collecting the following data points:
		* Job description with maximum length of 16KB.
		* Job requirements with maximum length of 16KB.
		* Name and contact info of the job poster.
	* Displays the current lowest bid amount.
	* Displays the number of bids.
	* Displays the auction expiration date/time and time remaining to bid.
	* Includes a form for placing a bid.

* The system:
	* Automatically closes bidding when the posting expiration date/time is reached.
	* Automatically assigns the lowest Bidder as the winner of the auction when the auction is closed.

* Extend these requirements as you see fit to create a positive user experience.

### System Targets

* There are 100K registered Bidders with 2K new Bidders registered per day.
* 1k jobs are posted every day growing at a rate of 250 jobs per week.
* Every job receives an average of 20 bids.

## Intuit Internal ONLY Do Not Share with Candidate

### Front End Candidate Instructions

#### 30 Minute Target

Have the candidate build the job page inclusive of details of the selected job and a form for submitting a bid. Have them walk through the data points they plan to collect how them. The candidate can mock backend service responses as needed using the library/framework of their choice.

#### 60 Minute Target

Have the candidate build all of the pages described in the requirements taking into consideration all of the 30 minute targets.


#### Evaluating Level

##### Strong Senior / Staff

Candidate has covered the following considerations:

* Suggested solution for user auth and session management.
* Suggested appropriate security measures for protecting PI data in flight.
* Has a plan for server latency when populating views (eg. loading screen / spinner and appropriate timeouts).
* Discussed testability and types of testing (unit, integration, visual automation).
* Understands Web performance metrics and the use of tools like Lighthouse and Core Web Vitals.
* Considered accessibility requirements as part of the design.


Candidate has coded/shown:

* A React component using appropriate hooks or life cycle methods to setup views with 
* Asynchronous data retrieval of job details.
* Method for posting a bid to a the job and confirming its completion to the user.
* Good separation of concerns/testability.
* At least one example unit test.


### Backend End Candidate Instructions

#### 45 Minute Target

Have the candidate start by designing the data model and system architecture.  Ask about database type & engine choice (eg. SQL vs NoSQL, MySQL vs Dynamo). How do they plan to scale the service to support increased traffic. Spend half the time on the design side and then have them code an endpoint to support receiving a job bid. Have them psuedo-code / assume APIs as necessary.


#### Evaluating Level

##### Strong Senior / Staff

Candidate has covered the following considerations:

* Asked about / suggested solution for user auth and session management.
* Ability to articulate their API design (eg. URI, HTTP method(s), HTTP status code responses, request body, and response).
* Asked about/ suggested appropriate security measures for protecting PII data in flight and at rest.
* Can explain how performance of the service is measured.
* Has a plan for scaling service compute appropriately based on growth characteristics – horizontal scaling / autoscaling for example.
* Can speak to atomicity of database operations and possible distribution of data to support scaling.
* Discussed testability and types of testing (unit, integration, and performance).

Candidate has coded/shown:

* An endpoint using appropriate HTTP method (POST).
* Performs input checking / validation.
* Validates user session (psuedo-code is the best that can be done).
* Performs error handling using best practices - responding with appropriate HTTP response codes (eg. 404 for a missing job).
* Handles database connections appropriately – shouldn't create database locks unnecessarily.
* Good separation of concerns/testability.
* At least one example unit test.


### Full Stack Candidate Instructions

Full stack candidates with at least an hour of available time can complete an end to end slice of the system covering most of the 30/45 minute targets for both the Front End and Back End sections above.  

#### Evaluating Level

##### Strong Senior / Staff

Candidate should have a good understanding of all of the front end and back end topics listed in the respective sections above.