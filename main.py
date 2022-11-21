from database import *
from restrictions import *
from processor import *

# import and clean database
df = load_df()
# print(df.head())
# get_columns_names(df)


df = clean_df(df)
# print(df.head())
# get_columns_names(df)

# get_columns_names(df)

# get restrictions
restrictions = menu(df)
A_ub = restrictions[0]
b_ub = restrictions[1]

# get objective function
z, bounds = minimize_calories_objective_function(df)

# solve
result = solve(z,A_ub,b_ub,bounds).x
df_lines_names = df.Category.values
for index,foodAmmount in enumerate(result):
    if foodAmmount > 0:
        print(df_lines_names[index], foodAmmount)
# for index,element in enumerate(result):



