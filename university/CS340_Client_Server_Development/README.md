## How I write programs that are maintainable, readable, and adaptable ##

I write programs in a modular way so that each part of the system has a clear responsibility. Instead of combining database logic, user interface logic, and data processing into one file, I separate them into independent components that can be reused and modified without breaking the rest of the system.
In Project One, I created a standalone CRUD Python module that handled all database operations. This allowed Project Two’s dashboard to communicate with MongoDB through clean, reusable methods rather than embedding raw database queries directly into the dashboard code.
The advantage of working this way was improved readability and maintainability. If the database schema changes or new queries are needed, I can modify the CRUD module without rewriting the dashboard interface.
This structure also improves adaptability. The same CRUD module could be reused in a web application, an API service, or another analytics dashboard without redesigning the entire backend logic.
Writing clear function names, consistent formatting, and descriptive variable names makes the code easier for other developers to understand and extend.
I focus on keeping logic simple and predictable so that future updates require minimal refactoring.

## How I approach a problem as a computer scientist ##

I begin by carefully analyzing the requirements before writing any code. For the Grazioso Salvare dashboard, I first identified what data needed to be stored, what queries were required, and how users would interact with the system.
I break complex problems into smaller steps. For this project, I separated database design, CRUD functionality, and dashboard visualization into independent development phases.
Compared to earlier programming assignments, this project required thinking about real client needs instead of just producing correct output. I had to design a system that would scale and remain usable over time.
I use iterative development. I test database queries independently before integrating them into the dashboard. I verify filters, sorting, and aggregation before connecting them to user interface elements.
In the future, when building databases for other clients, I would begin by modeling the data structure carefully and planning indexing and aggregation strategies early to improve performance.

## What computer scientists do and why it matters ##

Computer scientists design systems that organize, process, and transform data into meaningful information.
In this project, the dashboard transformed raw animal rescue data into filtered tables, charts, and geographic maps that help users make informed decisions.
For a company like Grazioso Salvare, this type of system improves efficiency by reducing manual data sorting and enabling quick insights through automated queries and aggregation.
By building scalable database solutions and clean backend logic, computer scientists help organizations reduce errors, improve accuracy, and make faster data-driven decisions.
This work matters because modern organizations depend on reliable data systems to operate effectively and compete successfully.
