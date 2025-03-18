import pandas as pd

# QUESTION1
df = pd.read_csv("D:\Data science file\movies_data.csv")
# print(df)

# QUESTION2
# g = df.groupby("industry")
# print(g.size())

# QUESTION 3
def grouper(df,idx,colmn):
    if 1<=df[colmn].loc[idx]<=3.9:
        return "Poor"
    elif 4<=df[colmn].loc[idx]<=7.9:
        return "Average"
    elif 8<=df[colmn].loc[idx]<=10:
        return "Good"
    else:
        return "others"
    

g = df.groupby(lambda idx: grouper(df, idx, "imdb_rating"))

for key,d in g:
    print("key", key)
    print("data", d, "\n")
