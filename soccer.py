import numpy
import pandas
import sqlite3

path = "C://Users//nicob//OneDrive//Dokumenter//Skole greier//Maskinlæring"
database = path + 'database.sqlite'

conn = sqlite3.connect(database)

tables = pandas.read_sql("""SELECT *
                        FROM sqlite_master
                        WHERE type='table';""", conn)
print(tables)