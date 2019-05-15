import numpy as np
import pandas as pd


#Create seed
np.random.seed(111)

#Generate some random test data
def create_data_set(Number=1):
    output = []

    for _ in range(Number):
        #Generate weekly date range
        rng = pd.date_range(start='1/1/2016', end='31/3/2019', freq='W-MON')

        #Create some random data
        data = np.random.randint(low=25, high=1000, size=len(rng))

        #Status pool
        status = [1,2,3]

        random_status = [status[np.random.randint(low=0, high=len(status))] for one in range(len(rng))]

        #States pool
        states = ['AP', 'ts', 'KA', 'MP', 'OD', 'KL']
        #Make random list of sates
        random_states  =[states[np.random.randint(low=0, high=len(states))] for one in range(len(rng))]
        output.extend(zip(random_states, random_status, data, rng))
    return output


#Create the data set
# data_set = create_data_set(4)
# df = pd.DataFrame(data=data_set, columns=['State', 'Status', 'CustomerCount', 'StatusDate'])
# print(df.info())

#Save the data to the excel file
# df.to_excel('lesson3.xlsx', index=False)

#Preparing Data, We will follow the following rules to prepare here
#Make sure the state column is all in upper case
#Only select records where the account status is equal to "1"
#Merge (AP and TS) to AP in the state column
#Remove any outliers (any odd results in the data set)

df =pd.read_excel('lesson3.xlsx', 0, index_col='StatusDate')
print(df.dtypes)
# print(df['State'].unique())

#1. Clean the States column, Converting into upper case
df['State']=df.State.apply(lambda x: x.upper())
# print(df['State'].unique())

#2.Only grap where Status equals to 1
mask = df['Status']==1
df = df[mask]

#3. Find all the records with the StateTS with df.State=='TS'
#And replace all those records with AP df.State[df.State == 'TS'] = 'AP'
mask = df.State == 'TS'
df['State'][mask] = 'AP'
print(df.State.unique())

