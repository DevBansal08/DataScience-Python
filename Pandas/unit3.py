import pandas as pd

def standard_curr(curr):
    if curr == "$$" or curr == "Dollars":
        return "USD"
    return curr

df_movies = pd.read_excel("D:\movies_db.xlsx" , "movies")
df_financials = pd.read_excel("D:\movies_db.xlsx" , "financials" , converters= {
    "currency" : standard_curr
})

print(df_financials.head(4))

df_merged = pd.merge(df_movies,df_financials, on= "movie_id")





