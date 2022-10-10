# Unique Email Addresses

## Tags

Difficulty Options: `easy`

Interview Type Options: `phonescreen` `onsite`

Level Options: `swe2` `sse`

Role Category Options: `backend` `frontend` `fullstack`

## Share with Candidate - Public

### Description

Every valid email consists of a local name and a domain name, separated by the `'@'` sign. Besides lowercase letters, the email may contain one or more `'.'` or `'+'`.

* For example, in `"alice@intuit.com"`, `"alice"` is the local name, and `"intuit.com"` is the domain name.

If you add periods `'.'` between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

* For example, `"alice.z@intuit.com"` and `"alicez@intuit.com"` forward to the same email address.

If you add a plus `'+'` in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

* For example, `"m.y+name@email.com"` will be forwarded to `"my@email.com"`.

It is possible to use both of these rules at the same time.


Given an array of strings `emails` where we send one email to each `email[i]`, return the number of different addresses that actually receive mails.

**Example 1:**

```
Input: emails = ["test.email+alex@intuit.com","test.e.mail+bob.cathy@intuit.com","testemail+david@int.uit.com"]
Output: 2
Explanation: "testemail@intuit.com" and "testemail@int.uit.com" actually receive mails.
```

**Example 2:**

```
Input: emails = ["a@intuit.com","b@intuit.com","c@intuit.com"]
Output: 3
```

### Preparation Instructions to be Shared in Advance

* You can use any programming language & online IDE of your choice

## Intuit Internal ONLY (Do not share with candidate)

Estimated time to complete: `15 minutes`

### Common Clarification Questions/FAQ

**Question 1:** Will the array be null?

**Answer:** Yes, the input array can be null or empty.


**Question 2:** Can a String within the array be null?

**Answer:** No every String within the array will be a non-null String.


**Question 3:** What if an email String does not contain a `"@"` character?

**Answer:** Assume that all given Strings have exactly one `"@"` character in them.


**Question 4:** Can the domain name contain the `"+"` character?

**Answer:** No, the domain name will not contain a `"+"` character.

### Solution

We need to clean the emails given to us. The most intuitive solution will be to iterate over the emails and clean them one by one.

Here, cleaning the email means removing unnecessary characters, per the rules given to us.

Once an email has been cleaned, it can be pushed into a set. The size of this set will then equal the count of unique emails.

**Rules to clean email:**

* If there are periods `'.'` in local name ignore them.
* If there is a plus `'+'` in local name skip all local name characters till '@'.
* There is only one `'@'` symbol and the substring after it is our domain name; we will keep the domain name as it is.

#### Possible Approaches

**Intuition:**

An elegant way of cleaning emails is to leverage built-in functions such as `split`, `replace` and `substring`.

**Algorithm:**

1. initialize a Set `set`
2. For each `email` in `emails`:
    * Split the `email` on `"@"` character into two parts `pre` and `post`
    * Replace all occurances of `"."` with an emoty String `""` in `pre`
    * If `pre` contains `"+"`, then set `pre` as a substring of `pre` from `0` to index of `"+"` in `pre`
    * concatinate `pre` and `post` and add the result to `set`
3. Return the size of `set`

#### Sample Solution

```js
/**
  A function that takes an array of Strings as input and returns a count of valid emails within them.
**/
public int numUniqueEmails(String[] emails) {
        Set<String> set = new HashSet<>();
        
        // Loop through each email.
        for(int i = 0; i < emails.length; ++i) {
            String[] mail = emails[i].split("@");
            String pre = mail[0];
            String post = mail[1];
            
            // filter out all '.' characters.
            if (pre.indexOf(".") != -1) {
                pre = pre.replace(".", "");
            }
            
            // Ignore anything after '+'
            if (pre.indexOf("+") != -1) {
                pre = pre.substring(0, pre.indexOf("+"));
            }
            
            // Add to set to ensure unique values.
            set.add(pre + "@" + post);
        }
   
        return set.size();
    }

```

#### Time Complexity
Let **N** be the number of the emails and **M** be the average length of an email.

Time Complexity will then be `O(N.M)`

* The split menthod goes through each String to create the substrings in `O(M)` time.
* The replace method also takes `O(M)` time.
* The substring method takes `O(M)` time as well.

Since we're repeating this for every `email`, that takes `O(N)` time, giving us a total of `O(M.N)`

### How to Assess Candidate / Expected Answer by Level

A strong SWE2 and SSE candidate should be able to finish this in 10 minutes without any hand holding.

Also, questions that we would like the candidate to ask are also useful.
Edge cases identified, etc.


### References
- [Count distinct emails in an array](https://www.geeksforgeeks.org/count-distinct-emails-present-in-a-given-array/)
