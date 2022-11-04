import pandas as pd
df1 = pd.read_csv("wine-quality.csv")

df2 =df1.copy()

df3 = pd.concat([df1, df2])

df3.to_csv("wine-quality.csv", index=False)
