import pandas as pd
df = pd.read_csv(r"D:\Data science file\weather_by_cities.csv")
# g = df.groupby("city")
# for city, data in g:
#     print("city", city)
#     print("max: ", data.temperature.max())

# print(g.get_group("mumbai"))

def grouper(df, idx, colmn):
    if 80 <= df[colmn].loc[idx]<=90:
        return "80-90"
    elif 50<= df[colmn].loc[idx] <=60:
        return "50-60"
    else:
        return "others"
    
g = df.groupby(lambda idx: grouper(df,idx,"temperature"))
for key,d in g:
    print("key:", key)
    print("data:", d)