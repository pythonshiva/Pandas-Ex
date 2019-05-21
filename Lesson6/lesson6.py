#Group by function
import pandas as pd

#Lets take a small data set
d = {'one': [1,1,1,1,1],
     'two': [2,2,2,2,2],
     'letter': ['a', 'a', 'b', 'b', 'c']}
    
#Lets make the sample data into DataFrame
df = pd.DataFrame(d)
print(df)

#Now we can create a group object with the above DF
grp_obj = df.groupby('letter')

#Summing up the groupby obj
grp_sum = grp_obj.sum()
print(grp_sum)

#Grouping with two columns
letter_one = df.groupby(['letter', 'one']).sum()
print(letter_one)
print(letter_one.index)
#Note: When we are grouping with two columns those two will become
#the indexes, we can avoid these in the following way if we want
letter_one = df.groupby(['letter', 'one'], as_index=False).sum()
print(letter_one)
print(letter_one.index)