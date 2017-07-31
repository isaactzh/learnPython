#database design
#connections between each table
#do not put the same string data in twice, use a relationship instead
#when there is on thing in the "real world" there should be one copy of that in the database
#primary key, like a unique ID
#foreign key, start point of the arrow and points to another table
#logical key, unique thing that we might use to look up this row from the outside world


#CREATE TABLE Genre(
#	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#	name TEXT
#	)

#insert into Artist(name) values('Led Zepplin')
"""
insert into Track(title, rating, len, count, album_id,genre_id)
	values('Black Dog',5,297,0,2,1);
insert into Track(title, rating, len, count, album_id,genre_id)
	values('Stairway',5,482,0,2,1);
insert into Track(title, rating, len, count, album_id,genre_id)
	values('About to Rock',5,313,0,1,2);
insert into Track(title, rating, len, count, album_id,genre_id)
	values('Who Made WHo',5,207,0,1,1);
"""

"""
Reconstructing Data with JOIN
-Relational Power: removing the replicated data and replace with references to a single
    copy of each bit of data: can read through very quickly, even for very large amounts
    of data, linked by the foreign keys
-The JOIN Operation: links across several tables as part of a select Operation
                     you must tell the JOIN how to use the keys that make the
                     connection between the tables using an ON clause
ex: select Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id
    select Track.tltle, Genere.name from Track join Genre on Track.genre_id = Genre.id

Work example:"""
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None :
        continue

    print(name, artist, album, count, rating, length)
	#if the artist is already there, ignore it
    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    #get the id of the artist
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ? )''',
        ( name, album_id, length, rating, count ) )

    conn.commit()
