## 📒 Notes

### Attributes

- Attributes are the properties or characteristics that describe entities within a database.
- They provide essential information about the data stored in the database and help to effectively the organize the database structure.

### Types Of Attributes

### Schema

- A schema is the blueprint or overall design of a database.
- It defines the logical structure of the database, including:
    - Table definitions
    - Column names and data types
    - Relationships between tables
    - Constraints
- Schemas are relatively static and do not change frequently.
- They are typically modified only when the database structure needs to be altered, such as adding new tables or columns.

### Instance

- An instance, also known as a database state, is a snapshot of the actual data in the database at a specific moment in time.
- It represents the current content of the database, including all the data values that conform to the schema structure.
- The key characteristics of the instance are as follows :
    - Dynamic : Instances change frequently as data is added, updated, or deleted.
    - Temporal : They represent the state of the database at a particular point in time.
    - Volatile : The data in an instance can be modified through various database operations.

| **Aspect** | **Schema** | **Instance** |
| --- | --- | --- |
| Definition | Overall structure and design of the database | Actual data stored at a particular moment |
| Nature | Static (changes infrequently) | Dynamic (changes frequently) |
| Content | Table structures, relationships, constraints | Data entries, records in tables |
| Modification | Requires significant effort and planning | Easily altered by CRUD operations |
| Representation | Describes how data should be organized | Shows the current state of data |

## Relational Schema And Instance

- Relation schema defines the design and structure of the relation or table in the database.
- It is the way of representation of relation states in such a way that every relation database state fulfills the integrity constraints set on a relational schema.

- Let $A1, A2,A3 ... An$ be attributes for a database.
- Then relation is given by $R = (A1, A2, A3 ... An)$
- Formally given as $D1, D2, D3 ....Dn$ as relation $R$ is a subset of $D1 \times D2 \times D3 \times.... \times Dn$
- Thus relation is a set of $n$ tuples $(a1, a2, a3 ... an)$ where each $ai \space \epsilon \space Di$
- The relation is represented using tables, and each element of the relation is a row in the table.

## Keys

- Kyes are widely used to identify the tuples(rows) uniquely in the table.
- If $K \subseteq R$, where $R$ is a set of attributes in a relation.

### Types Of Keys

1. **Super Keys**
- The set of one or more attributes (columns) that can uniquely identify a tuple (record) is known as super key.
- A super key is a group of single or multiple keys that uniquely identifies rows in a table. **It supports NULL values in rows.**
- A super key can contain extra attributes that aren’t necessary for uniqueness.
- $K$ is a superkey of $R$ if values of $K$ are sufficient to identify a unique tuple of each possible relation $r(R)$.
- Example : { ID } and { ID, name } are both superkeys of instructor.

1. **Candidate Keys**
- The minimal set of attributes that can uniquely identify a tuple is known as a candidate key.
- **It is a super key with no repeated data is called a candidate key.**
- **Super Key $K$ is a candidate key if it’s minimal.**
- Example : {ID} is a candidate key for instructor.

1. **Primary Key**
- One of the candidate keys is selected to be the primary key.
- A **primary key** is a **unique key**, meaning it can uniquely identify each record (tuple) in a table.
- It must have **unique values** and cannot contain any **duplicate** values.
- A **primary key** **cannot be NULL**, as it needs to provide a valid, unique identifier for every record.

![image.png](attachment:ba9c6ddb-5031-4323-a6ec-addf0bc19ba9:image.png)

1. **Alternate Key**
- The keys that are not selected as a primary key in a table is called an alternate key.
- An alternate key is also referred to as a **secondary key** because it can uniquely identify records in a table, just like the primary key.

1. **Composite Key**
- Consists of more than one attribute to uniquely identify an entity occurrence.
- In short more than one primary key in table, then it is called a composite key.

1. **Foreign Key**
- Primary key in one table which is referencing to a another table in a relation is called a foreign key.
- Value in one relation must appear in another (in other words, when a particular attribute is a key in a different table)
- They act as a cross-reference between the tables.

1. **Compound Key**
- It consists of more than one attribute to uniquely identify an entity occurrence.

