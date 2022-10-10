# Self-Employed application Web App

## Tags

Level Options: `swe2`, `senior`

Role Category: `frontEnd`

Difficulty Options: `medium`

Interview Type Options: `craft-demo`, `onsite`

## Share with Candidate - Public

### Product Requirements

You are building a responsive web application that helps self helps self-employed individuals to track their income and expenses in order to give them better insights of their monetary situation, so they can focus on what they love doing without worrying about their finances!

In order to do so, you need to create a dashboard which contains a set of widgets:

1. A widget (Summary Widget) to track a summary of the customer’s financial status.
	- It should read the data from the list of transactions from the customer’s bank account.
	- Where each transaction contains the transaction date; a description; a unique reference number; and a monetary amount which could be positive (cash in) or negative (cash out)
	- This widget should show the total monetary amount in the bank account looking at the transaction data. 
		- If the total is greater than a configured positive threshold, the number should be shown in green
		- If the total is lower than the same configured threshold from before (but the total is still positive) the number should be shown in yellow
		- If the total is lower than 0.00, the number should be shown in red	
		
2. One widget (Invoices Widget) to manage the list of invoices the user has for his/her customers, which supports both editing existing invoices as well as creating new ones.
	- Each invoice contains the following:
	    - name of the client
        - the creation date
        - a unique reference number
        - a monetary amount, which could be positive (money to be received) or negative (a refund to the customer)
        - a status (PAID or NOT PAID).
    - Every field should be modifiable, except the invoice status which is read only and it is worked out in the following way:
        - An invoice is considered PAID if there is a bank transaction for the same amount, with the bank transaction’s reference number being equal to the invoice’s reference number, and with the bank transaction date being later than the invoice creation date. 
        - An invoice is considered NOT PAID if the previous criteria is not matched. 
        - Users should be able to create a new invoice.

3. Other Requirements:
   - Summary widget should also show the number of invoices created in the last 30 days.
   - Changes in one widget should automatically update other widgets. 
        - I.e. the creation of an invoice should affect the summary widget, as this shows the number of invoices created in the month.


#### Additional instructions
  * Feel free to mock backend service responses and use any library/framework of your choice.
  * Add pseudocode or an actual example of a unit test.

## Intuit Internal ONLY [Do Not Share with Candidate]

#### 30 Minute Target

Have the candidate build the Summary Widget with the product requirement #1 by getting the transactions from mock response.

#### 60 Minute Target

Have the candidate build all of the specified product requirements taking into consideration all of the 30 minute targets (#1 - #3 of the product requirements).

#### Evaluating Level

##### SWE2 / Senior

Candidate is able to discuss a clear point of view and approach for the following:

* Described the solution for user on the UI component separation.
* Described the state for storing the transactions, Invoices and its details.
* Discussed data retention/filter strategy.
* Discussed testability and types of testing (unit, integration, and performance).
* Discussed how the list is shown - UI page performance, lazy loading / pagination.
* Considered accessibility requirements as part of the design.
* Has a plan for server latency when populating the widgets (eg. loading screen / spinner and appropriate timeouts).

Candidate has coded/shown:

* UI design with proper user interfaces
* Responsive UI.
* Separation of Concerns in React (container components, presentational components, etc.).
* Asynchronous data retrieval for transactions, Invoices and filter data.
* Has fallback UI rendered if a widget fails to load (e.g. due to an uncaught exception, network error etc.).
* Has Error UI rendered if the fetch result for transactions is empty
