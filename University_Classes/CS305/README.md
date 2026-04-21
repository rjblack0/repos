# CS-305
Ryan Blackburn
Southern New Hampshire University
Oct. 22nd 2025
CS-305

//Briefly summarize your client, Artemis Financial, and its software requirements. Who was the client? What issue did the company want you to address?//
Our client, Artemis Financial, was a consulting company that creates financial plans for clients. The assignment was for our company, Global Rain, to improve their web application’s security by adding encrypted communication and a file verification process to protect client data during transfer.

//What did you do well when you found your client’s software security vulnerabilities? Why is it important to code securely? What value does software security add to a company’s overall well-being?//
I was able to identify where encryption and verification were missing and add secure features without breaking functionality. Secure coding helps prevent attacks, protects client data, and maintains trust, which are key factors in a company’s reputation and success.

//Which part of the vulnerability assessment was challenging or helpful to you?//
Setting up HTTPS with a self-signed certificate was the hardest part because it required configuring the keystore and amending registries to make the browser trust it. It was also the most helpful and educational because it gave me hands-on experience with real SSL setup and secure communication.

//How did you increase layers of security? In the future, what would you use to assess vulnerabilities and decide which mitigation techniques to use?//
I added a SHA-256 checksum to verify data integrity, enabled HTTPS for encryption, and used OWASP Dependency-Check to scan for vulnerabilities. In the future, I’d use tools like OWASP ZAP or automated CI/CD scans to continuously find and fix security issues.

//How did you make certain the code and software application were functional and secure? After refactoring the code, how did you check to see whether you introduced new vulnerabilities?//
I tested the application manually by running it and checking the hash output over HTTPS. Then I ran OWASP Dependency-Check to confirm there were no new vulnerabilities introduced after the refactor.

//What resources, tools, or coding practices did you use that might be helpful in future assignments or tasks?//
I used Java’s message digest for hashing, Spring Boot’s SSL configuration for HTTPS, and the OWASP Dependency-Check plug-in. These tools and secure coding habits will be useful for future software projects.

//Employers sometimes ask for examples of work that you have successfully completed to show your skills, knowledge, and experience. What might you show future employers from this assignment?//
I’d show the completed Practices for Secure Software Report and the working codebase to demonstrate that I can secure an application, implement encryption, and verify my work through testing and vulnerability scanning.
