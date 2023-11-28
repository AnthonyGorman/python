## create a bridge table

import pandas as pd 

# create the hash map for the service and its ID
service_map = {
    'Bathing': 1,
    'Feeding': 2,
    'Wound Dressing': 3,
    'Catheter Care': 4,
    'Feeding Tube Care': 5,
    'Insulin Injections': 6,
    'Injections (Other)': 7,
    'Exercise Therapy': 8,
    'Blood Tests': 9,
    'Blood Pressure Monitoring': 10,
    'Medicine Administration': 11,
    'General Hygiene': 12,
    'Surgical Prep': 13,
    'IV Maintenance': 14,
    'Breathing Treatments': 15
}

newDF = pd.DataFrame(columns=['ServiceID', 'ReferralID', 'FrequencyID'])
df = pd.read_csv('bogusData.csv')

# index 4 through 19 are the columns we want
selected_columns = df.iloc[:, 4:20]

for column_name, column_data in selected_columns.items():
    
    for i, value in column_data.items():

        if value == "X":
            ServiceID = service_map[column_name]
            FrequencyID = df.loc[i, 'FrequencyID']
            newDF = newDF._append({'ServiceID': ServiceID, 'ReferralID': i+1, 'FrequencyID': FrequencyID}, ignore_index=True)

newDF.to_csv('bridge.csv', index=False)
