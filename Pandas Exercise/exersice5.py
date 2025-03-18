import pandas as pd

# QUESTION 1
df_movies= pd.read_csv(r"D:\Data science file\movies.csv")
df_financials= pd.read_csv(r"D:\Data science file\financials.csv")
df_languages= pd.read_csv(r"D:\Data science file\movies.csv")

# print(df_movies.head(3))

# QUESTION 2
df_new_movies = pd.read_csv(r"D:\Data science file\new_movies.csv")
df_movies= pd.concat([df_movies,df_new_movies], ignore_index=True)
# print(df_movies)

# QUESTION3
df_movies = pd.merge(df_movies,df_languages,on= "language_id", how="inner")
# print(df_movies.head(5))

# QUESTION4
df_movies= pd.merge(df_movies,df_financials, on= "movie_id", how="left")
# print(df_movies.tail(5))

# Question5
df_movies.to_csv("final_complete_data.csv", columns=["movie_id","title","lang_name","budget","revenue", "currency"], index=False)