SELECT student_fname, student_lname
FROM students
WHERE
    department_code = 'MCA'
    AND dob > '2002-06-15'
