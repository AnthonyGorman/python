# this file ultimately replaces the Name in the Physician table from bogusData.csv
# with a Physician ID

import pandas as pd 



df = pd.read_csv('Physicians.csv')

# first create a hashmap

# create a hash map for a string: LastName Firstname to a Physician ID
physician_map = {}

for index, row in df.iterrows():
    key = row['LastName'] + ', ' + row['FirstName']
    physician_map[key] = row['PhysicianID']

df = pd.read_csv('Patients.csv')

# create a hash map for a string: FirstName LastName to a Patient ID
patient_map = {}

for index, row in df.iterrows():
    key = row['FirstName'] + ' ' + row['LastName']
    patient_map[key] = row['PatientID']

df = pd.read_csv('bogusData.csv')
newDF = pd.DataFrame(columns=['PhysicianID', 'PatientID'])

for index, row in df.iterrows():
    physKey = row['Physicians']
    patKey = row['Patients']
    physID = physician_map[physKey]
    patID = patient_map[patKey]
    newDF = newDF._append({'PhysicianID': physID, 'PatientID': patID}, ignore_index=True)

newDF.to_csv('IDs.csv', index=False)