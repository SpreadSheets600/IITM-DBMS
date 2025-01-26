## Week 2 Graded Assessment

1. **Select the list of possible foreign key(s) for the given relations.**

**Explanation**: Foreign keys must reference primary keys of other tables. Here, `employee_num` in taskAssignment references employees`(employee_num)` and`task_num` in `taskAssignment` references `tasks(task_num)`. Therefore, both `employee_num` and `task_num` in taskAssignment are foreign keys linking to their respective primary keys in employees and tasks tables.

`employee_num, task_num`

2. **Using the table Students, choose the correct SQL statement that will return the resultant table given.**

**Explanation**: The query groups students by Age and Country to count how many students exist in each unique Age-Country combination, where Australia has 2 students aged 13, Germany has 1 student aged 13 and 2 aged 16, Scotland has 1 student aged 15, and Ireland has 1 student aged 18.

```sql
SELECT Age, Country, COUNT(*) FROM Students GROUP BY Age, Country
```

3. **Using the table Students, choose the correct SQL statement that will return the resultant table given.**

**Explanation**: The query groups students by Age and Country to count how many students exist in each unique Age-Country combination, where Australia has 2 students aged 13, Germany has 1 student aged 13 and 2 aged 16, Scotland has 1 student aged 15, and Ireland has 1 student aged 18.

```sql
SELECT DISTINCT Age, Country FROM Students ORDER BY Age DESC;
```

4. **Identify the appropriate query to find the city having minimum rainfall.**

**Explanation**: This query correctly finds Aligarh which has the minimum rainfall (3mm) by using WHERE clause to compare each row's rainfall with the minimum rainfall value. The other options are incorrect because:

- HAVING requires GROUP BY
- Using self-join with < would return multiple cities
- EXCEPT with self-join is unnecessarily complex and would give incorrect results

```sql
SELECT city
FROM weatherReport
WHERE rainfall = MIN(rainfall)
```

5. **Identify the output for the following SQL statement.**

**Explanation**: The query selects the city_code column from the weatherReport table and orders the result by state in ascending order and city in ascending order within each state. The output will be the city codes sorted by state and city.

```sql
SELECT city_code
FROM weatherReport
ORDER BY state, city;
```

6. **Which of the following statements are TRUE?**

**Explanation**:

- A candidate key is a minimal superkey (cannot remove any attributes while maintaining uniqueness)
- Therefore every candidate key must be a superkey by definition
- Not all superkeys are candidate keys (superkeys can have extra attributes)
- Not all superkeys are primary keys (only one candidate key becomes primary key)
- A foreign key can reference a primary key but is not required to be one itself

`All candidate keys are superkeys`

7. **Identify the correct operations that result in the output shown.**

**Explanation**:
This operation correctly produces the output shown in Figure 7 through:

- First performs a Cartesian product of r1 and r2
- Filters (σ) where B values match between r1 and r2 AND D values match
- Projects (π) only the needed columns A, B (from r1), C, D (from r1), and E
- Results in exactly the 4 tuples shown in Figure 7 with matching B and D values and the correct column ordering

`π A, r1.B, C, r1.D, E (σ r1.B = r2.B ∧ r1.D = r2.D ( r1 × r2 ))`

8. **Consider a table department that has salary as an attribute. What will be the output of the following query?**

**Explanation**: The SQL query uses the LIKE pattern '30%5\_\_%' which means:

- Starts with '30'
- Has any digit in the middle (%)
- Has '5' after that
- Fllowed by any two characters (\_)
- Therefore, 30050 matches this pattern as:
  - 30 (matches '30')
  - 0 (matches %)
  - 5 (matches '5')
  - 0 (matches first \_)
  - 0 (matches second \_)

`salary with value 30050`

9. **Identify the SQL statement(s) that find(s) the names of suppliers who supply parts with part_num 301 but do not supply parts with part num 304.**

**Explanation**: The correct query uses a subquery to find suppliers who supply part_num 301 but not 304.

```sql
SELECT sup_name
FROM suppliers s, parts p
WHERE s.sup_num = p.sup_num AND part_num = 301
EXCEPT
SELECT sup_name
FROM suppliers s, parts p
WHERE s.sup_num = p.sup_num AND part_num = 304;
```

10. **How many rows will be returned by the above SQL query?**

**Explanation**: The number of rows returned will be equal to the number of distinct sup_num values where their associated parts have part_qty > 30.

- Groups are formed by sup_num (GROUP BY s.sup_num)
- Only considers parts with quantity > 30
- Each supplier number appears once in the result since it's grouped by sup_num
- From Figure 8, there are 3 suppliers (S1, S2, S3) that have parts with quantity > 30

`3 Rows`
