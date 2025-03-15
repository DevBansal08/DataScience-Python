import pandas as pd
df = pd.read_csv(r"C:\Users\DEV BANSAL\Downloads\yc_weather.csv")
# print(df['Temperature'].max())

# print(df["EST"][df["Events"]=="Rain"])

# df.fillna(0,inplace=True)
# print(df["WindSpeedMPH"].mean())

# print(df["EST"][df["Humidity"]==53])

# print(df.Temperature.max())

# print(df.Temperature.value_counts())

print(df[df.Temperature== 30])

