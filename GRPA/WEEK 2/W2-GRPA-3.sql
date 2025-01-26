SELECT p.name, p.jersey_no
FROM players p, teams t
WHERE
    p.team_id = t.team_id
    AND t.name = 'Rainbow'
