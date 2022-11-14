import pandas as pd
import matplotlib.pyplot as plt

def load_df():
    df = pd.read_csv('food.csv')
    return df

def get_rows_and_columns(df):
    rows = len(df.axes[0])
    cols = len(df.axes[1])
    print("Number of Rows: ", rows)
    print("Number of Columns: ", cols)

def get_columns_names(df):
    columns = df.axes[1]
    print(columns)

def clean_df(df):
    df.dropna(inplace = True)

def plot_df():
    df.plot()
    plt.show()

