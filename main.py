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
z, bounds = minimize_calories_objective_function(df)

# solve
result = solve(z,A_ub,b_ub,bounds).x
print(len(result))
# for index,element in enumerate(result):



