import pandas as pd

def load_df():
    df = pd.read_csv('food.csv')
    return df

def clean_df(df):
    # remove lines with null values
    df.dropna(inplace = True)

    # group non unique values by category getting values as mean
    df= df.groupby(['Category'], as_index = False).mean()

    # clean Data. Major Minerals. and Vtamins. from columns title
    column_headers = df.columns.values.tolist()
    for column_header in column_headers:
        new_header = column_header.split(".")[-1]
        df.rename(columns={column_header: new_header}, inplace=True)
    
    # drop irrelevant columns
    df.drop(['Ash','Nutrient Data Bank Number','1st Household Weight','2nd Household Weight'], axis=1, inplace=True)

    return df

def database_details(df):
    rows = len(df.axes[0])
    cols = len(df.axes[1])
    print("Number of Rows: ", rows)
    print("Number of Columns: ", cols)

def get_columns_names(df):
    columns = df.axes[1]
    print(columns)
    print('\n')
    
