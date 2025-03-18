import pandas as pd

india_weather = pd.DataFrame({
    "city": ["mumbai", "delhi","banglore"],
    "temperature": [32,45,30],
    "humidity":[80,60,78]

} )
us_weather = pd.DataFrame({
    "city": ["nyc", "chicago","orlando"],
    "temperature": [21,14,35],
    "humidity":[68,65,75]

} )
df = pd.concat([india_weather,us_weather], keys =["india","us"])
print(df)