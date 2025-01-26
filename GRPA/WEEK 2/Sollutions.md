## DBMS GRPA Solltuions - Week 2

<details>
<summary> Question 1</summary>

![image](https://github.com/user-attachments/assets/11f040a2-3cb2-43de-b7c2-ddb57ce0e0dd)

Write an SQL statement to find the team_id of the players who were born before the year '2003'

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
</details>

<details>
<summary>Question 2</summary>
    
![image](https://github.com/user-attachments/assets/6f3d0f61-ff6e-4631-98ea-cec9e6828949)

Write an SQL statement to find the city and playground of the teams whose away-jersey color(jersey_away_color) is 'Pink'

<details>
<summary>Solution 2</summary>

```sql
SELECT city, playground FROM teams WHERE jersey_away_color = 'Pink'
```
</details>
</details>

<details>
<summary>Question 3</summary>

![image](https://github.com/user-attachments/assets/28cd421a-d30c-4a23-abf8-b3bd096e0b19)

Write an SQL statement to find the player name and jersey number of players from the team: 'Rainbow'

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
</details>

<details>
<summary>Question 4</summary>

![image](https://github.com/user-attachments/assets/451586be-3850-4436-bbd5-666f607e6a72)

Write an SQL statement to find the first names and the last names (student_fname, student_lname) of students who belong to the department with department code as 'MCA' and who were born after '2002-06-15'
    
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
</details>

<details>
<summary>Question 5</summary>

![image](https://github.com/user-attachments/assets/f829868e-d7cb-4da7-8a5a-2753c34f9f26)

Write an SQL statement to find the first names and the last names of faculty (faculty_fname, faculty_lname) who belong to the department:'Computer Science' and joined after '2015-03-03'

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
</details>
