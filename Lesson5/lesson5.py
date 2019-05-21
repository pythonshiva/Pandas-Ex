#Stacking and unstacking functions
import pandas as pd

#Our small dataset
d = {'one':[1,1], 'two': [2,2]}
i = ['a', 'b']

#Form DataFrame
df = pd.DataFrame(data= d, index=i)
print(df)