from database import *
from restrictions import *
from processor import *

# import and clean database
df = load_df()
# print(df.head())
# get_columns_names(df)
# database_details(df)


df = clean_df(df)
# print(df.head())
# get_columns_names(df)
# database_details(df)


#get restrictions
# restrictions = menu(df)
restrictions = restrictions_from_file(df)
A_ub = restrictions[0]
b_ub = restrictions[1]

# get objective function
z, bounds = minimize_calories_objective_function(df)

# solve
result = solve(z,A_ub,b_ub,bounds).x
df_lines_names = df.Category.values
for index,foodAmmount in enumerate(result):
    if foodAmmount > 0:
        print(index,df_lines_names[index], round(foodAmmount*10,2))




