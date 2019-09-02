import pandas as pd

unknown = pd.read_pickle(r'data\rawdata\offenders_by_age\unknown.pkl')
range_0_9 = pd.read_pickle(r'data\rawdata\offenders_by_age\range_0_9.pkl')
range_10_19 = pd.read_pickle(r'data\rawdata\offenders_by_age\range_10_19.pkl')
range_20_29 = pd.read_pickle(r'data\rawdata\offenders_by_age\range_20_29.pkl')
range_30_39 = pd.read_pickle(r'data\rawdata\offenders_by_age\range_30_39.pkl')
range_40_49 = pd.read_pickle(r'data\rawdata\offenders_by_age\range_40_49.pkl')
range_50_59 = pd.read_pickle(r'data\rawdata\offenders_by_age\range_50_59.pkl')
range_60_69 = pd.read_pickle(r'data\rawdata\offenders_by_age\range_60_69.pkl')
range_70_79 = pd.read_pickle(r'data\rawdata\offenders_by_age\range_70_79.pkl')
range_80_89 = pd.read_pickle(r'data\rawdata\offenders_by_age\range_80_89.pkl')
range_90_99 = pd.read_pickle(r'data\rawdata\offenders_by_age\range_90_99.pkl')
data_year = pd.read_pickle(r'data\rawdata\offenders_by_age\data_year.pkl')
offense_type_list = pd.read_pickle(r'data\rawdata\offenders_by_age\offense_type_list.pkl')

fbi_offenders_by_age = pd.DataFrame({'unknown':unknown,
                                    'range_0_9':range_0_9,
                                    'range_10_19':range_10_19,
                                    'range_20_29':range_20_29,
                                    'range_30_39':range_30_39,
                                    'range_40_49':range_40_49,
                                    'range_50_59':range_50_59,
                                    'range_60_69':range_60_69,
                                    'range_70_79':range_70_79,
                                    'range_80_89':range_80_89,
                                    'range_90_99':range_90_99,
                                    'data_year':data_year,
                                    'offense_type_list':offense_type_list})

fbi_offenders_by_age.to_pickle(r'C:\Users\wenyu\Documents\GitHub\project_1\data\cleandata\fbi_offenders_by_age.pkl')