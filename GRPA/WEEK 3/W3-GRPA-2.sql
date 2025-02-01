SELECT p.name 
FROM players p 
JOIN teams t ON p.team_id = t.team_id 
WHERE t.name = 'All Stars' 
AND p.dob = (
    SELECT MIN(dob) 
    FROM players pl 
    JOIN teams te ON te.team_id = pl.team_id 
    WHERE te.name = 'All Stars'
)