![image.png](attachment:e5d65158-744e-42ed-8a1c-dda8163182c8:image.png)

![image.png](attachment:c9810eb7-bc53-4805-9eae-9d2cd9ee4d2a:image.png)

![image.png](attachment:24bcc9bc-e0cf-4579-b264-4602ed651f98:image.png)

## Relational Query Languages

- Relational Database systems are expected to be equipped with a query language that assists users to query the database.
- Relational Query Language is used by the user to communicate with the database user requests for the information from the database.
- Relational algebra breaks the user requests and instructs the DBMS to execute the requests.
- It is the language by which the user communicates with the database.

### **Procedural Query Language**

- In Procedural Language, the user instructs the system to perform a series of operations on the database to produce the desired results.
- Users tell what data to be retrieved from the database and how to retrieve it.
- Procedural Query Language performs a set of queries instructing the DBMS to perform various transactions in sequence to meet user requests.

### **Relational Algebra is a Procedural Query Language**

1. **Select ( $\sigma$ ):** Returns rows of the input relation that satisfy the provided predicate. It is unary Operator means requires only one operand.
2. **Projection ( ℼ ):** Show the list of those attribute which we desire to appear and rest other attributes are eliminated from the table. It separates the table vertically.
3. **Set Difference ( - ):** It returns the difference between two relations. If we have two relations R and S them R-S will return all the tuples (row) which are in relation R but not in Relation S , It is binary operator.
4. **Cartesian Product ( X ):** Combines every tuple (row) of one table with every tuple (row) in other table ,also referred as cross Product . It is a binary operator.
5. **Union ( U ):** Outputs the union of tuples from both the relations. Duplicate tuples are eliminated automatically. It is a binary operator means it require two operands.

## Operations

## History Of SQL ( Structured Query Language )

- IBM developed Structured English Query Language (SEQUEL) as a part of System R project.
- Renamed Structured Query Language ( SQL: still pronounced as SEQUEL )

## Alternatives

- There aren't any alternatives to SQL for speaking to relational databases ( i.e. SQL as a protocol )
    - There are alternatives to writing SQL in the applications
