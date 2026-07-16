# Pandas

import numpy as np
import pandas as pd

#* Creating a series
"""
Inside an array multiple datatypes are not stored.
But in series we can store multiple datatypes
"""
labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([40,50,60])
dictionary = {1 : 100,2 : 200,3 : 300}
print(pd.Series(labels))
print(pd.Series(my_list))
print(pd.Series(arr))
print(pd.Series(my_list,index = labels)) # we call the index points as labels only
print(pd.Series(arr,index = labels))     # and the data is called data points
print(pd.Series(dictionary))



#* Dataframes : combination of multiple series together

# Creation of Dataframes
datadict = {
    'Name' : ['Joyjeet','Akash','Rishab','Ayush'],
    'Age' : [18,24,19,32],
    'City' : ['New Delhi','Kolkata','Mumbai','Bengaluru'],
    'Salary' : [5000,1500,9000,2000]
}
df1 = pd.DataFrame(datadict)
print(df1)

datalist = [
    ['Joyjeet',18,'New Delhi',5000],
    ['Akash',24,'Kolkata',1500],
    ['Rishab',19,'Mumbai',9000],
    ['Ayush',32,'Bengaluru',2000]
]
df2 = pd.DataFrame(datalist)
colm = ['Name','Age','City','Salary']
print(df2)
df3 = pd.DataFrame(datalist,columns = colm)
print(df3)
print(df3['Name'])
print(df3[['Name','City']])

# Creating a new colm
df3['Designation'] = ['Economist','Engineer','Doctor','Businessman']
print(df3)

# Removing a colm both temporarily and permanently
print(df3.drop('Designation',axis = 1))     # Will remove it for the current execution only
print(df3)  # Designation will be shown here
print(df3.drop('Designation',axis = 1,inplace = True)) # Removes completely
print(df3)

# Removing a row
print(df3.drop(3,axis = 0)) # inplace = True works here as well

"""
axis = 0 horizontal drop
axis = 1 vertical drop
"""

# Showing a particular row or element
print("\"")
print(df2.loc[0])
print(df3.loc[0])
print(df3.loc[0,"Salary"])

# Selecting subsets of rows and colums
print(df3.loc[[0,1],["Name","City","Salary"]])
print(df3.loc[[2,3],["Name","City"]])

""" only those people whose age is more than 20 """
print(df3[df3["Age"] > 20])
print(df3[(df3["Age"] > 20) & (df3["Salary"] > 1800)])


#* Missing Data

# Finding missing data
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan],
    'D': [1, np.nan, np.nan, np.nan, 5]
}
df4 = pd.DataFrame(data)
print(df4)
print(df4.isna())
print(df4.isna().sum())
print(df4.isna().any())

# Removing missing data
df5 = df4.dropna()  # removes all row with even atleast 1 null value
print(df5)
df6 = df4.dropna(thresh = 3)    # removes the rows with less than threshold null values
print(df6)

# Filling missing data
df7 = df4.fillna(0) # replace all the null values with 0
print(df7)

values = {'A': 100,'B':200,'C':300,'D':400}
df8 = df4.fillna(value = values)
print(df8)

df9 = df4.fillna(df4.mean())
print(df9)


#* Merging, Joining and Concatenation of 2 dataframes

