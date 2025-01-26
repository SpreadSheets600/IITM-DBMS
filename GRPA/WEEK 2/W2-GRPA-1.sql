SELECT DISTINCT
    team_id
FROM players
WHERE
    EXTRACT(
        YEAR
        FROM dob
    ) < 2003
