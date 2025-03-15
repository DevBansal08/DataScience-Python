import pandas as pd


#Question1
df = pd.read_csv("D:\movies_data.csv")
# print(df.head(4))

#Question2
df["year_classify"] = df["release_year"].apply(lambda x : "Before 2000" if x <2000 else "After 2000")
print(df)

#Question3

df.to_csv("Final_name.csv", columns = ["movie_id","budget", "revenue", "year_classify"], index =False)