import mysql.connector

# เชื่อมต่อกับ MySQL
connection = mysql.connector.connect(
    host="localhost",         # หรือ IP Address ของ Server
    user="root",              # Username MySQL
    password="0609", # Password MySQL
    database="pysql1"     # ชื่อ Database ที่สร้างไว้
)

# ตรวจสอบการเชื่อมต่อ
if connection.is_connected():
    print("เชื่อมต่อสำเร็จ!")
else:
    print("เชื่อมต่อไม่สำเร็จ!")
