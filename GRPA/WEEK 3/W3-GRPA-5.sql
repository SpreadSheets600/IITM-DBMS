SELECT bc.title, COUNT(bcp.accession_no) as copy_count
FROM book_catalogue bc
LEFT JOIN book_copies bcp ON bc.ISBN_no = bcp.ISBN_no
WHERE bc.title LIKE '%Programming%'
GROUP BY bc.title