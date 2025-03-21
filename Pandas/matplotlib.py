import pandas as pd

df= pd.read_excel("D:\Data science file\linechart.xlsx")


from matplotlib import pyplot as plt
a = plt.plot(df["Quarter", df["Fridge"]])
print(a)