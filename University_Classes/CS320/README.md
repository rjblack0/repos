# CS320

## How can I ensure that my code, program, or software is functional and secure? ##

I make sure that my software is functional and secure by applying requirements-driven testing and automated unit tests throughout development. 
In my work in this course I validated functionality by writing JUnit test cases that directly corresponded to documented requirements, including both positive tests for expected behavior, and negative tests to verify that invalid input was properly rejected. 
This approach ensured that the software behaved in the expected manner under normal conditions as well as under edge cases. Security and stability are supported by enforcing strict validation rules, immutability where required, and consistent error handling, and I verified all of these through automated tests that promoted resuability whenever the code were to change.

## How do I interpret user needs and incorporate them into a program? ##

User needs are first translated into functional requirements with concrete constraints and behaviors interpreted into the code. 
In the Contact, Task, and Appointment services, user needs were expressed as rules such as required fields, maximum lengths, and immutability of identifiers. 
I incorporated these needs by enforcing them at the object and service level and then validating them through unit tests. By aligning each test case directly with a designated requirement, I ensured that the implementation met user expectations and prevented invalid or unsafe input from entering the system.

## How do I approach designing software? ##

I approach software design with a goal of simplicity, separation of concerns, and testability. Each class is designed with a single responsibility, and service classes manage business logic independently from data objects. 
Approaching the project this way makes the code easier to understand, maintain, and test. I keep testing in mind from the beginning, ensuring that methods are clear and easy to validate through automated unit tests. 
This approach is designed to support scalability, improve reliability, and align with modern development practices such as continuous integration and automated testing.
