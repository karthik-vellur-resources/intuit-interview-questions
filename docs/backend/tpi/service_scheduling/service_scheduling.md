# Service Scheduling

## Tags

Level Options: `intern`, `swe1`, `swe2`

Role Category: `backend`

Difficulty Options: `easy`

Interview Type Options: `phonescreen` `onsite`

## Share with Candidate - Public

### Description

Design and implement a service scheduler for an in-person customer service center (Very similar to genius bar at the Apple centers or Xfinity store service).

1. Customer walks into the store and checks in. They are given a ticket with a sequential service number.
2. The service number is called by the staff in the order determined by the scheduler.
3. There are 2 different tiers of customers: 
    
    1) Regular customers are serviced in the order they arrive.

    2) VIP customers.
    `VIP customers are given higher priorities compared to Regular customers. `

#### Part 1

Design class for customer and ServiceScheduler with required high-level characteristics.

#### Part 2

Implement the ServiceScheduler to serve ALL VIP customers before serving regular customers.
Implement two methods `checkIn(Customer)` and `getNextCustomer()`

#### Part 3

Implement the scheduler to make sure 2:1 VIP vs. Regular customer processing rate.
Modify `getNextCustomer()` method to implement the customer processing rate.


### Preparation Instructions to be Shared in Advance

* You can use any programming language & IDE of your choice

## Intuit Internal ONLY Do Not Share with Candidate

Estimated time to complete: `45 minutes`

1. Part 1: ~ 5-10 minutes
2. Part 2: ~ 10-15 minutes
3. Part 3: ~ 10-15 minutes

### Common Clarification Questions/FAQ

1. Part 1:
    *  Scheduler only need to handle in person scheduling. There is no other type of scheduling, such as online scheduling, phone calls, etc.
    *  All customers have their information records in the system.
    *  To schedule, we need customer’s name and phone number.
    *  For simplicity, all service requests go through the same scheduling/service process.
    *  Strategy for setting VIP priorities will vary in the following sections below, for this section we tell the candidate no need to worry about it.

2. Part 2:
    *  Serving a customer is an atomic operation, i.e., we do not stop serving a regular customer in the middle of the service when a VIP customer walks in.

### Solution

#### Approach
* Use two queues to track regular customers and VIP customers.
* Use a counter to track customer processing rate.

#### Sample Solution (works as is in glider)

