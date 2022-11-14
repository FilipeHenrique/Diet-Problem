from database import *
from processor import *
from processor import *

# import and clean database
df = load_df()
clean_df(df)

# get restrictions


# get objective function
z = minimize_calories_objective_function(df).array

# solve

