import pandas as pd




data = {
    "EmployeeID": ["E001", None, "E003", "E004", "E005", "E006"],
    "Name": ["Ali", "Sara", "Ahmed", None, "Usman", "Fatima"],
    "Age": [25, None, 30, 28, None, 26],
    "Department": ["IT", "HR", None, "Finance", "IT", "HR"],
    "Salary": [50000, 60000, None, 55000, 70000, None],
    "JoiningDate": ["2021-01-01", "2020-05-10", None, "2019-07-15", "2022-03-20", "2021-11-11"]
}

df = pd.DataFrame(data)

print("🔹 Raw Data:")
print(df)


print("\n check missing values:")
print(df.isnull().sum())


df["Age"]=pd.to_numeric(df["Age"], errors="coerce")
df["Salary"]=pd.to_numeric(df["Salary"], errors="coerce")
df["JoiningDate"] = pd.to_datetime(df["JoiningDate"], errors="coerce")
df["JoiningDate"] = df["JoiningDate"].ffill()

#handle kryn ga missing values ko


df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
df["Name"]=df["Name"].fillna(df["Name"].mode()[0])
df["Department"]=df["Department"].fillna(df["Department"].mode()[0])
df=df.dropna(subset=["EmployeeID"])

print("\n Cleaned Data:")
print(df)


print("\nAverage Salary:", df["Salary"].mean())


print("\nSalary by Department:")
print(df.groupby("Department")["Salary"].mean())

print("\nOldest Employee:")
print(df.loc[df["Age"].idxmax()])

print("\n highest salary:")
print(df.loc[df["Salary"].idxmax()])


df_sorted=df.sort_values(["Salary"], ascending=False)
print(df_sorted)