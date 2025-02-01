SELECT m.match_num, r.name
FROM matches m 
JOIN match_referees mr ON m.match_num = mr.match_num
JOIN referees r ON mr.referee = r.referee_id
WHERE m.match_date = '2020-05-15'
