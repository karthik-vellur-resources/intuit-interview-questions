# Worldwide countries information Web App

## Tags

Level Options: `swe2`, `senior`

Role Category: `frontEnd`

Difficulty Options: `medium`

Interview Type Options: `craft-demo`, `onsite`

## Share with Candidate - Public

### Product Requirements

You are building a responsive web application that helps users to see the list of countries and few details about the country.

1. A widget to display the country list
	- Each country should have
		- Its name
		- Its flag (display the icon in smaller size)
		- Population
		- Region
		- Capital
		- "View More" button to display the additional details of the country

2. A widget to display the additional details of the country as below
	- Its flag (should display larger image while viewing the details)
	- Population
	- Region
	- Capital
	- Native Name
	- Currencies used
	- Languages
	- Border countries

3. A widget to provide a search option to filter the countries list
	- Filter by countryName
	- If time permits, extend the search based on the region, language and currency

#### Additional instructions
  * Add pseudocode or an actual example of a unit test.
  * Feel free to extend the product requirements as you see fit.

#####  Api Details :
	List all countries 
		https://restcountries.com/v3.1/all

	Search by
		CountryName - https://restcountries.com/v3.1/name/{name}
		Region - https://restcountries.com/v3.1/region/{region}
		Language - https://restcountries.com/v3.1/lang/{lang}
		Currency - https://restcountries.com/v3.1/currency/{currency}
		
	Filter the response with required fields
		https://restcountries.com/v3/{service}?fields={field},{field},{field}
		eg. https://restcountries.com/v3/all?fields=name,capital,currencies

## Intuit Internal ONLY [Do Not Share with Candidate]

#### 30 Minute Target

Have the candidate build the countryList application with the product requirement #1 by getting the countryList from the APIs provided

#### 60 Minute Target

Have the candidate build all of the specified product requirements taking into consideration all of the 30 minute targets (#1 - #3 of the product requirements).

#### Evaluating Level

##### SWE2 / Senior

Candidate is able to discuss a clear point of view and approach for the following:

* Described the solution for user on the UI component separation.
* Described the state for storing the countryList and its details.
* Discussed data retention/filter strategy.
* Discussed testability and types of testing (unit, integration, and performance).
* Discussed how the list is shown - UI page performance, lazy loading / pagination.
* Considered accessibility requirements as part of the design.
* Has a plan for server latency when populating the widgets (eg. loading screen / spinner and appropriate timeouts).

Candidate has coded/shown:

* UI design with proper user interfaces
* Responsive UI.
* Separation of Concerns in React (container components, presentational components, etc.).
* Asynchronous data retrieval for countryList and filter country data.
* Has fallback UI rendered if a widget fails to load (e.g. due to an uncaught exception, network error etc.).
* Has Error UI rendered if the search result is empty

## Reference

* [Rest Countries API](https://restcountries.com/)
