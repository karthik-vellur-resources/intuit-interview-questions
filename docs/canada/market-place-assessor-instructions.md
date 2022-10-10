# Market Place Craft Demo

## Assessor Information

### Project Description
This craft is based on the full stack MarketPlace craft in this repo.

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
#### Instructions for Assessors

It will be helpful to set up the project yourself, at least once, prior to conducting an assessment. This is so you are familiar with the project and can help the candidate if/when they become stuck.

The projects are:

https://github.intuit.com/poolhiring/marketplace-frontend-react

https://github.intuit.com/poolhiring/marketplace-backend-springboot

#### Question Pool

#### Start of Interview

1. Ensure candidate was able to get the craft demo running and has a general understanding

#### SWE1/SWE2 Level Frontend or Backend

1. Sort jobs by posting date
1. Sort by most active/least active (number of bids)
1. One of the jobs has $undefined for current bid. Why is that? Can you fix it?

#### Senior/Staff Level, Frontend

1. Create a form to post a bid and save it in the back end.
3. Create a form to post a job and save it in back end.
5. Allow a job poster to designate a maximum allowable bid as part of the posting.

#### Senior/Staff Level, Backend

1. Implement a way to close jobs past expiry with >0 bids
1. Design and implement a way to have bids expire after a certain period of time