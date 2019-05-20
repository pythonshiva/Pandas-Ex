#In this chapter we will work on some basics
import pandas as pd
#Create some data
some_list = list(range(0,10))

#Lets add this list to the DF
df = pd.DataFrame(some_list)

#We can change the name of the column
df.columns = ['Numbers']

#If we wanted to add some extra columns to the df
#This will add a column named "five" with values of 5
df['Five']=5

#If we want to duplicate a column
df['dFive']=df['Five']

#We can change the index values
index_vals = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df.index = index_vals
print(df.loc['i'])
print('____________')

#Fetching multiple values
print(df.loc['a':'d']) #Here we will get details from a to d(d also included)

#If we use integer based location we will get the values as list slice
print(df.iloc[0:3]) #Here we will get only 3 values(a,b,c and d is not included)

#We can also fetch the data with the column names
print(df['Numbers'])
print(df[['Numbers', 'Five']])

#Fetch the Numbers column from the data in an index range
print(df.loc[df.index[0:3], 'Numbers'])
print(df.loc[df.index[5:], ['Numbers', 'Five']])

#Fetch top N records(default is 5)
print(df.head())

#Fetch last N records default is 5
print(df.tail())

#Delete a column
del df['dFive']

