#relational databases
#relational datavases model data by storing rows and columns in tables.
#The power of the ralational database lies in its ability to efficiently retrieve
#data from those tables and in particular where there are multiple tables and realtionships
#between those tables involved in the query.
#Terminology:
    #Database: contains many tables
    #Relation(table): contains tuples and attributes
    #Tuples(row): a set of fields that generally represents an "obeject" like a person or a music disk
    #Attributes(column or field): one the possibly many elements of data corresponding to the
    #object represented by the row
#SQL: Structured Query Language: Language between the database and API
#our code talk to database application
#four basic function of SQL: CRUD, create, read, update, delete

##########################################################################

#using the database
#database model or database schema is the structure or format of a database.
#It is the application of a data model when used in conjunction with a database management system
#SQLite embedded database


#CREATE TABLE Users(
#    name VARCHAR(128),
#    email CARCHAR(128)
#)

#INSERT INTO Users(name, email)VALUES('Kristin','lcd@umich.edu')
#DELETE FROM Users WHERE email='ted@umich.edu'
#UPDATE Users SET name='Charles' WHERE email = 'csev@umich.edu'
#SELECT*FROM Users WHERE email='csev@umich.edu'
#SELECT*FROM Users ORDER BY email



#homework example:
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    (emailname, org) = email.split("@")
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
