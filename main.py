from database import *
from restrictions import *
from processor import *

# import and clean database
df = load_df()
clean_df(df)

# get restrictions
restrictions = menu(df)
A_ub = restrictions[0]
b_ub = restrictions[1]

# get objective function
z = minimize_calories_objective_function(df)

# solve
# falta definir o array de bounds
# solve()

