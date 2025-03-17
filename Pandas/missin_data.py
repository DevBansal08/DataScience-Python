import pandas as pd

df= pd.read_csv("D:\Data science file\weather_data.csv" )
# print(type(df.day))

df.set_index('day', inplace=True)
# METHOD1
# df.fillna(0,inplace = True)

# METHOD2
# df.fillna({
#     'temperature' : df.temperature.mean(),
#     'windspeed' : df.windspeed.mean(),
#     "event" : "No Event"
# }, inplace = True)

# METHOD3
# df.fillna(method = "ffill", inplace = True)

# METHOD4
# df=df.interpolate()

print(df)