### DBMS GRPA Solltuions - Week 2

<details>
<summary>Solution 1</summary>

```sql
SELECT DISTINCT
    team_id
FROM players
WHERE
    EXTRACT(
        YEAR
        FROM dob
    ) < 2003
```

</details>

<details>
<summary>Solution 2</summary>

```sql
SELECT city, playground FROM teams WHERE jersey_away_color = 'Pink'
```

</details>

<details>
<summary>Solution 3</summary>

```sql
SELECT p.name, p.jersey_no
FROM players p, teams t
WHERE
    p.team_id = t.team_id
    AND t.name = 'Rainbow'
```

</details>

<details>
<summary>Solution 4</summary>

```sql
SELECT student_fname, student_lname
FROM students
WHERE
    department_code = 'MCA'
    AND dob > '2002-06-15'
```

</details>

<details>
<summary>Solution 5</summary>

```sql
SELECT faculty_fname, faculty_lname
FROM faculty f, departments d
WHERE
    f.department_code = d.department_code
    AND d.department_name = 'Computer Science'
    AND f.doj > '2015-03-03'
```

</details>
