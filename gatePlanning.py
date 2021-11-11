from gurobipy import Model,GRB,LinExpr
import numpy as np
from variable_loader import *
import math

def create_variables(model, flights, gates):

	num_flights = len(flights["passengers"])
	num_gates = len(gates["distance"])

	variables = list(list(i) for i in np.zeros((num_flights,num_gates)))
	coeff = np.zeros((num_flights,num_gates))
	for i in range(num_flights):
		num_pax = flights["passengers"][i]
		for j in range(num_gates):
			distance = gates["distance"][j]
			var_name = 'x' + str(i) + str(j)
			coeff[i,j] = distance * num_pax / 10000
			variables[i][j] = model.addVar(lb=0, ub=1, vtype=GRB.BINARY,name=var_name)

	return variables, coeff

def create_objective(model, variables, coeff):
	model.setObjective(np.dot(np.array(variables).flatten(),coeff.flatten()), GRB.MINIMIZE)


# def create_constraints(model, flights, gates, variables):
# 	num_flights = len(flights["passengers"])
# 	num_gates = len(gates["distance"])

# 	for i in range(num_flights):
# 		model.addConstr(sum(variables[i]) == 1)

# 	for j in range(num_gates):
# 		model.addConstr(sum(row[j] for row in variables) <= 1)

def create_constraints(model, flights, gates, variables):
	num_flights = len(flights["passengers"])
	num_gates = len(gates["distance"])

	# flight constraints
	for i in range(num_flights):
		vars_to_add_f = []
		for j in range(num_gates):
			if flights["category"][i] == gates["category"][j]:
				vars_to_add_f.append(variables[i][j])
		model.addConstr(sum(vars_to_add_f) == 1)

	# gate constraints - including compatibility
	print(f'vars = {variables}')
	for j in range(num_gates):
		vars_to_add = []
		for k in range(num_flights):
			if flights["category"][k] == gates["category"][j]:
				vars_to_add.append(variables[k][j])
		print(f"varstoadd = {vars_to_add}")
		model.addConstr(sum(vars_to_add) <= 1)


flights, gates = create_dict("dataset_flights.csv", "dataset_gates.csv")
model = Model()
variables, coeff = create_variables(model, flights, gates)
model.update()
create_objective(model, variables, coeff)
create_constraints(model, flights, gates, variables)
model.update()
model.write("LP_problem.lp")
model.optimize()




# Print optimal Solution

for var in model.getVars():
	print(f"{var.VarName} = {var.X}")