```java
import java.util.*;

class ServiceScheduler {
    /* Discuss Pros of using enum */
    enum CustomerType
    {
        REGULAR, VIP
    }

    LinkedList<Customer> regularQ;
    LinkedList<Customer> vipQ;
    int vipCount;
    private static final int WAIT_TIME=5;
    private static final int VIP_RATE=2;

    public ServiceScheduler() {
        this.regularQ = new LinkedList<>();
        this.vipQ = new LinkedList<>();
        vipCount = 0;
    }

    public void checkIn(Customer customer) {

        /* Discuss why to use Switch case */
        switch(customer.getCustomerType()) {
            case REGULAR:
                regularQ.add(customer);
                System.out.println("Added customer to regular Q.");
                System.out.println(customer.toString());
                int wait = (regularQ.size() + vipQ.size()) * WAIT_TIME;
                System.out.println("Wait time: " + wait);
                break;
            case VIP:
                vipQ.add(customer);
                System.out.println("Added customer to VIP Q.");
                System.out.println(customer.toString());
                int waitTime = vipQ.size() * WAIT_TIME;
                System.out.println("Wait time: " + waitTime);
                break;
            default:

        }
    }

    /* Part 2 */
    public Customer getNextCustomer() {

        if(!vipQ.isEmpty()) {
            Customer c = vipQ.remove();
            return c;
        } else {
            return regularQ.remove();
        }
    }

    /* Part 3 */
    public Customer getNextCustomerWithRate() {

        if(!vipQ.isEmpty() && vipCount < VIP_RATE) {
            Customer c = vipQ.remove();
            vipCount+=1;
            return c;
        } else {
            vipCount = 0;
            return regularQ.remove();
        }
    }

    public static class Customer {
        private String firstName;
        private String lastName;
        private String contact;
        private CustomerType customerType;

        public Customer(String firstName, String contact, CustomerType customerType) {
            this.firstName = firstName;
            this.contact = contact;
            this.customerType = customerType;
        }

        public String getFirstName() {
            return firstName;
        }

        public String getLastName() {
            return lastName;
        }

        public CustomerType getCustomerType() {
            return customerType;
        }

        @Override
        public String toString() {
            return "Customer{" +
                    "firstName='" + firstName + '\'' +
                    '}';
        }
    }

    public static void main(String[] args) {

        Customer a = new Customer("a","1234", CustomerType.REGULAR);
        Customer c = new Customer("c","5678", CustomerType.VIP);
        Customer d = new Customer("d","1123", CustomerType.VIP);
        Customer e = new Customer("e","91283", CustomerType.VIP);
        Customer b = new Customer("b","8272", CustomerType.REGULAR);


        ServiceScheduler scheduler = new ServiceScheduler();

        System.out.println("----------- PART 1 ------------- ");
        scheduler.checkIn(a);
        scheduler.checkIn(c);
        scheduler.checkIn(d);
        scheduler.checkIn(b); // What would be the wait time for customer B check in?? Ans: 20 minutes
        scheduler.checkIn(e);

        System.out.println("----------- PART 2 ------------- ");
        // System.out.println(scheduler.getNextCustomer().toString());
        // System.out.println(scheduler.getNextCustomer().toString());
        // System.out.println(scheduler.getNextCustomer().toString());
        // System.out.println(scheduler.getNextCustomer().toString());
        // System.out.println(scheduler.getNextCustomer().toString());

        System.out.println("----------- PART 3 ------------- ");
        System.out.println(scheduler.getNextCustomerWithRate().toString());
        System.out.println(scheduler.getNextCustomerWithRate().toString());
        System.out.println(scheduler.getNextCustomerWithRate().toString());
        System.out.println(scheduler.getNextCustomerWithRate().toString());
        System.out.println(scheduler.getNextCustomerWithRate().toString());

    }
}
```

### Output
```
----------- PART 1 ------------- 

Added customer to regular Q.
Customer{firstName='a'}
Wait time: 5
Added customer to VIP Q.
Customer{firstName='c'}
Wait time: 5
Added customer to VIP Q.
Customer{firstName='d'}
Wait time: 10
Added customer to regular Q.
Customer{firstName='b'}
Wait time: 20
Added customer to VIP Q.
Customer{firstName='e'}
Wait time: 15

----------- PART 3 ------------- 

Customer{firstName='c'}
Customer{firstName='d'}
Customer{firstName='a'}
Customer{firstName='e'}
Customer{firstName='b'}
```

### Time Complexity:
* Time Complexity: **O(N)**.`Where N are all the customers who check in`
* Auxiliary space: **O(N)**. `The extra space is needed for the two queues.`

### How to Assess Candidate / Expected Answer by Level

1. **INTERN**
```
●   Candidate asks questions to ensure understanding of the problem statement.
●   Candidate should have customer and ticket classes modeled.
●	Candidate identifies that 2 queues or lists to distinguish between the two tiers of customers and populates this as soon as customers checks in.
●	Candidate creates clear logic to process the queue in the required priority.
●   Add customer to the queue, and remove customers from the queues based on the
requirements
```
2. **SWE1 and above**
```
●   Candidate asks questions to ensure understanding of the problem statement.
●   Candidate should have customer and ticket classes modeled.
●	Candidate identifies that 2 queues or lists to distinguish between the two tiers of customers and populates this as soon as customers checks in.
●   Check VIP queue for emptiness before calling next customer to service.
●   Add customer to the queue, and remove customers from the queues based on the counter.
●   Candidate adds the shortest wait time which will be the current status of the two queues when the ticket was generated.
requirements

```

### Variation/Similar problems

## Layering Questions

*  How can we calculate and display wait time for a Regular customer and for a VIP customer? **HINT:** Multiply a constant value of processing time by the size of the queue.