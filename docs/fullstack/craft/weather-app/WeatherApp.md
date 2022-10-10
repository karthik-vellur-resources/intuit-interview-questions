# Weather App

## Tags

Level Options: `sse`, `senior`, `staff`

Role Category: `fullstack`

Difficulty Options: `medium`

Interview Type Options: `craft-demo`, `onsite`

## Share with Candidate - Public

### Product Requirements

You are building a responsive web application that helps users track the essential weather data for a given location. The application will contain the following:

1. A widget to accept a city name or zip (postal) code information.
1. A widget to display the current weather condition that includes:
      - day (e.g. "Monday, March 1st, 2021")
      - weather description (e.g. "Misty")
      - temperature
      - pressure
      - humidity and
      - wind information
3. A widget to display the daily weather condition for 10 days that includes:
      - day (e.g. "Monday, March 2nd, 2021")
      - weather description (e.g. "Partly Cloudy")
      - min and max temperature
4. A control to switch between imperial (e.g. miles/hour for wind) or metric (e.g. Celsius for temperature) units.
5. The application will remember the input provided by the user such as city name/zip, and imperial/metric units until the user changes it.

### Additional instructions
  * Add psuedo code or an actual example of a unit test.
  * Feel free to extend the product requirements as you see fit.

## Intuit Internal ONLY [Do Not Share with Candidate]

### Front-end Candidate Instructions

#### 30 Minute Target

Have the candidate build the weather application with the product requirements #1 and #2 for accepting city name/zip information and the current weather. The candidate can mock back-end service responses as needed using the library/framework of their choice.

#### 60 Minute Target

Have the candidate build all of the specified product requirements taking into consideration all of the 30 minute targets (#1 - #5 of the product requirements).

#### Evaluating Level

##### Strong Senior / Staff

Candidate is able to discuss a clear point of view and approach for the following:

* Described the ReSTful / GraphQL APIs for updating preferences, and fetching current and forecast data.
* Stacked views for the 10 day forecast utilizing CSS grid layout concepts.
* Has a plan for server latency when populating the widgets (eg. loading screen / spinner and appropriate timeouts).
* Discussed testability and types of testing (unit, integration, visual automation).
* Understands web performance metrics to track (e.g. Core Web Vitals).
* Considered accessibility requirements as part of the design.
* Discussed approaches for building and packaging the web application (e.g. minification, bundling in to static assets - js, css, images).
* Understands how web applications are deployed (e.g. deployment to a CDN).

Candidate has coded/shown:

* Responsive UI.
* Asynchronous data retrieval for current and forecast weather data.
* Good separation of concerns/testability.
* At least one example or pseudo code for unit test.
* Used appropriate client-side storage for storing user preference (e.g. localstorage).
* Has fallback UI rendered if a widget fails to load (e.g. due to an uncaught exception, network error etc.).


### Back-end Candidate Instructions

#### 30 Minute Target

Have the candidate build the APIs that enable product requirements #1 and #2, for accepting city name/zip information and providing the current weather. The candidate can mock the weather data using the library/framework of their choice.

#### 60 Minute Target

Have the candidate build all of the specified product requirements taking into consideration all of the 30 minute targets (#1 - #5 of the product requirements).

#### Evaluating Level

##### Strong Senior / Staff

Candidate is able to discuss a clear point of view and approach for the following:

* Described the solution for user auth and session management.
* Described the data model for storing user preferences, and weather data.
* Described the appropriate database type to use (SQL, vs. NoSQL).
* Discussed data retention/archival policy.
* Discussed testability and types of testing (unit, integration, and performance).
* Described how the application would be deployed and accessible by the front-end (containers, CI/CD, hosting etc.).
* Discussed how performance of the service is measured.
* Has a plan for scaling service storage and compute appropriately based on growth characteristics – horizontal scaling / autoscaling for example.

Candidate has coded/shown:

* APIs with proper request/response contracts and HTTP status codes.
* Performs input checking / validation.
* Performs error handling using best practices - responding with appropriate HTTP response codes (eg. 404 for a city name/zip that is not available for reporting).
* Good separation of concerns/testability.
* At least one example or pseudo code for unit test.
* Shown good technology choices.. i.e SpringBoot, JPA, various java 8+ features such as streams, optional, completable future, etc.

### Full Stack Candidate Instructions

Full stack candidates with at least an hour of available time can complete an end to end slice of the system covering most of the 30 minute targets for both the front-end and back-end sections above - A responsive app that shows the current weather of a given location using appropriate APIs and mocked data.

#### Evaluating Level

##### Strong Senior / Staff

Candidate should have a good understanding of all of the front-end and back-end topics listed in the respective sections above.


