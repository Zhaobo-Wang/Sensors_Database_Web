import pandas as pd
data = [1,2,3,4,5]
series = pd.Series(data) #pd.series的s是大写
print(series)


import pandas as pd
data = {
    'name':['alice','bob','charlie'],
	'age':[25,30,35],
	'city':['new york','los angeles', 'chicago']
}
df = pd.DataFrame(data) #dataframe的d大写	
#print(df)

df_filtered = df[df['age']>30] #一个是filter age必须得大于30
print(df_filtered)

df_sorted = df.sort_values(by='age') #一个是sort
print(df_sorted)
