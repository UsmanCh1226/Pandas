import pandas as pd

df = pd.read_csv("learning_pandas.csv", index_col="Name")

# SELECTION BY COLUMN
#print(df["Name"].to_string())
#print(df["Height"].to_string()) 
#print
#print(df[["Name", "Height", "Weight"]].to_string())

#SELECTION BY ROWS 
print(df.loc["Charizard": "Blastoise", ["Height", "Weight"]]) 
 