# AppFounders API

### An API for the AppFounders Web App

Estimated time to complete: 4-6 hrs

## Tags

`Tags: medium craft-demo sse staff backend cloud-engineer`

## Description

Your team is building a new app called AppFounders. The purpose of this app is to connect entrepreneurs to other entrepreneurs in their area. Your team has amassed a collection of data about entrepreneurs including which companies they founded or are associated with, their email addresses, and what state they're in.

You're responsible for creating an API which presents this data to the React-based frontend interface.

## Requirements

Create a GraphQL or REST API which serves [this data set](https://gist.github.com/leftrightleft/a08af6e03dcfaa578b5bd4231924c1d4) to the web app.

The API should have the following capabilities:

- Return all information about a specific founder (app_name, state, email, etc.)
- Return all founders of a specific app
- Return all founders in a particular state
- Add new founders and apps to the database

Use any database, idiomatic HTTP framework, and any of the following languages to build this service:

- Java/Kotlin/Scala
- Python
- Ruby
- Go
- JavaScript/NodeJS

While this service is obviously a toy, please treat it as you would a real web service. That means write production quality code per your standards and include _at least_ the following:

- Unit Tests
- README documentation
- An architecture diagram

Please post your solution to a public GitHub (or BitBucket or GitLab) repository and include instructions for running your service.

## Rubric / How to Assess Candidate

What to look for from a candidate:

- Code Repository and Documentation
  - API documentation (Swagger, MKDocs, etc.)
  - Code repo (Github, GitLab, etc.)
  - Quality README including local execution
  - CI/CD
- API Design
  - Are proper HTTP verbs used?
  - Is there documentation?
  - Is the API well designed and logical?
  - Do the response codes make sense
  - Is the response valid JSON?
  - Did they make use of query parameters and path parameters correctly?
- Code
  - Proper error handling
  - Unit tests
  - Reasonable logic
  - How did the candidate handle Null data?
- Database
  - Database selection
  - SQL/No SQL. Reasoning?
  - Did they include schema documentation?
- Architecture
  - Did the candidate include Infrastructure in their repo?
  - Containerized/Serverless?

Follow-up questions:

- How would you host/productionize this service?
- How would you scale this service?
- How would you secure this service?
- How would you monitor this service?
- How would you make your service more resilient to failure?
- Who do you see as the customers in this case, and who would you collect feedback from them during the design and build process?
