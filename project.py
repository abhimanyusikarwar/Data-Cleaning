import pandas as pd
import csv

df=pd.read_csv("final.csv")
print(df.shape)
del df["Constellation"]
del df["Spectral_type"]
del df["Brown_dwarf"]
del df["Mass"]
del df["Radius"]
del df["axis"]

print(df.shape)


print(list(df))
df.to_csv("main.csv")