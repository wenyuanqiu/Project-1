import pandas as pd

data_year = pd.read_pickle(r'data\rawdata\offenders_by_sex\data_year.pkl')
female_count = pd.read_pickle(r'data\rawdata\offenders_by_sex\female_count.pkl')
male_count = pd.read_pickle(r'data\rawdata\offenders_by_sex\male_count.pkl')
offense_type_list = pd.read_pickle(r'data\rawdata\offenders_by_sex\offense_type_list.pkl')
unknown = pd.read_pickle(r'data\rawdata\offenders_by_sex\unknown.pkl')

fbi_offenders_by_age = pd.DataFrame({'data_year':data_year,
                                    'female_count':female_count,
                                    'male_count':male_count,
                                    'offense_type_list':offense_type_list,
                                    'unknown':unknown})

fbi_offenders_by_age.to_pickle(r'C:\Users\wenyu\Documents\GitHub\project_1\data\cleandata\fbi_offenders_by_sex.pkl')