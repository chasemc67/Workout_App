import sqlite3
from Person import Person
import datetime

def insertSampleData():
      conn = sqlite3.connect('people.db')

      dob = datetime.datetime(1995,3,22)
      testDate = datetime.datetime(2017,1,21)

      #conn.execute("INSERT INTO PEOPLE (ID,NAME,PHONE,DATEOFTEST,GENDER,DOB,HEARTRATE,BLOODPRESSURE,HEIGHT,WEIGHT) VALUES (1, 'Paul', '780-700-1070', testDate, 'male',dob, 100, 200, 300, 400)")
      conn.execute("INSERT INTO PEOPLE VALUES (1, 'Bill', '780-700-1070', 'today', 'male', 'a while ago', 100, 200, 300, 400)")
      conn.execute("INSERT INTO PEOPLE VALUES (2, 'Jim', '780-700-1070', 'today', 'male', 'a while ago', 100, 200, 300, 400)")
      conn.execute("INSERT INTO PEOPLE VALUES (3, 'James', '780-700-1070', 'today', 'male', 'a while ago', 100, 200, 300, 400)")
      conn.execute("INSERT INTO PEOPLE VALUES (4, 'Bob', '780-700-1070', 'today', 'male', 'a while ago', 100, 200, 300, 400)")

      conn.commit()
      conn.close()