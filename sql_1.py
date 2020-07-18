import sqlite3

# create new database
conn = sqlite3.connect(r'.\sql_db\Demo_table.db')
print('Database created.')

# create Cursor to execute queries
cur = conn.cursor()

# create table in database
cur.execute('''                
                CREATE TABLE IF NOT EXISTS Customer(
                User_ID INTEGER PRIMARY KEY NOT NULL,
                Product_ID INTEGER NOT NULL,
                Name TEXT NOT NULL,
                Gender TEXT NOT NULL,
                AGE INTEGER NOT NULL,
                CITY TEXT);                
                ''')

# Insert 1 value
cur.execute('''Insert Into Customer 
            ('User_ID','Product_ID','Name','Gender','AGE','CITY') 
            Values 
            (1007, 3, 'Princess Diana', 'Female', 28, 'Amazons');''')

# Insert multiple values into table at once
customers = [(1008, 2, 'John Wick', 'Male', 32, 'New York'),
         (1009, 1, 'Tony Stark', 'Male', 35, 'New York'),
         (1010, 3, 'Gordon Ramsey', 'Male', 38, 'London')
            ]
cur.executemany('Insert Into CUSTOMER Values (?,?,?,?,?,?)', customers)

# Fetch all rows of query result
cur.execute('SELECT * FROM CUSTOMER;').fetchone()

# iterate over the rows 
for row in cur.execute('SELECT Name FROM CUSTOMER;'):
    print(row)

# Fetch all rows of query result which returns a list
cur.execute('SELECT * FROM CUSTOMER;').fetchall()

# save changes
conn.commit()
print('Changes saved.')

# close database connection
conn.close()
print('Connection closed.')