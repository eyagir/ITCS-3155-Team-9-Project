from django.shortcuts import render
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

# data for index.html
select_grads = """SELECT * FROM recent_grads"""
cursor = conn.cursor(dictionary=True)
cursor.execute(select_grads)
result = cursor.fetchall()
p = []
p.append("Major, P25, Median, P75")
for row in result:
    p.append(row["Major"]  + ", " + str(row["P25th"])  + ", " + str(row["Median"])  + ", " + str(row["P75th"]))
    
# data for hpay.html
select_popular = """SELECT * FROM recent_grads ORDER BY Median"""
cursor.execute(select_popular)
result = cursor.fetchall()
r = []
for row in result:
    r.append(row["Major"]  + ", " + str(row["P25th"])  + ", " + str(row["Median"])  + ", " + str(row["P75th"]))

# data for popular.html
selct_popular = """SELECT * FROM recent_grads ORDER BY Total"""
cursor.execute(select_popular)
result = cursor.fetchall()
x = []
for row in result:
    x.append(row["Major"]  + ", " + str(row["P25th"])  + ", " + str(row["Median"])  + ", " + str(row["P75th"]))


def index(request):
    return render(request, 'index.html', {"list": p})

def ctool(request):
    return render(request, 'ctool.html')

def hpay(request):
    return render(request, 'hpay.html', {"list": r})

def popular(request):
    return render(request, 'popular.html', {"list": x})

if(conn.is_connected()):
     cursor.close()
     conn.close()
     print("MySQL connection is closed.")  