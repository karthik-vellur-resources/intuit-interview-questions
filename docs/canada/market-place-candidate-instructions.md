# Market Place Craft Demo

## Candidate Instructions

You are being provided a skeleton project that to be used during the technical portion of your interview.

Please read the description and set up the project as described below. Once you have successfully set up the project, you may wish to explore the code so that you are familiar with it.

A technical assessor will set aside 15 minutes prior to the technical assessment to assist you with any last-minute technical setup.

Please note: **It is expected that you will have this project working on your own equipment prior to the interview starting.**

### Project Description

You are building a Market Place where people can post contract jobs to be performed.  The jobs are bid on in an auction format similar to eBay but for jobs/tasks instead products.

The Market Place has two actors:

1. Poster: Person looking for someone to complete a specific job/task.
2. Bidder: Self-employed individual that is bidding on work at a fixed price.
 
### Simplified Design

      _____               _____
     |     |             |     |
     | Job |  <---On---  | Bid | 
     |_____|             |_____|
    
        ^          ^
       / \        /
        |        /
        |      Bids
      Posts    /
        |     /
        |    /
      ______
     |      |
     | User |
     |______|

---------------------
#### Instructions for Front End Setup 

##### Requirements
- Node 14 or higher and NPM v6 or higher
    - To install Node and NPM please see [the NPM documentation](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

##### Steps to install

1. Once you have the prerequisite libraries installed, unzip the provided craft skeleton into a location of your choosing.
1. Navigate into the newly-created `marketplace-frontend-react` directory.
1. `npm install`

Great job! Now you should be all set to run the project!

##### Running the project

In the project directory, you need only to run `npm start`. This will spin up a simple server at [http://localhost:3000](http://localhost:3000) - you can navigate to this url in a browser of your choice to view the app.

##### Available commands

###### `npm run start`

Runs the app in development mode. Open it at [http://localhost:3000](http://localhost:3000) to view.

The page will reload if you make edits.\
You will also see any lint errors in the console.

###### `npm run test`

Launches the test runner in interactive watch mode.\
Runs tests using the Jest framework - see the `create-react-app` documentation section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) or the native [Jest documentation](https://jestjs.io/docs/getting-started) for more information.

##### Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

To learn about Jest, check out the [Jest documentation](https://jestjs.io).

-----------------
#### Instructions for Back End Setup 

This is a simple, bare-bones service that will be used as the basis as the back end for your craft demonstration.

##### Requirements
- [Java11](https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/downloads-list.html)
- [Maven](https://maven.apache.org/download.cgi)

##### Be sure the java version is correct!
- `java -version` at the command line will display the Java version. *You should be using Java 11*
- `mvn -v` at the command line should show which Java version that maven is using. *It should also be using Java 11*
- if you are not using Java 11, and mvn is also not using Java 11, you may have trouble getting this project to work


##### Steps to install

1. Once you have the prerequisite libraries installed, unzip the provided craft skeleton into a location of your choosing.
1. Navigate into the `marketplace-backend-springboot` directory.
1. `mvn -N wrapper:wrapper`
1. `mvn clean install` 

Great job! Now you should be all set to run the project!

###### Running the project

In the project directory, you need only to run `./mvnw spring-boot:run -f "pom.xml"`. This will start a server at [http://localhost:8080](http://localhost:8080).
You can visit [http://localhost:8080/helloworld](http://localhost:8080/helloworld) to see the example service.

To stop the project, kill the process using Ctrl-C.

###### Using an IDE

Now that you have the project running from the command line, you can also import the project to the IDE of your choice to make working with it easier.
Some possibilities are:
1. [Spring Tool Suite](https://spring.io/tools)
1. [Eclipse](https://www.eclipse.org/downloads/)
1. [IntelliJ IDEA](https://www.jetbrains.com/idea/)
1. [Visual Studio](https://visualstudio.microsoft.com/)

##### API

Details about the API are available at: http://localhost:8080/swagger-ui/

##### About the project

The project was created using the [spring initializr](https://start.spring.io/).
Learn about [spring boot](https://spring.io/projects/spring-boot).

##### In Memory Database

The project comes with an H2 in-memory database configured in application.properties. The H2 console is at [http://localhost:8080/h2-console/](http://localhost:8080/h2-console/), and it can be connected to using `jdbc:h2:mem:marketplacedb` as the database url.

-----------------
#### FAQ

**Q**. I can't get the back end service to work

**A**. Check your java version and your maven version as described in the instructions.


**Q**. Help! I can't get this set up!

**A**. Please reach out to your recruiter ASAP and they will get you in touch with someone who can help. Please be specific about what you are having trouble with. 
