SELECT p.name
FROM players p
JOIN teams t ON p.team_id = t.team_id
WHERE t.name = 'Amigos'