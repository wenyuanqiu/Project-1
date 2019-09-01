import pandas as pd

pickle_path = r'data\rawdata\oris.pkl'
oris = pd.read_pickle(pickle_path)
pickle_path = r'data\rawdata\data_years.pkl'
data_years = pd.read_pickle(pickle_path)
pickle_path = r'data\rawdata\offenses.pkl'
offenses = pd.read_pickle(pickle_path)
pickle_path = r'data\rawdata\state_abbrs.pkl'
state_abbrs = pd.read_pickle(pickle_path)
pickle_path = r'data\rawdata\cleareds.pkl'
cleareds = pd.read_pickle(pickle_path)
pickle_path = r'data\rawdata\actuals.pkl'
actuals = pd.read_pickle(pickle_path)

fbi_data = pd.DataFrame({'ori':oris,'year':data_years,'offense':offenses,'state':state_abbrs,'cleared':cleareds,'actual':actuals})

print(fbi_data.info())
fbi_data.to_csv(r'data\cleandata\fbi_data.csv')

fbi_data_p1 = fbi_data.iloc[0:1000000,:]
fbi_data_p2 = fbi_data.iloc[1000000:2000000,:]
fbi_data_p3 = fbi_data.iloc[2000000:3000000,:]
fbi_data_p4 = fbi_data.iloc[3000000:4000000,:]
fbi_data_p5 = fbi_data.iloc[4000000:5000000,:]
fbi_data_p6 = fbi_data.iloc[5000000:fbi_data.shape[0]:]

fbi_data_p1.to_csv(r'data\cleandata\fbi_data_p1.csv')
fbi_data_p2.to_csv(r'data\cleandata\fbi_data_p2.csv')
fbi_data_p3.to_csv(r'data\cleandata\fbi_data_p3.csv')
fbi_data_p4.to_csv(r'data\cleandata\fbi_data_p4.csv')
fbi_data_p5.to_csv(r'data\cleandata\fbi_data_p5.csv')
fbi_data_p6.to_csv(r'data\cleandata\fbi_data_p6.csv')

print(fbi_data_p5.shape)
print(fbi_data_p6.shape)
