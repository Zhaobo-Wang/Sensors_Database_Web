import mysql.connector

# 连接到 MySQL 服务器
connection = mysql.connector.connect(
    host='localhost',  # MySQL服务器地址
    user='root',       # MySQL用户名
    password='jimbo991016', # MySQL密码
    database='sensor_data'  # 要查询的数据库名
)

# 创建游标对象
cursor = connection.cursor()

# 查询数据库中的所有表
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
print("Tables in sensor_data database:")
for table in tables:
    print(table[0])

# 查询 Sensors 表中的数据
print("\nData from Sensors table:")
cursor.execute("SELECT * FROM Sensors")
sensors_data = cursor.fetchall()
for row in sensors_data:
    print(row)

# 查询 Measurements 表中的数据
print("\nData from Measurements table:")
cursor.execute("SELECT * FROM Measurements")
measurements_data = cursor.fetchall()
for row in measurements_data:
    print(row)

# 关闭连接
cursor.close()
connection.close()
