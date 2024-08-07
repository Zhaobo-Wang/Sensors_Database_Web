import mysql.connector

# 连接到 MySQL 服务器
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jimbo991016",
    database="sensor_data"
)

# 创建游标对象
cursor = connection.cursor()

# 执行查询
cursor.execute("SELECT * FROM sensor_readings")

# 获取所有行
rows = cursor.fetchall()

# 输出行数据
for row in rows:
    print(row)

# 关闭连接
cursor.close()
connection.close()
