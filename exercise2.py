import pandas as pd

# QUESTION1
df = pd.read_csv(r"D:\Data science file\fruits_data.csv")
# print(df.shape)
# print(df.columns)

# QUESTION2
# new_df = df.fillna("-1")
# print(new_df)

# QUESTION3
df.fillna({
    "apple(1kg)": df["apple(1kg)"].mean(),
    "banana(1 dozen)": df["banana(1 dozen)"].mean(),
    "grapes(1kg)": df["grapes(1kg)"].mean(),
    "mango(1kg)": df["mango(1kg)"].mean(),
    "Water Melons(1)":"Not Available"
}, inplace=True)
print(df)