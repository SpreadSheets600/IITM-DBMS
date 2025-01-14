## 📖 Quick Summary

<aside>
**Key Takeaways** :

- DBMS evolved from physical record-keeping to modern database systems, offering superior data management capabilities over traditional methods
- Key advantages include scalability, performance optimization, data consistency, and robust security features
- Database architecture follows a three-level abstraction model: physical, logical, and view levels
- SQL serves as the primary language for database operations, though it's often integrated with other programming languages
- Transaction management ensures data integrity through ACID properties and concurrency control
- Modern database systems support various data models and architectures to meet different organizational needs
</aside>

## 📒 Notes

### Data Management

- Management of data or records is a basic need for human society :
    - storage of data : remember things and maintain a record
    - retrieval of data : to get the stored data back for later
    - **storage and retrieval are most the important aspect of data management**
    - transaction : some action taken on the data.
    - audit : logging of all the transactions, details of what happened and who did it ?
    - archival : archiving the data for later use

### Physical

- Physical data formally known as Book Keeping was used.
- The most significant development happened when **Henry Brown** patented a " **receptacle for storing and preserving papers** " ( file cabinet ) on Nov 2 , 1886 .
- **Herman Hollerith** adopted the **punch cards** used for weaving looms to act as the memory for a mechanical tabulating machine in 1890 .

### Electronic

- Electronic data and records management evolves with technological advances — particularly in memory, storage, computing, and networking.
    - 1950 : Computer programming emerged.
    - 1960 : Data management utilized punch cards and magnetic tapes.
    - 1970 :
        - COBOL and CODASYL approach introduced in 1971
        - Apple II platform launched VisiCalc on October 14, 1979, marking the birth of spreadsheets.
        - Magnetic disks became widespread.
    - 1980 : RDBMS transformed data management.
    - 1990 : Internet made data management global.
    - 2000 : E-commerce boomed - NoSQL emerged for unstructured data management.
    - 2010 : Data Science gained prominence.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/b644516a-7804-47e9-9455-0a04e3cecf0b/406471bc-51cc-4f9c-94f6-582de76a0cef/image.png)

### Book Keeping ( Physical Storage )

- Book keeping refers to the traditional method of maintaining physical records in ledgers, files, and paper documents.
- This system, while reliable for centuries, had several limitations including physical storage constraints, difficulty in searching records, and vulnerability to damage or loss.
- Manual book keeping also required significant time and effort for data entry, calculations, and maintaining organized records.

### Spreadsheet Files ( Digital Storage )

- Spreadsheets revolutionized data management by providing a digital solution for organizing and analyzing data in rows and columns.
- They offer features like automatic calculations, data sorting, and filtering that were impossible with physical records.
- The introduction of spreadsheet software marked a significant shift from manual to computerized data management, making it easier to maintain and manipulate large datasets.

### Book Keeping VS Spreadsheet Files

- Durability - less prone to physical damage
- Scalability - easier to search and modify, easier to upgrade storage
- Security - password protected, user-based access
- Ease of Use - easier to search records, modify and maintain
- Consistency - less prone to mistakes, easier to check for them
- Efficiency - faster data processing and retrieval , automated calculations and analysis
- Cost - lower initial setup and maintenance costs

### DBMS VS Spreadsheet Files

- No row count limitations
- Superior performance when handling large datasets
- Maintains data consistency across all entries
- Enforces data validation rules (e.g., ensuring correct data types)
- Provides granular user access controls and permissions
- Includes built-in safeguards against system failures

### File Handling - Python VS DBMS

| Parameter | File Handling via Python | DBMS |
| --- | --- | --- |
| Scalability - amount of data | Very difficult to insert, modify, and query records | In-built features to provide high scalability for a large number of records |
| Scalability - changes in data structure | Extremely difficult to change the structure of records as in the case of adding or removing attributes | Adding or removing attributes can be done seamlessly using simple SQL queries |
| Time of execution | In seconds | In milliseconds |
| Persistence (data survives after the process with which it was created has ended) | Data processed using temporary data structures have to be manually updated to the file | Data persistence is ensured via automatic, system-induced mechanisms |
| Robustness | Ensuring robustness of data has to be done manually | Backup, recovery, and restore need minimum manual intervention |
| Security | Difficult to implement in Python (Security at OS level) | User-specific access at database level |
| Programmer's productivity | Most file access operations involve extensive coding to ensure persistence, robustness, and security of data | Standard and simple built-in queries reduce the effort involved in coding, thereby increasing a programmer's throughput |
| Arithmetic operations | Easy to do arithmetic computations | Limited set of arithmetic operations are available |
| Costs | Low costs for hardware, software, and human resources | High costs for hardware, software, and human resources |

## Database Management System ( DBMS )

### Levels Of Abstraction

- Physical Level : describes how record is stored physically
- Logical Level : describes how data is stored in database and the relationships among the data fields, schemas and constraints
- View Level : describes how the data is presented to end users, showing only relevant portions of the database while hiding complexity

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/b644516a-7804-47e9-9455-0a04e3cecf0b/cfc5e5c6-f1f2-43a8-beb5-4452043dc0d6/image.png)

