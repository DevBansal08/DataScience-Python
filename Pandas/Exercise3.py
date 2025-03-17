import pandas as pd

# QUESTION1
df = pd.read_csv(r"D:\Data science file\food_db.csv")
# print(df.shape)
# print(df)

# QUESTION2
# new_df=df.replace(["5%","10%"], "13%")
# print(new_df)

# QUESTION3
new_df = df.replace(["Average","Good","Very Good","Excellent"],[1,2,3,4])
print(new_df)