import mysql.connector
import webbrowser
from django import template

try:
    conn = mysql.connector.connect(user='eyup', password='12345',
                              host='127.0.0.1',database='major_data',
                               auth_plugin='mysql_native_password')

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
    conn.close()

select_grads = """SELECT * FROM recent_grads"""
cursor = conn.cursor(dictionary=True)
cursor.execute(select_grads)
result = cursor.fetchall()
p = []
p.append("Major, P25, Median, P75")

for row in result:
    p.append(row["Major"]  + ", " + str(row["P25th"])  + ", " + str(row["Median"])  + ", " + str(row["P75th"]))
    #print(row["Major"])
    #p.append(row["P25th"])
    #print(row["P25th"])
    #p.append(row["Median"])
    #print(row["Median"])
    #p.append(row["P75th"])
    #print(row["P75th"])
    
print(p)

if(conn.is_connected()):
    cursor.close()
    conn.close()
    print("MySQL connection is closed.")    


def major_data():
    return p