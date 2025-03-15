import pandas as pd

df_movies = pd.read_excel("D:\movies_db.xlsx" , "movies")
df_financials = pd.read_excel("D:\movies_db.xlsx" , "financials")

df_merge = pd.merge(df_movies,df_financials, on = "movie_id")
print(df_merge)

df_merge.to_excel("movies_db.xlsx", sheet_name="db_merged", index=False)