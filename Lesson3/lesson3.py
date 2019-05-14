import numpy as np
import pandas as pd


#Create seed
np.random.seed(111)

#Generate some random test data
def create_data_set(Number=1):
    output = []

    for _ in range(Number):
        #Generate weekly date range
        rng = pd.date_range(start='1/1/2017', end='31/3/2019', freq='W-MON')

        #Create some random data
        data = np.random.randint(low=25, high=1000, size=len(rng))

        #Status pool
        status = [1,2,3]

        random_status = [status[np.random.randint(low=0, high=len(status))] for one in range(len(rng))]

        #States pool
        states = ['AP', 'TN', 'KA', 'MP', 'OD', 'KL']
        #Make random list of sates
        random_states  =[states[np.random.randint(low=0, high=len(states))] for one in range(len(rng))]
        output.extend(zip(random_states, random_status, data, rng))
    return output


#Create the data set
data_set = create_data_set(4)
df = pd.DataFrame(data=data_set, columns=['States', 'Status', 'CustomerCount', 'StatusDate'])
print(df.info())

#Save the data to the excel file
df.to_excel('lesson3.xlsx', index=False)