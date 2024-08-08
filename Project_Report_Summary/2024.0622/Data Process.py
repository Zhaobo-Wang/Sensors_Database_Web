# 数据清洗 （处理缺失值）
import pandas as pd 
#创建包含温度和湿度数据的字典，其中包含一些缺失值（None）
data = {
    'Temperature': [28.5,30.1,None,29.2,25.7],
    'Humidity': [56,None,54,55,53]
}

df = pd.DataFrame(data) #将字典转换为DataFrame
df_cleaned = df.dropna() #删除包含缺失值的行
df_filled = df.fillna(df.mean()) #用每列的均值填充缺失值
print(df)
print(df_cleaned)
print(df_filled)



# 格式转换 （将时间字符串改成日期格式）
import pandas as pd 
#创建包含时间戳字符串的字典
data = {
    'Timestamp': ['2024-06-21 11:24:32','2024-06-21 11:24:33','2024-06-21 11:24:34']
}

df = pd.DataFrame(data) #将字典转换为DataFrame
df['Timestamp'] = pd.to_datetime(df['Timestamp']) #使用Pandas的to_datetime函数将字符串格式的时间戳转换为日期时间对象
print(df)



# 数据标准化
import pandas as pd
#创建包含摄氏温度和华氏温度数据的字典
data = {
    'Temp_c': [28.5, 30.1, 29.2, 28.9],
    'Temp_f': [83.3, 86.2, 84.6, 84.0]
}
df = pd.DataFrame(data) #将字典转换为DataFrame
df['Temp_f_in_c'] = (df['Temp_f'] - 32) * 5/9 #使用公式将华氏温度转换为摄氏温度并添加到新列
print(df)



# 基本的数据分析：平均值，中位数，标准差standard deviation
import pandas as pd
#创建一个数据字典，其中包含温度和湿度的数据
data = {
    'Temp_c': [28.5, 30.1, 29.2, 28.9],
    'Temp_f': [83.3, 86.2, 84.6, 84.0],
    'Humidity': [56,55,57,54]
}

#将数据字典转换为一个Pandas数据框
df = pd.DataFrame(data)

# 计算温度湿度的平均值
temp_mean = df['Temp_c'].mean()
humidity_mean = df['Humidity'].mean()
print('temp_mean =',temp_mean)
print('humidity_mean =',humidity_mean)

# 计算温度湿度的中位数
temp_median = df['Temp_c'].median()
humidity_median = df['Humidity'].median()
print('temp_median =',temp_median)
print('humidity_median =',humidity_median)

# 计算温度湿度的标准差
temp_std = df['Temp_c'].std()
humidity_std = df['Humidity'].std()
print('temp_std =',temp_std)
print('humidity_std =',humidity_std)


# 数据转换 （可以添加新的计算列，合并列等等）
import pandas as pd
#创建一个数据字典，其中包含温度和湿度的数据
data = {
    'Temp_c': [28.5, 30.1, 29.2, 28.9],
    'Temp_f': [83.3, 86.2, 84.6, 84.0],
    'Humidity': [56,55,57,54]
}

df = pd.DataFrame(data) #将数据字典转换为一个Pandas数据框
mean_temperature = df['Temp_c'].mean() #计算摄氏温度的平均值
df['High_Temp'] = df['Temp_c'] > mean_temperature 
#创建一个新列'High_Temp'，值为Temp_c是否高于平均值

print(mean_temperature)
print(df)


# 直接处理大批量的数据
"""
import pandas as pd

file_path = '.....' # 定义Excel文件的路径
df = pd.read_excel(file_path) #从指定路径读取Excel文件，并将其内容加载到一个Pandas数据框中
df = pd.DataFrame(data) #创建一个数据字典，其中包含温度和湿度的数据

mean_temperature = df['Temp_c'].mean() #计算摄氏温度的平均值
df['High_Temp'] = df['Temp_c'] > mean_temperature #创建一个新列'High_Temp'，值为Temp_c是否高于平均值
df.to_excel('...', index = False) #将更新后的数据框保存到一个新的Excel文件中，不包含索引

"""