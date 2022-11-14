import scipy.optimize as sco

def minimize_calories_objective_function(df):
    z = df["Kilocalories"].array
    bounds = [(0,None) for element in z]
    return z,bounds

def solve(z,A_ub,b_ub,bounds):
    sol =sco.linprog(z,A_ub=A_ub,b_ub=b_ub,bounds=bounds,method='simplex')
    return sol