import sqlite3

conn = sqlite3.connect('movies.db')
c = conn.cursor()

# create a table
c.execute(""" CREATE TABLE Movies (
            name text,
            actor text,
            actress text,
            director text,
            year_of_releases text)
""")

# insert 1 record to table
c.execute("""INSERT INTO Movies values(
            'Dr.Strange',
            'Benedict',
            'Elizebeth',
            'Bruce',
            '2021')
            """)

# insert many records to table
movie_list = [('KGF', 'Yash', 'Srinidhi', 'Sanjay', '2022'),
              ('Spiderman 2', 'Tom', 'Alia', 'Steven', '2019'),
              ('Spiderman 3', 'Tom', 'Natasha', 'Jonny', '2020')]

c.executemany("INSERT INTO Movies values(?,?,?,?,?)", movie_list)

# selecting all rows from Movies table
c.execute("SELECT * FROM Movies")
print(c.fetchall())

# selecting particular rows from Movies table
c.execute("SELECT * FROM MOVIES WHERE ACTOR = 'Yash'")
print(c.fetchall())

# commit a command
conn.commit()

# close the connection
conn.close()
