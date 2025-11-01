//Find the sum and average of a list

list = {}   //Get a list
n = list.length
if n == 0  // Outlier check, if 0
    RETURN error
int total = {}
for i in list;  //For all numbers in the list
    total = total + i; //Finding the sum is simply iterating the list 
average = total / list.length   //divide total by the number of items in the list


//Find the Factorial

n = INPUT;
IF n < 0 THEN;      // Prevents negative numbers
    Error;
result = 1; // We want the default here to be 1, not 0, to prevent division by 0
FOR i = 1 to n;     // Iterate over from 1 to n, the input
    result = result * i;    //Multiply the first number by 1, then that number by 2,
                            //Continuing until reaching the designated number, n.


// Check if number is Prime

if n < 2 THEN;  //If number is prime, it will not be less than 2
    NOT PRIME;
If n == 2;      //If it is 2, it is prime
    PRIME;
if n % 2 == 0   //If it is divisble by 2, not prime
    NOT PRIME;
FOR i = 3 TO SQRT n STEP 2;     //Skips all odd numbers
    IF n % i == 0 THEN ;        //Divide the selected number by each number,
        NOT PRIME;              //If remainder is 0, not prime
else
    PRIME;          //If All checks fail, then is Prime

// Sort a List (Bubble Sort)

list = {}           //Get a List
n = list.length     //Store how many items are in the list
for i = 0 TO n - 2;          //Loop 1 checks how many times we go through the list
    for j = 0 TO n - i - 2  //Loop 2 compares each number and the number next to it
        IF list[j] > list[j + 1] THEN   //Check if later value is greater than sooner value
            temp = list[j]       //Store later value in temp
            list[j] = list[j + 1]   //Swap laters position with the next value
            list [j+1] = temp

//Reverse a List

list = {}       //Get a list
n = list.length     //Get the length of the list
    for i = 0 to (n / 2) - 1;   //Loop only halfway through the list
    temp = list[i];     //Store the first item to temp
    list[i] = list[n - i -1]    //Set the first item to the last item
    list [n- i - 1] = temp;     // Set the last item to the value of temp

//Linear Search

list = {}       //Get a list
target = x;     //Get target
n = list.length

for i = 0 to n;     //Check everything from 0 to n
    IF list[i] == target THEN;
        CONFIRM

//Binary Search
//Must be sorted

list = {}               // Get a sorted list
target = x              // The number we are looking for
low = 0                 // Pointer at the start of the list
high = list.length - 1  // Pointer at the end of the list

while low <= high;   // Loop: keep checking while start <= end
    mid = (low + high) / 2  // Find the middle position between the two pointers

    IF list[mid] == target THEN;    // Check if the middle number matches target
        BREAK                       // Exit if found

    ELSE IF list[mid] < target THEN;    // If middle number is smaller
        low = mid + 1                   // Move the start pointer up (ignore left side)

    ELSE                                // If middle number is larger
        high = mid - 1                  // Move the end pointer down (ignore right side)

// Hash Search

hashTable = {}             // Get table
key = x                    // get target
index = hash(key)          // Hash function: converts key into an index number
bucket = hashTable[index]  // Use the index to locate the correct bucket or slot

IF bucket == EMPTY THEN;              // If no data at that position
    ERROR
ELSE                                  // If data exists there
    FOR each item in bucket;          // Loop: go through all items stored in this bucket
        IF item.key == key THEN;      // Check if any item matches our key
            BREAK                     // Stop searching once found
    PRINT "Not Found"                 // If loop finishes with no match


//Count characters in a string
START countCharacter()

str = "Implementation Consultant"   // The string to search
target = 't'                         // The character we are counting
count = 0                            // Counter variable starts at 0

for i = 0 TO str.length - 1;         // Loop through every character in the string
    IF str[i] == target THEN;        // Check if current character matches target
        count = count + 1            // Add 1 to count each match

//Count words in a sentence

sentence = "FAST builds enterprise software."
count = 0
    for i = 0; i < sentence.length; ++i
        if sentence[i] == ' '           // Detect space between words
            count++

// Fibonacci (Iterative)

// Get n (which Fibonacci number to compute)
n = INPUT
IF n < 0 THEN;                  // Reject negatives
    PRINT "Error"
    STOP
IF n == 0 THEN;                 // Base case 0 → 0
    PRINT 0
    STOP
IF n == 1 THEN;                 // Base case 1 → 1
    PRINT 1
    STOP

a = 0                           // F(0)
b = 1                           // F(1)

