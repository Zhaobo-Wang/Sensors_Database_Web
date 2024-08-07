import pandas as pd
import mysql.connector
import numpy as np

# 连接到 MySQL 数据库
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='jimbo991016',
    database='sensor'
)

cursor = connection.cursor()  # 创建一个游标对象，用于执行 SQL 语句

file_path = 'D:/McMaster/2024_Summer/Project_with_Junbo/Updated_DHT11_Data_Collection_v5.xlsx'  # 读取 Excel 文件中的数据
sensors = pd.read_excel(file_path, sheet_name='Sensors')  # 读取名为'Sensors'的表
measurements = pd.read_excel(file_path, sheet_name='Measurements')  # 读取名为'Measurements'的表

# 打印列名以进行检查
print("Sensors DataFrame columns:", sensors.columns)
print("Measurements DataFrame columns:", measurements.columns)

# 删除重复的主键记录
sensors = sensors.drop_duplicates(subset=['Sensor Key'])
measurements = measurements.drop_duplicates(subset=['ID'])

# 替换 `nan` 值为 `None`
sensors = sensors.replace({np.nan: None})
measurements = measurements.replace({np.nan: None})

try:
    for index, row in sensors.iterrows():  # 遍历 Sensors 数据框的每一行，插入数据到 Sensors 表，如果主键重复则忽略插入
        sql = "INSERT IGNORE INTO Sensors (Sensor_ID, Location, Sensor_Key) VALUES (%s, %s, %s)"  # 定义插入语句，使用 INSERT IGNORE 避免主键重复错误
        params = (row['Sensor ID'], row['Location'], row['Sensor Key'])  # 从当前行提取数据
        print(f"Executing SQL: {sql} with params {params}")  # 打印即将执行的 SQL 语句和参数，便于调试
        cursor.execute(sql, params)  # 执行插入操作

    for index, row in measurements.iterrows():  # 插入数据到 Measurements 表，如果主键重复则忽略插入
        sql = """INSERT IGNORE INTO Measurements (ID, Temperature, Humidity, Timestamp, TimeZone, Temperature_Change_Rate, 
                   Humidity_Change_Rate, Comfort_Index, Location, Sensor_ID, Comfort_Level) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""  # 定义插入语句，使用 INSERT IGNORE 避免主键重复错误
        
        params = (row['ID'], row['temperature'], row['humidity'], row['timestamp'], row['timezone'], 
                  row['temperature Change Rate'], row['humidity_change_rate'], row['comfort_index'], row['location'], row['sensor_id'], row['comfort_level'])  # 从当前行提取数据
        print(f"Executing SQL: {sql} with params {params}")  # 打印即将执行的 SQL 语句和参数，便于调试
        cursor.execute(sql, params)  # 执行插入操作

    connection.commit()  # 提交更改到数据库，确保所有插入操作被保存

except mysql.connector.Error as err:  # 捕捉并打印数据库操作错误
    print("Error: {}".format(err))

finally: 
    cursor.close()  # 关闭游标
    connection.close()  # 关闭连接
