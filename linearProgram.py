import cvxpy as cp

x = cp.Variable()
x2 = cp.Variable()

variableConstraints = x >= 0 
variableConstraints1 = x2 >= 0
woodConstraint = 22*x + 45*x2 <= 5500
steelConstraint = 15*x + 10*x2 <= 2500

constraints = [variableConstraints, variableConstraints1, woodConstraint, steelConstraint]
problem = cp.Problem(cp.Maximize(3*x + 4*x2), constraints)
print(problem.solve())
print(x.value, x2.value)

