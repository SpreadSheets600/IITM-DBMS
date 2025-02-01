SELECT DISTINCT s.department_code, m.member_type
FROM students s
JOIN members m ON s.roll_no = m.roll_no
JOIN book_issue bi ON m.member_no = bi.member_no
WHERE bi.doi = '2021-08-02'