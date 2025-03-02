import sys
import os
import psycopg2
import math

file = open("parameter.txt", "r")
x = file.read()

try:
    connection = psycopg2.connect(
        database=sys.argv[1],
        user=os.environ.get("PGUSER"),
        password=os.environ.get("PGPASSWORD"),
        host=os.environ.get("PGHOST"),
        port=os.environ.get("PGPORT"),
    )

    cursor = connection.cursor()
    query = """select SUM(matches.host_team_score) as S
            from matches,teams 
            where matches.host_team_id=teams.team_id
            and matches.host_team_score>matches.guest_team_score
            and teams.name LIKE '{}%' """.format(x)

    cursor.execute(query)
    result = cursor.fetchone()
    S = result[0]
    X = S * 10
    X_deg = X * (math.pi / 180)
    cos_value = round(math.cos(X_deg), 2)
    print(cos_value)

    cursor.close()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    connection.close()
