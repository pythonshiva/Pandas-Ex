#Pandas lesson2
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt

#Define some initial set of names
names = ['Siva', 'Vamsi', 'Naga', 'Aravindan', 'Mahesh']

#Make random list of 1000 names using above list
random_names = [names[random.randint(low=0, high=len(names))] for one in range(1000)]

#Number of births per the name in the year 1990 in different locations
births = [random.randint(low=0, high=100) for one in range(1000)]

#Now form the baby data set with the random_names and births
baby_dataset = list(zip(random_names, births))

df = pd.DataFrame(data = baby_dataset, columns= ['Names', 'Births'])

#Export the data frame to the csv file
df.to_csv('Births1990.csv', header=False, index=False)

#now we try reading the data from the csv file
df = pd.read_csv('Births1990.csv', names=['Names', 'Births'])

#To find the unique values in the names column
unique_names = df['Names'].unique()
# print(unique_names)

#We can describe the df object 
# print(df['Names'].describe())

#As one name is reccuring multiple times we can actually group these
#Creating the groupby obejct
df = df.groupby('Names')
print(df)

#Apply the sum fucntion to the group by object
df  = df.sum()
# print(df)

#To get the highest birth rate with the names
#Method-1
sorted_df = df.sort_values(['Births'], ascending=False)
# print(sorted_df.head(1))

#Method-2
print(df['Births'].max())

#Presenting the data
ax = df['Births'].plot(kind='bar', title= "No of births with name in the year 1990", legend=True)
ax.set_xlabel('Names')
ax.set_ylabel('Births')
plt.show()
