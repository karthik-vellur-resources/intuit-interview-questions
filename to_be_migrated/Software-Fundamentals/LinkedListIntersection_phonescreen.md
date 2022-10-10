# Linked List Intersection
### Write a function to get the intersection point of two Linked Lists



Estimated time to complete:20 minutes

Tags: medium phonescreen onsite sse swe2 frontend backend

## Description
Write a function to get the intersection point of two Linked Lists


```js
Input:
        1st linked list:  3->6->9->15->30
        2nd linked list:  10->15->30

Output: 15 is the intersection point
```

### Approach:

Using difference of node counts

Get count of the nodes in the first list, let count be c1.
Get count of the nodes in the second list, let count be c2.
Get the difference of counts d = abs(c1 – c2)
Now traverse the bigger list from the first node till d nodes so that from here onwards both the lists have equal no of nodes.
Then we can traverse both the lists in parallel till we come across a common node. (Note that getting a common node is done by comparing the address of the nodes)


### Sample Solution:

```js
// Java program to get intersection point of two linked list

class LinkedList {

    static Node head1, head2;

    static class Node {

        int data;
        Node next;

        Node(int d)
        {
            data = d;
            next = null;
        }
    }

    /*function to get the intersection point of two linked
    lists head1 and head2 */
    int getNode()
    {
        int c1 = getCount(head1);
        int c2 = getCount(head2);
        int d;

        if (c1 > c2) {
            d = c1 - c2;
            return _getIntesectionNode(d, head1, head2);
        }
        else {
            d = c2 - c1;
            return _getIntesectionNode(d, head2, head1);
        }
    }

    /* function to get the intersection point of two linked
     lists head1 and head2 where head1 has d more nodes than
     head2 */
    int _getIntesectionNode(int d, Node node1, Node node2)
    {
        int i;
        Node current1 = node1;
        Node current2 = node2;
        for (i = 0; i < d; i++) {
            if (current1 == null) {
                return -1;
            }
            current1 = current1.next;
        }
        while (current1 != null && current2 != null) {
            if (current1 == current2) {
                return current1.data;
            }
            current1 = current1.next;
            current2 = current2.next;
        }

        return -1;
    }

    /*Takes head pointer of the linked list and
    returns the count of nodes in the list */
    int getCount(Node node)
    {
        Node current = node;
        int count = 0;

        while (current != null) {
            count++;
            current = current.next;
        }

        return count;
    }

    public static void main(String[] args)
    {
        LinkedList list = new LinkedList();
        Node nodeA =  new Node(3);
        Node nodeB =  new Node(6);
        Node nodeC =  new Node(15);
        Node nodeD =  new Node(15);
        Node nodeE =  new Node(30);

        // creating first linked list
        list.head1 = nodeA;
        list.head1.next = nodeB;
        list.head1.next.next = nodeC;
        list.head1.next.next.next = nodeD;
        list.head1.next.next.next.next = nodeE;

        // creating second linked list
        list.head2 = new Node(10);
        list.head2.next = nodeD;

        System.out.println("The node of intersection is " + list.getNode());
    }
}
```
```py
class Node():
    def __init__(self, data, nxt):
        self.nxt = nxt
        self.data = data

    def next(self):
        return self.nxt


def get_count(head_a):
    count = 0
    node = head_a
    while node != None:
        node = node.next()
        count += 1

    return count


def move_head_n(head, n):
    node = head
    for _ in range(n):
        node = node.next()
    return node


def get_intersection(head_a, head_b):
    count_a = get_count(head_a)
    count_b = get_count(head_b)
    diff_count = abs(count_b - count_a)

    if count_b > count_a:
        head_b = move_head_n(head_b, diff_count)
    elif count_a > count_b:
        head_a = move_head_n(head_a, diff_count)

    node_a = head_a
    node_b = head_b

    while node_a and node_b:
        if node_a == node_b:
            return node_a.data
        node_a = node_a.next()
        node_b = node_b.next()

    return None


e = Node(30, None)
d = Node(15, e)
c = Node(9, d)
b = Node(6, c)
a = Node(3, b)

f = Node(10, d)

print(get_intersection(a, f))
```

### Time Complexity:
Time Complexity: O(m+n)
Auxiliary Space: O(1)

### Alternate Approach:

Method 1(Simply use two loops)
Use 2 nested for loops. The outer loop will be for each node of the 1st list and inner loop will be for 2nd list. In the inner loop, check if any of nodes of the 2nd list is same as the current node of the first linked list. The time complexity of this method will be O(M * N) where m and n are the numbers of nodes in two lists.

Method 2 (Mark Visited Nodes)
This solution requires modifications to basic linked list data structure. Have a visited flag with each node. Traverse the first linked list and keep marking visited nodes. Now traverse the second linked list, If you see a visited node again then there is an intersection point, return the intersecting node. This solution works in O(m+n) but requires additional information with each node. A variation of this solution that doesn’t require modification to the basic data structure can be implemented using a hash. Traverse the first linked list and store the addresses of visited nodes in a hash. Now traverse the second linked list and if you see an address that already exists in the hash then return the intersecting node.

Method 3 (Use Hashing)
Basically, we need to find a common node of two linked lists. So we hash all nodes of the first list and then check the second list.
1) Create an empty hash set.
2) Traverse the first linked list and insert all nodes’ addresses in the hash set.
3) Traverse the second list. For every node check if it is present in the hash set. If we find a node in the hash set, return the node.

Method 4(Make circle in first list)
1. Traverse the first linked list(count the elements) and make a circular linked list. (Remember the last node so that we can break the circle later on).
2. Now view the problem as finding the loop in the second linked list. So the problem is solved.
3. Since we already know the length of the loop(size of the first linked list) we can traverse those many numbers of nodes in the second list, and then start another pointer from the beginning of the second list. we have to traverse until they are equal, and that is the required intersection point.
4. remove the circle from the linked list.


### Variation/Similar problems

Union and Intersection of two Linked Lists
Intersection of two Sorted Linked Lists
Union and Intersection of two linked lists | Set-3 (Hashing)
Union and Intersection of two linked lists | Set-2 (Using Merge Sort)
Identical Linked Lists
First common element in two linked lists

### Solving Time
20 to 30 mins

### Reference:
https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/


