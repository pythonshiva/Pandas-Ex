#Outliers
import pandas as pd
States = ['NY', 'NY', 'NY', 'NY', 'FL', 'FL', 'GA', 'GA', 'FL', 'FL']
data = [1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
idx1  = pd.date_range('1/1/2012', periods=10, freq="MS")
df1 = pd.DataFrame(data, index= idx1, columns=['Revenue'])
df1['State']=States
# print(df1)

# Create a second dataframe
data2 = [10.0, 10.0, 9, 9, 8, 8, 7, 7, 6, 6]
idx2 = pd.date_range('1/1/2013', periods=10, freq='MS')
df2 = pd.DataFrame(data2, index=idx2, columns=['Revenue'])
df2['State'] = States

# Combine dataframes
df = pd.concat([df1,df2])
print(df)

#Ways to calculate Outliers
#Average and Standard deviation are valid only for gaussian distribution
# make a copy of original df
newdf = df.copy()

newdf['x-Mean'] = abs(newdf['Revenue'] - newdf['Revenue'].mean())
newdf['1.96*std'] = 1.96*newdf['Revenue'].std()
newdf['Outlier'] = abs(newdf['Revenue'] - newdf['Revenue'].mean()) > 1.96*newdf['Revenue'].std()
print(newdf)

#Method-2
newdf = df.copy()
State = newdf.groupby('State')
newdf['Outlier'] = State.transform( lambda x: abs(x-x.mean()) > 1.96*x.std() )
newdf['x-Mean'] = State.transform( lambda x: abs(x-x.mean()) )
newdf['1.96*std'] = State.transform( lambda x: 1.96*x.std() )
print(newdf)