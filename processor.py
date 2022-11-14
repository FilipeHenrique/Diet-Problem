def minimize_calories_objective_function(df):
    z = df["Data.Kilocalories"].array
    return z

def solve(z,A_ub,b_ub,bounds):
    sol =sco.linprog(z,A_ub=Aub,b_ub=bub,bounds=[bounds],method='simplex')
    print(sol)
    return sol