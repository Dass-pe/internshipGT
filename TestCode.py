import pandas as pd
churn_data = pd.DataFrame({'CustomerId': [1,2,3,4,5,6,7,8,9,10],
                           'Gender': ['M', 'M', 'M', 'M', 'M', 'M', 'F', 'F', 'F', 'F'],
                           'Churn': [0,0,0,0,1,1,0,0,0,1]})
print(churn_data.head())
