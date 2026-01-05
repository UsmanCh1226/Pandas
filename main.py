import pandas as pd
 
data = {"Name": ["SpongeBob", "Patrick", "Squidward"],
        "Age": [30, 35, 50]}

df = pd.DataFrame(data)
 

#Add a new column
df["Job"] = ["Cook ", "NA", "Cashier"]

# Add a new row 
new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},f
                        {"Name": "Eugene", "Age": 60, "Job": "Manager" }],
                       index= ["Employee 4", "Employee 5"])
df = pd.concat([df, new_rows])


print(df)