### Schema And Instance

- Schema is a way the data is organized, similar to type information of a variable.
    - Logical Schema : the overall logical structure of the database, define the data elements and
    their relationship.
    - Logical Schema : the overall physical structure of the database, how the actual database is
    built.
- Physical Data Independence: the ability to modify the physical schema without changing the logical
schema.
- Instance is the actual value of the data.
- Applications depends on the on the logical schema. Physical schema might change, we might change from one data type to another but the logical schema should not change.

### Data Model

It is a collection of tool that defines the data, semantics, relationships and constraints.

**There are several types of data models:**

- Relational Model - organizes data into tables with rows and columns
- Entity-Relationship Model - represents data using entities and their relationships
- Object-Oriented Model - represents data as objects with attributes and methods

### Data Definition Language ( DDL )

- DDL is a computer language used to define and modify the structure of database objects in a database.
- It allows users to create and modify database schemas and describes how the data should be stored in the database.
- DDL compiler sets a table template which is stored in data dictionary.
- Data dictionary contains data metadata which tells us about the data, database schema and other important metadata about database structures, relationships, constraints and authorization.
- The data dictionary serves as a centralized repository of information about the data stored in the database, making it easier to maintain and manage the database system efficiently.
- DDL statements are used to perform tasks like creating tables, modifying table structures, and defining constraints - all of which are recorded in the data dictionary.

### Data Manipulation Language ( DML )

- DML is a computer language used to manipulate and retrieve data from the database.
- It is also known as query language.
- It provides commands for tasks like inserting, updating, deleting, and querying data stored in database tables.
- While DDL deals with database structure, DML focuses on the actual data operations within that structure.

### Structured Query Language ( SQL )

- Most widely used commercial language.
- SQL is not a *Turning Machine Equivalent Language.* Which means that anything that can be written in SQL can be written in C, Python, Ruby, Rust but not everything written in C or python cannot be written in SQL.
- To perform complex functions, generally SQL is embedded and used with other high level language.
- We typically use SQL to store data and use other language ( host language ) to perform other complex tasks.

### Database Design

- The process of designing the genial structure of the database is called database design.
- **Logical Design**
    - Focuses on creating an abstract representation of the database structure, including entities, relationships, and attributes without considering physical implementation details
    - Involves defining tables, fields, relationships, and constraints that will store and organize the data
    - Results in a schema that serves as a blueprint for the database implementation
- **Physical Design**
    - Involves determining how the logical design will be implemented in the actual database system
    - Includes decisions about storage structures, file organization, indexing strategies, and access methods
    - Focuses on optimizing database performance, efficiency, and resource utilization

### Extensible Markup Language ( XML )

- It is defined by WWW Consortium ( W3C )
- Originally designed for marking up documents.
- Now it is widely used for storing and exchanging data between different systems and applications.
- XML provides a flexible, self-describing way to structure data using custom tags and attributes.
- It serves as a common format for data interchange on the web and in enterprise applications.
- A wide variety  of tools is available for parsing, browsing and querying XML documents/data.

## Database Engine

### Store Engine

- Program module that provides the interface between the low-level data stored in the database
and the application programs and queries submitted to the system.
- It is responsible for interaction with the OS file manager, efficient storing, retrieving and
updating of data.

### Query Processing

- Mostly includes parsing and translation, optimization and evaluation.
- Parsing - writing the query in terms of some language
- Optimization - finding the most efficient way to execute a query by analyzing different execution plans and choosing the one with lowest cost
- Evaluation - executing the optimized query plan to retrieve or modify data from the database

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/b644516a-7804-47e9-9455-0a04e3cecf0b/b5805e6e-b411-4606-a7e5-8a1e203bfed1/image.png)

### Transaction Management

- It is a collection of operations that perform a single logical function in a database application.
- Transactions are designed to maintain database consistency and integrity by ensuring that all operations within the transaction are completed successfully or none of them are applied.
- Each transaction follows ACID properties (Atomicity, Consistency, Isolation, Durability) to guarantee reliable processing of database operations.
    - Transaction Management Component
        - ensures that transactions are processed reliably and maintains data integrity through proper coordination of concurrent operations
        - handles transaction operations like commit, rollback, and recovery in case of system failures
        - works closely with the Concurrency Control Manager to prevent conflicts between simultaneous transactions
    - Concurrency Control Manager
        - ensures efficient handling of multiple concurrent transactions by controlling access to shared data resources
        - implements locking mechanisms and scheduling algorithms to maintain data consistency and prevent interference between transactions
        - helps maximize system performance while maintaining data integrity through proper synchronization of concurrent operations

### Database Architecture

- It is mostly influenced by the underlying computer system on which the database is running.
- Database architecture refers to how a DBMS system is organized internally and how it interacts with other components.
- The architecture can be classified into different types:
    - Single-tier architecture: where all components are on one system
    - Two-tier architecture: separates client and server
    - Three-tier architecture: divides the system into presentation, application, and data tiers
- The choice of architecture depends on factors like scalability needs, performance requirements, and system complexity.