FOR i = 2 TO n;                 // Build up from 2 to n
    next = a + b                // Next Fibonacci
    a = b                       // Shift window forward
    b = next

PRINT b                         // F(n)

// Fibonacci (Recursive)

// Get n
n = INPUT
IF n < 0 THEN;                  // Reject negatives
    PRINT "Error"
    STOP

FUNC FIB(k)
    IF k == 0 THEN; RETURN 0    // Base case
    IF k == 1 THEN; RETURN 1    // Base case
    RETURN FIB(k-1) + FIB(k-2)  // Recursive step

PRINT FIB(n)

// Palindrome Check (Two Pointers)

// Get a string to test
s = INPUT
left = 0                        // Pointer: start of string
right = s.length - 1            // Pointer: end of string

WHILE left < right;             // Move inward from both ends
    IF s[left] != s[right] THEN;
        PRINT "Not Palindrome"
        STOP
    left = left + 1
    right = right - 1

PRINT "Palindrome"

// Singly Linked List Traversal

// Node structure (conceptual)
// node.value → the data
// node.next  → pointer to the next node (or NULL at end)

// Get head of list
head = INPUT_HEAD               // Pointer to first node
current = head                  // Traversal pointer

WHILE current != NULL;          // Loop until we reach the end
    PRINT current.value         // Visit current node
    current = current.next      // Move pointer to next node

// End when current is NULL


// Convert String to Lowercase

str = "FAST Enterprises"          // Input string
result = ""                       // Empty string to store result

FOR i = 0 TO str.length - 1;      // Loop through each character
    ch = str[i]                   // Current character

    IF ch >= 'A' AND ch <= 'Z' THEN;    // Check if uppercase
        ch = ch + 32                    // Convert to lowercase (ASCII: +32 difference)

    result = result + ch          // Add converted character to result

PRINT "Lowercase:", result


//Stack (Push/Pop)

// Storage + pointer
stack = new array[CAPACITY]   // Fixed-size array for storage
top = -1                      // Pointer: index of the current top item (-1 means empty)

// Push (add to top)
PUSH(x)
    IF top == CAPACITY - 1 THEN          // Check overflow
        PRINT "Stack Full"
        RETURN
    top = top + 1                        // Move top pointer up
    stack[top] = x                       // Place item at the new top

// Pop (remove from top)
POP()
    IF top == -1 THEN                    // Check underflow
        PRINT "Stack Empty"
        RETURN
    value = stack[top]                   // Read the top item
    top = top - 1                        // Move top pointer down
    RETURN value

// Peek (read top without removing)
PEEK()
    IF top == -1 THEN
        PRINT "Stack Empty"
        RETURN
    RETURN stack[top]

// isEmpty (check if stack has no items)
isEmpty()
    RETURN (top == -1)


//Queue (Enqueue/Dequeue)

// Storage + pointers + size
queue = new array[CAPACITY]   // Fixed-size array for storage
front = 0                     // Pointer: index of the next item to remove
rear = 0                      // Pointer: index where the next item will be added
size = 0                      // Tracks how many items are in the queue

// Enqueue (add to rear)
ENQUEUE(x)
    IF size == CAPACITY THEN              // Check overflow
        PRINT "Queue Full"
        RETURN
    queue[rear] = x                       // Place item at rear
    rear = (rear + 1) % CAPACITY          // Move rear pointer forward (wrap around)
    size = size + 1

// Dequeue (remove from front)
DEQUEUE()
    IF size == 0 THEN                     // Check underflow
        PRINT "Queue Empty"
        RETURN
    value = queue[front]                  // Read the front item
    front = (front + 1) % CAPACITY        // Move front pointer forward (wrap around)
    size = size - 1
    RETURN value

// Peek (read front without removing)
PEEK()
    IF size == 0 THEN
        PRINT "Queue Empty"
        RETURN
    RETURN queue[front]

// isEmpty (check if queue has no items)
isEmpty()
    RETURN (size == 0)

/*
SQL
*/

// Simulated table 'TaskQueue' with columns (id, task_name, status)

START processTaskQueue()

    // Simulated table 'TaskQueue' with columns (id, task_name, status)

    WHILE EXISTS(SELECT * FROM TaskQueue WHERE status = 'pending')
        task = SELECT TOP 1 * FROM TaskQueue WHERE status = 'pending' ORDER BY id ASC
        PRINT "Processing task:", task.task_name
        UPDATE TaskQueue SET status = 'completed' WHERE id = task.id
    ENDWHILE