# Merging of 2 DataFrames
employees = pd.DataFrame({              # dataframe 1
    'employee_id': [1, 2, 3, 4, 5, 6],
    'name': ['Virat', 'Rohit', 'Peter', 'Dhoni', 'ABD', 'Ishan'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Sales']
})
salaries = pd.DataFrame({               # dataframe 2
    'employee_id': [1, 2, 3, 6, 7],
    'salary': [60000, 80000, 65000, 70000, 90000],
    'bonus': [5000, 10000, 7000, 8000, 12000]
})
print(employees)
print(salaries)

a = pd.merge(employees,salaries)
print(a)
b = pd.merge(employees,salaries, on= 'employee_id')
print(b)
"""
a and b have same value.
on= is used to merge the dataframe based on the common column.
Since there is only one common column so on= is not required
"""
c = pd.merge(employees,salaries, on= 'employee_id', how='inner')
print(c)
d = pd.merge(employees,salaries, on= 'employee_id', how='outer')
print(d)
e = pd.merge(employees,salaries, on= 'employee_id',how= 'left')
print(e)
f = pd.merge(employees,salaries, on= 'employee_id',how='right')
print(f)
"""
how= inner is by default even if i dont add that at the end.
thus a,b and c have same outputs.
inner means merges using the common values of the common rows.
outer means merges all the values of common column and leave the value 'NaN' wherever ther is no value.
left means merges the left value of the two dataframe provided.
right means merges the right value of the two dataframe provided.
"""

# Concatenation of 2 DataFrames
df10 = pd.DataFrame({
    'A' : ['A0','A1','A2'],
    'B' : ['B0','B1','B2'],
    'C' : ['C0','C1','C2']
})
df20 = pd.DataFrame({
    'A' : ['A3','A4','A5'],
    'B' : ['B3','B4','B5'],
    'C' : ['C3','C4','C5']
})
print(df10)
print(df20)
print(pd.concat([df10,df20]))   # concatenation on the basis of columns
print(pd.concat([df10,df20],axis=1)) # concatenation on the basis of rows


# Joining 2 DataFrames
df11 = pd.DataFrame({
    'name':['Alice','Bob','Charlie']
}, index=[1,2,3])
df12 = pd.DataFrame({
    'score':[85,90,93]
}, index=[2,3,4])
print(df11)
print(df12)
print(df11.join(df12))
print(df12.join(df11))

#* groupby and Aggregation
data2 = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Store': ['S1', 'S1', 'S2', 'S2', 'S1', 'S2', 'S2', 'S1'],
    'Sales': [100, 200, 150, 250, 120, 180, 200, 300],
    'Quantity': [10, 15, 12, 18, 8, 20, 15, 25],
    'Date': pd.date_range('2023-01-01', periods=8)
}

df21 = pd.DataFrame(data2)
print(df21)

# group by category and calc the sum of sales
df22 = df21.groupby('Category') # Just categorises A and B
print(df22)
for i,j in df22:
    print(i)
    print(j)

df23 = df21.groupby('Category')['Sales'].sum() # provides sum of sales for both the categories
print(df23)

# group by stores and calc the sum of sales
df24 = df21.groupby('Store')['Sales'].sum()
print(df24)

# group by multiple columns and calc total sales
df25 = df21.groupby(['Category','Store'])['Sales'].sum()
df26 = df21.groupby(['Store','Category'])['Sales'].sum()
print(df25)
print(df26)


# Aggregation
"""mean,median,mode,var,std,min,max,count"""
df27 = df21['Sales'].mean()
df28 = df21['Sales'].median()
df29 = df21['Sales'].mode()
print(df27)
print(df28)
print(df29)
df30 = df21['Sales'].agg(['mean','median','sum','var','min','max','std'])
print(df30)
""" mode dont work inside .agg() because it returns multiple values"""

#* Pivot Tables
# Creation of Pivot Tables
data3 = {
    'Date': pd.date_range('2023-01-01', periods=20),
    'Product': ['A', 'B', 'C', 'D'] * 5,
    'Region': ['East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West',
               'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
    'Sales': np.random.randint(100, 1000, 20),
    'Units': np.random.randint(10, 100, 20),
    'Rep': ['John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary',
            'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice']
}
df31 = pd.DataFrame(data3)
print(df31)

pivot1 = pd.pivot_table(df31,values='Sales',index='Region',columns='Product')       # mean asbe as agg = mean by default
print(pivot1)

pivot2 = pd.pivot_table(df31,values='Sales',index='Region',columns='Product',aggfunc='median')
print(pivot2)

pivot3 = pd.pivot_table(df31,values=['Sales','Units'],index='Region',columns='Product')
print(pivot3)

# Cross Tabs
"""same as pivot table. but instead of agg we use count functions"""
ct1 = pd.crosstab(df31['Region'],df31['Product'])
print(ct1)


#* Operations
df32 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
})
print(df32)
print(df32.shape)
print(df32.columns)
print(df32.info())
print(df32.describe())
print(df32['A']+10)

# Squaring all the element in the colm B

def square(x):
    return x**2
def cube(x):
    return x**3

print(df32['B'].apply(square))  # only provides required output without changing th dataframe


df32['B'] = df32['B'].apply(square) # now the DataFrame will store the changed value of B
print(df32)

df32['D'] = df32['A'].apply(cube)   # creates a new column D
print(df32)
