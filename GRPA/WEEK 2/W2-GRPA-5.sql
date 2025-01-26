SELECT faculty_fname, faculty_lname
FROM faculty f, departments d
WHERE
    f.department_code = d.department_code
    AND d.department_name = 'Computer Science'
    AND f.doj > '2015-03-03'
