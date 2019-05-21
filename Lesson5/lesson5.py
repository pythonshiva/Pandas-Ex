#Stacking and unstacking functions
import pandas as pd

#Our small dataset
d = {'one':[1,1], 'two': [2,2]}
i = ['a', 'b']

#Form DataFrame
df = pd.DataFrame(data= d, index=i)
# print(df)

#Bring the column and place them in the index
stack = df.stack()
print(stack)
#now it became the multi level index
# print(stack.index)

unstack = df.unstack()
print(unstack)
print(unstack.index)

#We can also flip the column names with the index using Transpose
transpose = df.T
print(transpose)
