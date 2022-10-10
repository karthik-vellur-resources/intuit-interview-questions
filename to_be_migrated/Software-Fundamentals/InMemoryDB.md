# Suited For
Software Engineer 2 and Senior Software Engineer

## Difficulty Level
Medium-Hard

### Given Problem statement:

#### Part - 1 

Support for the following operations:
1. READ: Operation get a value given a key and should throw an exception if no such key exists
2. INSERT: Operation adds a value given a key or updates the the value if key already exists Ex: 
            1. INSERT a=1; 
            2. READ a; //returns 1
            3. INSERT a=1;
            4. INSERT b=3;
            5. INSERT a=2;
            6. READ a; // returns 2
3. DELETE: Operations removes the value associated with the key being deleted.

#### Part - 2

Support for transactions around the operations implemented previously : INSERT, READ, DELETE.

1. Transactions will start with the keyword: START_TXN
2. Transactions will end with the keyword: COMMIT_TXN
3. Transactions will be rolled back utilizing the keyword: ROLLBACK_TXN
4. Any modify operations will only be visible to the scope of the transaction until COMMIT_TXN is invoked.
5. Once COMMIT_TXN is invoked, the result of all operations that took place within the transaction block is visible to everyone.
6. ROLLBACK_TXN will rollback all operations to the start of transaction namely START_TXN

Ex: Commit a transaction

INSERT a=1;
INSERT b=1;

START_TXN;

READ a; // Should return 1
READ b; // Should return 1

INSERT c=3;
INSERT b=2;

COMMIT_TXN;

READ a; // Should return 1
READ b; // Should return 2
READ c; // Should return 3

Ex: Rollback a transaction

INSERT a=1;
INSERT b=1;

START_TXN;

READ a; // Should return 1
READ b; // Should return 1

INSERT c=3;
INSERT b=2;

ROLLBACK_TXN;

READ a; // Should return 1
READ b; // Should return 1
READ c; // throw exception as key cannot be found
