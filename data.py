import pandas as pd 

def test_create_dataframe(dataframe, test_column):
    ''' A function where you can text if a pandas dataframe matchs 
    a list of columns, and the values in each column have the same python type. 
    At least 10 rows of data is required to get a positive response. '''
    if sorted(list(dataframe.columns)) == sorted(test_column) and df.equals(df.dtypes) and dataframe.shape[0]>=10:
        return True
    return False

if __name__ == '__main__':
    df = pd.read_csv('https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD') #import the data 
    df = df.head(10) # only fetch first 10 rows for testing 
    test_column = df.columns.tolist() # get the list of columns 
    print(test_create_dataframe(df, test_column)) # print result 
    
