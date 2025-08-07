import sqlite3

conn = sqlite3.connect('C:/Users/birdc/source/repos/EliteVideo/db/movies.db')
cursor = conn.cursor()

# Create video table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Video (
    VID_NUM NUMERIC(8,0) PRIMARY KEY,
    VID_INDATE DATE,
    MOVIE_NUM NUMERIC(8,0)
)
''')

# Create price table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Price (
    PRICE_CODE NUMERIC(2,0) PRIMARY KEY,
    PRICE_DESCRIPTION VARCHAR(20),
    PRICE_RENTFEE NUMERIC(5,2),
    PRICE_DAILYLATEFEE NUMERIC(5,2)
)
''')

# Create movie table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Movie (
    MOVIE_NUM NUMERIC(8,0) PRIMARY KEY,
    MOVIE_TITLE VARCHAR(75),
    MOVIE_YEAR NUMERIC(4,0),
    MOVIE_COST NUMERIC(5,2),
    MOVIE_GENRE CHAR(20),
    PRICE_CODE NUMERIC(2,0),
    FOREIGN KEY (PRICE_CODE) REFERENCES Price(PRICE_CODE)
)
''')

# Create membership table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Membership (
    MEM_NUM NUMERIC(8,0) PRIMARY KEY,
    MEM_FNAME VARCHAR(30),
    MEM_LNAME VARCHAR(30),
    MEM_STREET VARCHAR(120),
    MEM_CITY VARCHAR(50),
    MEM_STATE CHAR(2),
    MEM_ZIP CHAR(5),
    MEM_BALANCE NUMERIC(10,2)
)
''')

# Create rental table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Rental (
    RENT_NUM NUMERIC(8,0) PRIMARY KEY,
    RENT_DATE DATE,
    MEM_NUM NUMERIC(8,0),
    FOREIGN KEY (MEM_NUM) REFERENCES Membership(MEM_NUM)
)
''')

# Create detail rental table
cursor.execute('''
CREATE TABLE IF NOT EXISTS DetailRental (
    RENT_NUM NUMERIC(8,0),
    VID_NUM NUMERIC(8,0),
    DETAIL_FEE NUMERIC(5,2),
    DETAIL_DUEDATE DATE,
    DETAIL_RETURNDATE DATE,
    DETAIL_DAILYLATEFEE NUMERIC(5,2),
    PRIMARY KEY (RENT_NUM, VID_NUM),
    FOREIGN KEY (RENT_NUM) REFERENCES Rental(RENT_NUM),
    FOREIGN KEY (VID_NUM) REFERENCES Video(VID_NUM)
)
''')


conn.commit()
conn.close()
print("Database schema initialized.")