- These alternatives have been implemented in the form of front-ends for working with relational databases. Some examples of a front-end include (for a section of languages):
    - **SchemeQL** and **CLSQL**
        - Probably the most flexible, thanks to their [Lisp](https://en.wikipedia.org/wiki/Lisp_(programming_language)) heritage
        - They also look a lot more like SQL than other front-ends
    - **LINQ** (in [.NET](https://dotnet.microsoft.com/))
    - **ScalaQL** and **ScalaQuery** (in [Scala](https://www.scala-lang.org/))
    - **SQL Statement**, **ActiveRecord** and many others in [Ruby](https://www.ruby-lang.org/en/)

## Derivatives

- There are several query languages that are derived from or inspired by SQL.
- Out of these, the most popular and effective is **SPARQL**.
- **SPARQL** ( pronounced *sparkle,* a recursive acronym for *SPARQL Protocol and RDF Query Language* ) is an RDF query language
    - A semantic query language for databases - able to retrieve and manipulate data stored in ***Resource Description Framework*** ( ***RDF*** ) format.
    - It has been standardized by the W3C Consortium as key technology of the semantic web
    - Versions
        - SPARQL 1.0 (Jan. 2008)
        - SPARQL 1.1 (Mar. 2013)

## Data Definition Language (DDL)

The SQL data-definition language ( DDL ) allows the specification of information about relations, including :

- *Integrity Constraints*
- The *Schema* for each *Relation*
- The *Domain* of values associated with each *Attribute*
- And, as we will see later, also other information such as :
    - The set of *Indices* to be maintained for each relations
    - *Security and Authorization* information for each relation
    - The *Physical Storage Structure* of each relation on disk

### Data Types In SQL

- ***char(n)*** - Fixed length character string, with user-specified length *n*
- ***varchar(n)*** - Variable length character strings, with user-specified max length *n*
- ***int*** - Integer (a finite subset of the integers that is machine-dependent)
- ***smallint(n)*** - Small integer (a machine-dependent subset of the integer domain type)
- ***numeric(p, d)*** - Fixed point number, with user-specified precision of *p* digits, with *d* digits to the right of decimal point. (ex. *numeric(3, 1)* allows 44.5 to be stored exactly, but not 444.5 or 0.32)
- ***real, double precision*** - Floating point and double-precision floating point numbers, with machine-dependent precision
- ***float(n)*** - Floating point number with user specified precision of at-least *n* digits

### Create Table Construct

- An SQL relation is defined using the **create table** command:
    
    **create table** *r* $(A_{1}D_{1}, A_{2}D_{2},...,A_{n}D_{n}),$
    
    $(integrity-constraint_{1}),$
    
    $...$
    
    $(integrity-constraint_{k}));$
    
- ***r*** is the name of the relation (table)
- each $A_i$ is an attribute name in the schema of relation ***r***
- $D_i$ is the data type of values in the domain of attribute $Ai$

**For Example -**

```sql
create table instructor (
	ID char(5),
	name varchar(20),
	dept_name varchar(20),
	salary numeric(8, 2));
```

### Create Table Construct : Integrity Constraints

- **not null ⇒ Ensures no value can be left empty**
- **primary key $(A_1,...,A_n)$ ⇒ Makes the column / attribute unique ( Not Null, and prevents duplicate data )**
- **foreign key $(A_m,...,A_n)$ references *r ⇒ References to the primary key of another table in a relation.***

```sql
create table instructor (
	ID char(5),
	name varchar(20) not null,
	dept_name varchar(20),
	salary numeric(8, 2),
	primary key (ID),
	foreign key (dept_name) references department));
```

### Updating Tables

| Name | Command | Type |
| --- | --- | --- |
| Insert | **`insert into** *instructor* **values** ('10211', 'Smith', 'Biology', 66000);` | DML |
| Delete | `delete from <databse_name>` | DML |
| Drop | `drop table <table_name>`  | DDL |
| Alter | `ater table <table_name> <r> add <a> <d>` 
( a ⇒ attribute, r ⇒ relation and d ⇒ domain ) | DDL |
| Alter | **`alter table** *r* **drop** a` 
( a ⇒ attribute, r ⇒ relation and d ⇒ domain ) | DDL |

## Data Manipulation Language ( DML )

- A typical SQL query has the form:
    
    **select** $A_1, A_2,..., A_n$
    
    **from** $r_1, r_2,...,r_m$
    
    **where** $P$
    
    - $A_i$ represents an attribute from $r_i$'*s*
    - $r_i$ represents a relation
    - $P$ is a predicate
- The result of an SQL query is a relation.

### Select Clause

- The **select** clause lists the attributes desired in the result of a query.

```sql
select <attribute> from <table_name>
```

- **SQL allows duplicates in relations as well as in query results.**
- To force eliminate the duplicates we use the `distinct` word.

```sql
select distinct <attribute>
from <table_name>
```

- When keyword `all` is specified, it states all duplicates to be included as well.

```sql
select all <attribute>
from <table_name>
```

- Using `*` includes all the attributes to be included.

```sql
select *
from <table_name>
```

### Where Clause

- It specifies the condition to be satisfied, it corresponds to the selection predicate of linear algebra.

```sql
select <attribute_1>
from <table_name>
where <attribute_2> = "<object>"
```

- Logical operations can be performed using the logical connectives **and, or, not.**
- Other arithmetic operations can also be performed using the arithmetic operators.
- SQL includes a **between as** comparison operator.

```sql
select <attribute_1>
from <table_name>
where <attribute_2> between "<object_1>" and "<object_2>"
```

- SQL can a includes tuple comparison.

```sql
select <attribute_1>
from <table_name>
where <attribute_2> in ("<object_1>", "<object_2>")
```

### From Clause

- The **from** clause lists the relations involved in the query

```sql
select *
from <table_1>, <table_2>
```

- Generates every possible `table_1` - `table_2` pair with all attributes from both relations.
- This is also known as the cartesian product of the tables.
- Cartesian product is not very useful directly, but useful when combined with the where-clause condition (selection operation in relational algebra)

### Cartesian Product ( JOINS )

- The join operation merges the two tables based on the same attribute name and their data types are known as Natural join Unlike INNER JOIN ( EQUI JOIN ), which requires you to specify the columns and conditions for the join explicitly.

### Equi Join

- Inner Join joins two table on the basis of the column which is explicitly specified in the **ON / AS clause**.
- The resulting table will contain all the attributes from both the tables including common column also.
- An inner join ( equi join ) between two tables will return only records where a joining field, such as a key, finds a match in both tables.

```sql
select *
from <table_1> as <t1>
inner join <table_2> as <t2>
on <t1>.<attribute> = <t2>.<attribute>
```

- The above can also be simply written as,

```sql
select *
from <table_1>, <table_2>
where <t1>.<attribute> = <t2>.<attribute>
```

![image.png](attachment:3b25fa30-373a-4fb4-958a-0819f73bd99b:image.png)

### Natural Join

- Natural Join in **SQL** joins two tables based on the same attribute name and **datatypes**.
- The resulting table will contain all the attributes of both tables but keep only one copy of each common column.

```sql
select * 
from <table_1> natural join <table_2> 
```

| **NATURAL JOIN** | **INNER JOIN** |
| --- | --- |
| Natural Join joins two tables based on same attribute name and datatypes. | Inner Join joins two table on the basis of the column which is explicitly specified in the ON clause. |
| In Natural Join, The resulting table will contain all the attributes of both the tables but keep only one copy of each common column | In Inner Join, The resulting table will contain all the attribute of both the tables including duplicate columns also |
| In Natural Join, If there is no condition specifies then it returns the rows based on the common column | In Inner Join, only those records will return which exists in both the tables |
| `select * from <table_1> natural join <table_2>`  | `select * from <table_1>, <table_2> where <t1>.<attribute> = <t2>.<attribute>` |

### As Operation

- The SQL allows renaming relations and attributes using the **as** clause.

```sql
old_name as new_name
```

## String Operations

- SQL includes a string-matching operator for comparisons on character strings.
- The operator **like** uses patterns that are described using two special characters:
    - **percent (%)**
        
        The % character matches any sub-string
        
    - **underscore ( _ )**
        
        The _ character matches any character
        

```sql
select <sttribute>
from <table>
where <Attribute> like '%substring%'
```

- Patterns are *case sensitive*
- Short Examples
    - 'Intro%' matches any string beginning with "Intro"
    - '%Comp%' matches any string containing "Comp" as a substring
    - '___' (3 underscores) matches any string of exactly 3 characters
    - '___%' (3 underscores and then a %) matches any string of at least 3 characters
- SQL supports variety of string operations such as
    - Concatenation (using "$||$") [ double pipe symbol ]
    - Converting from upper to lower case (and vice-versa)

### Order By Clause

- Arrange the results in ascending or descending order depending upon the criteria given.
- It can be used to solve multiple attributes.

### Duplicates

- In relations with duplicates, SQL can define how many copies of tuples appear in the result.
- **Multiset** versions of some of the relational algebra operators - given multiset relations $r_1$ and $r_2$:
    
    a) **SELECT** **$\sigma_{\theta}(r_1):$** If there are $c_1$ copies of tuple $t_1$ in $r_1$ and $t_1$ satisfies selection $\sigma_{\theta}$, then there are $c_1$ copies of $t_1$ in $\sigma_{\theta}(r_1)$
    
    b) **PROJECTION** $\Pi_A(r):$ For each copy of tuple $t_1$ in $r_1$, there is a copy of tuple $\Pi_A(t_1)$ in $\Pi_A(r_1)$ where $\Pi_A(t_1)$ denotes the projection of the single tuple $t_1$
    
    c) $r_1 \times r_2:$ If there are $c_1$ copies of tuple $t_1$ in $r_1$ and $c_2$ copies of tuples $t_2$ in $r_2$, there are $c_1 \times c_2$ copies of the tuple $t_1 \cdot t_2$ in $r_1 \times r_2$
    
- Example:
    - Suppose multiset relations $r_1(A, B)$ and $r_2(C)$ are as follows:
        
        $r_1 = \{(1, a)(2, a)\}$ ; $r_2 = \{(2),(3),(3)\}$
        
    - Then $\Pi_B(r_1)$ would be $\{(a),(a)\}$ while $\Pi_B(r_1) \times r_2$ would be
        
        $\{(a, 2),(a, 2),(a, 3),(a, 3),(a, 3),(a, 3)\}$
        
- SQL Duplicate Semantics:
    
    **select** $A_1, A_2, ...,A_n$
    
    **from** $r_1, r_2, ..., r_m$
    
    **where** $P$ is equivalent to the multiset version of the expression:
    
    $\Pi_{A_1,A_2,...,A_n}(\sigma_P(r_1 \times r_2 \times ... \times r_m))$
    

## Set Operations

- **UNION** : Merges all unique rows from two or more SELECT statements, eliminating duplicates.
- **UNION ALL :** Merges all rows from two or more SELECT statements, keeping duplicates.
- **INTERSECT :** Returns only the rows that appear in both SELECT statements.
- **EXCEPT :** Returns rows from the first SELECT statement that don't appear in the second.

### Example

- The courses that ran in Fall 2009 **or** in Spring 2010 ( UNION )

```sql
(select course_id from section where sem = 'Fall' and year = 2009)
union
(select course_id from section where sem = 'Spring' and year = 2010)
```

- The courses that ran in Fall 2009 **and** in Spring 2010 ( INTERSECT )

```sql
(select course_id from section where sem = 'Fall' and year = 2009)
intersect
(select course_id from section where sem = 'Spring' and year = 2010)
```

- The courses that ran in Fall 2009 **but not** in Spring 2010 ( EXCEPT )

```sql
(select course_id from section where sem = 'Fall' and year = 2009)
except
(select course_id from section where sem = 'Spring' and year = 2010)
```

- Set operations such as **union**, **intersect** and **except** automatically eliminate the duplicates.
- To retain all the duplicates, use the corresponding multiset versions **union all**, **intersect all** and **except all.**
- Suppose a tuple occurs *m* times in *r* and *n* times in *s*, then it occurs
    - $m + n$ times in *r* **union all** *s*
    - min(*m*, *n*) times in *r* **intersect all** *s*
    - max(0, *m* - *n*) times in *r* **except all** *s*

### Null Values

- A NULL value is something unknown or a value that does not exist yet
- **Importance Of Null Values ?**
    - Certain values may not exist for everyone.
    - Often times while we are creating/inserting a record, we may not know all the values of all the fields.
- It is possible for tuples to have a *null* value, denoted by **null**, for some of their attributes.
- It is not possible to test for *null* values with comparison operators such as $=, \lt, \gt or \lt \gt$
- We use *null* and *not null* operators instead.

### NULL values : Three Valued Logic

- Three values - **true, false, unknown**
- Any comparison with *null* returns *unknown*
    - Example: $5 \lt null$ or $null \lt\gt null$ or $null = null$
- Three-valued logic using the value unknown:
    - **OR:**
        - (*unknown* **or** *true*) = *true*
        - (*unknown* **or** *false*) = *unknown*
        - (*unknown* **or** *unknown*) = *unknown*
    - **AND:**
        - (*true* **and** *unknown*) = *unknown*
        - (*false* **and** *unknown*) = *false*
        - (*unknown* **and** *unknown*) = *unknown*
    - **NOT:**
        - (**not** *unknown*) = *unknown*
    - "*P* **is unknown**" evaluates to *true* if predicate *P* evaluates to *unknown*
- Result of **where** clause predicate is treated as *false* if it evaluates to *unknown*

### Aggregate Functions

- These functions operate on the multiset of values of a column of a relation (table) and return a value -
    - **avg:** average value
    - **min:** minimum value
    - **max:** maximum value
    - **sum:** sum of the values
    - **count:** number of values

**Examples**

- Find the average salary of instructors in the Computer Science department

```sql
select avg(salary)
from instructor
where dept_name = 'Comp. Sci.'
```

- Find the total number of instructors who teach a course in the Spring 2010 semester

```sql
select count(distinct ID)
from teaches
where semester = 'Spring' and year = 2010
```

- Find the number of tuples in the *course* relation (table)

```sql
select count(*)
from courses;
```
