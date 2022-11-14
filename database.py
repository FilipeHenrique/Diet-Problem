import pandas as pd

def load_df():
    df = pd.read_csv('food.csv')
    clean_df(df)
    return df

def clean_df(df):
    # remove lines with null values
    df.dropna(inplace = True)

    # clean Data. from columns title
    column_headers = df.columns.values.tolist()
    for column_header in column_headers:
        if column_header.startswith("Data."):
            new_header = column_header.split(".",1)[1]
            df.rename(columns={column_header: new_header}, inplace=True)

def get_rows_and_columns(df):
    rows = len(df.axes[0])
    cols = len(df.axes[1])
    print("Number of Rows: ", rows)
    print("Number of Columns: ", cols)

def get_columns_names(df):
    columns = df.axes[1]
    print(columns)
    
