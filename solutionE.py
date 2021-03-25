import sqlite3

filename = input()
condition1 = input()
condition2 = input()
field = input()

conn = sqlite3.connect(filename)

query = f'''
SELECT condition FROM Talks
WHERE {condition1} AND {condition2}
ORDER BY {field}
'''

cur = conn.cursor()
for row in cur.execute(query):
    print(row[0])
cur.close()
