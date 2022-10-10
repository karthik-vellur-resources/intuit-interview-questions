# Small Business Relationships

## Tags

Level Options: `intern`, `swe1`, `swe2`

Role Category: `backend`

Difficulty Options: `medium`

Interview Type Options: `phonescreen` `onsite`

## Share with Candidate - Public

### Description

Quickbooks helps small businesses with day to day operations. Intuit wants you to use company data from Quickbooks to discover relationships between companies in their networks. 

**For example:**

CompanyA purchases dairy from CompanyB. CompanyB purchases pet feed from companyC.

> Company A (Grocery Store, address, etc) <--> Company B (Dairy Farm, address, etc) <--> Company C (Pet Feed Store, address, etc). 

`A <--> B <-->  C`


1. **Part 1:** 

How would you go about solving whether a company is connected to another? What data structures would you consider?

2. **Part 2:** OOP Design

Design some simple objects to work with that reflect small businesses and the direct relationships that they have with others. Please code these with the intention to use them. You can use the example above as a sample.

3. **Part 3:** Algorithms Question

Deliver a feature for users that checks how many degrees of separation exist between two different businesses. For example, Business A regularly buys goods from Business B which regularly buys from Business C. A is one degree separated from C! The code must return the shortest path if there are multiple. Run your code with the example above.
`A <--> B <--> C`
Degree of separation between A & C is 1.


### Preparation Instructions to be Shared in Advance

* You can use any programming language & IDE of your choice

## Intuit Internal ONLY Do Not Share with Candidate

Estimated time to complete: `45 minutes`

1. Part 1: ~ 10 minutes
2. Part 2: ~ 10 minutes
3. Part 3: ~ 25 minutes

### Common Clarification Questions/FAQ

1. Part 1:
    *  Company objects are to stay at a high level (only a few characteristics)
    *  A company can be related to multiple other companies. 1 to many relationship between companies.

2. Part 2:
    *  Only direct relationships are to be reflected in class objects
    *  Manually create 3 companies to start resembling the example in part 1

2. Part 3:
    *  Creating a static graph is acceptable.

### Solution

#### Approach
* Use a graph traversal algorithm (BFS) to determine if a company is related to another company.
* Keep a track of visited companies to avoid infinite loop of graph cycles


#### Sample Solution (works as is in glider)

```java
import java.util.*;

class Main {

   public static void main(String[] args) {

        /* Part 2 */
        Company cA = new Company("A");
        Company cB = new Company("B");
        Company cD = new Company("D");
        Company cC = new Company("C");

        /* Create uni-directional relationship */
        cA.addRelationship(cB);
        cC.addRelationship(cD);
        cB.addRelationship(cC);

        /* Part 3 solution */
        System.out.println(cA.getDegreeOfSeparation(cC));

    }

    /* Part 1 solution */
    static class Company {
        private String companyType;
        private String companyAddress;
        private String companyName;

        /* You can use a map too which would provide constant look up time. Discuss Pros & cons of using Map vs List */
        List<Company> relations;

        public Company(String companyName) {
            this.companyName = companyName;
            this.relations = new ArrayList<>();
        }

        public void addRelationship(Company company) {
            this.relations.add(company);
        }

        public String getCompanyName() {
            return companyName;
        }

        public List<Company> getRelations() {
            return this.relations;
        }

        /* Part 3 solution */
        public int getDegreeOfSeparation(Company company) {

            int deg = 0;
            Queue<Company> companyQueue = new LinkedList<>();
            HashSet<String> visitedCompanies = new HashSet<>();

            companyQueue.addAll(this.getRelations());

            while(!companyQueue.isEmpty()) {
                int size = companyQueue.size(); // Record the size before we add more
                for(int counter=0; counter < size; counter++) {
                    Company thisCompany = companyQueue.remove();
                    if(thisCompany.getCompanyName().equals(company.getCompanyName())) {
                        return deg;
                    }
                    if(visitedCompanies.contains(thisCompany.getCompanyName())) {
                        continue;
                    }
                    visitedCompanies.add(thisCompany.getCompanyName());
                    companyQueue.addAll(thisCompany.getRelations());
                }
                deg++;
            }

            return -1; // Relation not found

        }

        @Override
        public String toString() {
            return "Company{" +
                    "companyName='" + companyName + '\'' +
                    '}';
        }
    }

}
```

#### Time Complexity
* Time Complexity: **O(C+R)**.`The above algorithm is simply BFS with an extra set to keept track of visited companies. So time complexity is the same as BFS.`
* Auxiliary space: **O(C)**. `The extra space is needed for the stack.`

`C -> companies,
R -> Relations`

### How to Assess Candidate / Expected Answer by Level

1. **INTERN**
```
●   Candidate asks questions to get clarification on requirements
●   Candidate is able to compare data structures and justify the best fit
●	Candidate is able to adjust design when given new constraints
●	Effectively tackles the Part 3 question and has solid ideas to solve the layering questions
```
2. **SWE1 and above**
```
●   Candidate asks questions to get clarification on requirements
●   Candidate is able to compare data structures and justify the best fit
●	Candidate is able to adjust design when given new constraints
●	Creates necessary objects to fit their design (most likely just Company class with two way relationships between them, potential abstract classes to define industries or additional classes to organize that).
●	Demonstrates understanding of the correct relationships between the different objects
●	Effectively handles the part 3 question
    ○	Candidate understands that DFS is not optimized to find shortest paths.
```

### Layering Questions

*  Add another node (companyD) to your current graph and explain your algorithms results (A -> D)
*  Introduce another cycle and explain your algorithms results (A -> D)
*  Discuss why DFS is not a reasonable option?
*  ** BONUS ** Return the path and the degrees of separation.