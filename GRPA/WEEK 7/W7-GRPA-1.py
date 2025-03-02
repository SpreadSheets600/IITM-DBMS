import sys
import os
import psycopg2

file = open("date.txt", "r")
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
    query = """select referees.name 
            from referees,matches,match_referees
            where matches.match_date = '{}' 
            and matches.match_num=match_referees.match_num 
            and match_referees.referee=referees.referee_id """.format(x)

    cursor.execute(query)
    result = cursor.fetchall()

    l = ""
    for i in result:
        for j in i:
            l = j
    l = l.split()
    k = ""
    for i in l:
        if i != l[-1]:
            k += " " + i[0] + "."
        else:
            k = i + k
    print(k)

    cursor.close()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    connection.close()
