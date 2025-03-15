import pandas as pd
df = pd.read_csv(r"C:\Users\DEV BANSAL\Downloads\yc_weather.csv")

print(df.shape)

print(df.describe())

print(df)

print(df.iloc[5])
print(df.info())
print(df.index)