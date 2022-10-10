# QuickBooks Customer Retention Assignment

## Tags

Difficulty Options: `easy` `medium` `hard` 

Interview Type Options: `craft-demo`  

Level Options: `swe2` `sse` `staff` `pe` 

Role Category Options: `data` 

## Share with Candidate - Public

### Description

#### Background
Quickbooks Online (QBO) is a web-based service that provides financial management and tax preparation services for US and global small business owners. Quickbooks’ primary service allows users to track bank, credit card, investment, and loan balances and transactions through a single user interface, as well as manage billings, payments, payroll, reports, and taxes. 

#### The Problem
If QuickBooks were able to predict customer retention, efficient advertising and product customization would be a breeze. You are given a dataset containing information about usage of Quickbooks Online (QBO) between January and March 2020, inclusive. Each row represents a user’s login to QBO (the event). Each event has been joined to a summary of the user’s activity the same day. Each of these users had their first login to the product in Jan 2020. Can you build a model to predict 30 day user retention, given this table that contains login data and the product usage profile.

#### Guidelines
The end goal is to build a model that predicts user retention given login information and product usage data. 

You have one hour and a half to explore the data and build a simple prediction model, or at least present a roadmap for developing a model at a later stage. You can use external resources (e.g. public libraries and packages, Google and StackOverflow) but not help from other people.

After that, we would like you to present your code and discuss it with you. We are much more interested in learning about your thinking process, how you make decisions, and why. The performance of the model is of lesser importance.

The data table is provided in CSV format. It may be accessed in Pandas by:
`pandas.read_csv("craft_demo_dataset_new_users.csv.gz")`


A data dictionary is provided below. 

##### Event Information
- `event_id (int)` - A unique identifier of the database row 
- `timestamp (datetime)` - The time when the user login event occurred
- `accountloginfirstseen` (string) - The date when the account was created
- `userid (string)` - A unique identifier of the user who is logging into the product

##### User Profile Information
- `activity_summary_date  (datetime)` - the date of that summary row
- `subscription_type_name (string)` - the type of subscription that the user has. It can have the following values: Not Subscribed, null(!), Not Applicable, Not Defined, Buy Now, Retail, Trial, Wholesale
- `plan_frequency_name (string)` - when the plan is paid. Possible values are: monthly, annually
- `qbo_region_name (string)` - country of the QBO business (Add distinct values)
- `naics_industry_type (float)` - a 2 digit code indicating the industry of the business. Based on the North American Industry Classification System.
- `qboa_attach_ind (boolean)` - Whether QuickBooks Online Accountant (QBOA) has been attached to this account. If attached, it means that an accountant is maintaining the books for this QuickBooks company
- `payroll_attach_ind (boolean)` - Whether Payroll as an add-on service has been attached on this QuickBooks account
- `payments_attach_ind (boolean)` - Whether Payments as an add-on service has been attached on this QuickBooks account
- `seconds_spent_on_site_nbr (int)` - Number of seconds spent on QuickBook by the user that day
- `add_invoice_cnt (int)` - Number of invoices added that day by a QuickBooks user that day
- `money_in_txn_cnt (int)` - Number of money-in transactions for a QuickBooks company that day
- `money_out_txn_cnt (int)` - Number of money-out transactions for a QuickBooks company that day
- `import_customer_data_cnt (int)` - Number of times a QuickBooks user imported customer data that day
- `add_rcv_payment_cnt (int)` -  Number of payments received by the QuickBooks company on that day
- `add_customer_cnt (int)` - Number of customers added that day by a QuickBooks user
- `connect_to_bank_cnt (int)` - Number of banks that have been connected that day by a QuickBooks user
- `add_payment_method_cnt (int)` - Number of payment methods added that day by a QuickBooks user

### Links to Extra Files or References

The dataset for this assignment will be provided in Glider.

## Intuit Internal ONLY (Do not share with candidate)

Estimated time to complete: `90 minutes`

### Solution

- [Sample Solution 1](https://github.intuit.com/gist/cdepeuter/58b9fc52fbfbe336a1924197d7d574eb)

#### Possible Approaches

There are two ways to look at this craft demo problem. The first is heavy on data exploration and understanding, the second is modeling. It is unlikely that any candidate will be able to complete both routes in the same session. Either route or a combination of the two are acceptable as a solution.
For both routes, we should evaluate:
1. Code quality (to the extent that is possible in 90 min of work) and thought process.
2. Ability to prioritize work, given what they already know (“if you had one more hour and only one more hour to work on this problem, what would you do?”)

For those candidates who went the data exploration route, we want to evaluate:
1. What types of data exploration did they do?
	- Were the graphs, tables, or statistics that were generated informative?
2. How would their exploration inform a modeling approach? (Something beyond “I generated 1000 graphs”)
3. Did they note any discrepancies or abnormalities in the data? Do they understand what effects they would have on the modeling approach? Do they have any approaches to mitigate the issues they identified?

For those candidates who went the modeling route:
1. What assumptions or interpretations did they make in label generation?
2. … in feature engineering?
3. Can they justify those assumptions?
4. What modeling approaches (algorithms) did they use and why?
5. How did (or would) they evaluate the model?
6. Did they sanity-check the results of the model?


#### Sample Solution

### How to Assess Candidate / Expected Answer by Level

#### Data Scientist
##### Topics to Potentially Explore
- Overall understanding of the problem
- Discuss descriptive statistics around data shape and quality
- Ability to describe how they would define the target label
- Ability to explain the MDLC process
- Ability to define target KPIs
- Discuss sampling approaches
##### Potential Target Outcome
###### Conventional Approach
- Well defined logic to create a target label
- Well defined approach to sample and split the data for training
- Clear understanding of the overall problem
###### Analytical approach
- Candidate shows a clear logic / thought process in how he progressed through the analysis
- Candidate shows clear and actionable insights from his analysis
- Clear understanding of the overall problem

#### Senior Data Scientist
##### Topics to Potentially Explore
- All of the items from Data Scientist 
- Discuss different approaches to feature engineering
- Discuss pros and cons to some of the approaches
- Ability to substantiate technical decisions
- Ability to discuss at least one approach that could lead to a successful solution of the problem
##### Potential Target Outcome
- Have a well defined and thought out data set for training with a valid approach for feature engineering
- Potentially, look for early training results

#### Staff Data Scientist
##### Topics to Potentially Explore
- All of the items from Senior Data Scientist
- Discuss in depth problem understanding to build expectations around good vs. bad outcomes of the development process
- Ability to discuss modeling methodologies and choices
- Discuss different approaches along with pros and cons
- Discuss modeling results which approach is recommended and why

##### Potential Target Outcome
- Deep understanding of the problem as well as sanity checks
- At least one model trained or a clear path/approach
- Solid substantiation of any technical decision


#### Principal Data Scientist
##### Topics to Potentially Explore
- All of the items from Staff Data Scientist
- Next steps beyond solving the problem
- Decision making around prioritization / business constraints
- Decision making and understanding around solution deployment in production
##### Potential Target Outcome
- Ability to discuss more than one approach to the problem with reasoning
- Ability to discuss potential challenges beyond the problem statement
- Solid substantiation of any technical decision

### References

- [QuickBooks Retention Assignment Dataset](https://drive.google.com/file/d/1Kkszjh7go3GL1SLrwS5kMWZcnnZxpprn/view?usp=sharing)
