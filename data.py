import pandas as pd 

df = pd.read_csv('https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD') #import the data 
df = df.head(100) # only fetch first 10 rows for testing 

def test_datatype(df):
    ''' Test if all columns have values of the correct type''' 
    columns = list(df)
    for name in columns:
        try: 
            tp = (df[name].map(type) == type(df[name].iloc[1].item())).any().tolist()
        except AttributeError:
            tp = (df[name].map(type) == type(df[name].iloc[1])).any().tolist() 
    return tp


def test_column_names(df):
    ''' The dataframe has the expected columns '''
    df_columns = sorted(df.columns.tolist())
    df_checklist = ['trip_id',
        'starttime',
        'stoptime',
        'bikeid',
        'tripduration',
        'from_station_name',
        'to_station_name',
        'from_station_id',
        'to_station_id',
        'usertype',
        'gender',
        'birthyear']
    if df_columns == sorted(df_checklist):
        return True 

def test_nan_values(df):
    ''' There are no nan values '''
    return df.notnull().values.any()

def test_least_row_counts(df):
    ''' The dataframe has at least one row '''
    return df.shape[0]>=1

if __name__ == '__main__':
     df = pd.read_csv('https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD') #import the data 
     df = df.head(100) # only fetch first 100 rows for testing 
     print(test_column_names(df) & test_datatype(df) & test_least_row_counts(df) & test_nan_values(df))
    
