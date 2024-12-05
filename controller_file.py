import mysql.connector
from tabulate import tabulate
from dotenv import load_dotenv
import os

def main_sql(query):  # รับคำสั่ง SQL เป็นพารามิเตอร์
    load_dotenv()  # โหลดค่าจากไฟล์ .env
    mydb = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

    print("Connected to database:", mydb)
    mycursor = mydb.cursor()

    mycursor.execute(query)  # รันคำสั่ง SQL ที่ได้รับเป็นพารามิเตอร์

    myresult = mycursor.fetchall()  # ดึงข้อมูลทั้งหมดจากผลลัพธ์

    # แสดงผลในรูปแบบตาราง
    print(tabulate(myresult, headers=[i[0] for i in mycursor.description], tablefmt="pretty"))
