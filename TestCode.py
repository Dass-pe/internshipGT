import pandas as pd
churn_data = pd.DataFrame({'CustomerId': [1,2,3,4,5,6,7,8,9,10],
                           'Gender': ['M', 'M', 'M', 'M', 'M', 'M', 'F', 'F', 'F', 'F'],
                           'Churn': [0,0,0,0,1,1,0,0,0,1],
                           'Age': [35, 67, 55, 41, 76, 65, 89, 55, 25, 32]})

aggmap = {'Age': 'mean',
       'Churn': 'sum'}

print(churn_data.groupby(['Gender']).agg(aggmap))
print(churn_data.head())
