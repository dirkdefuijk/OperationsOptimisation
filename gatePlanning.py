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
			var_name = 'x' + str(i) + '|'+ str(j)
			coeff[i,j] = distance * num_pax / 10000
			variables[i][j] = model.addVar(lb=0, ub=1, vtype=GRB.BINARY,name=var_name)

	return variables, coeff

def create_objective(model, variables, coeff):
	model.setObjective(np.dot(np.array(variables).flatten(),coeff.flatten()), GRB.MINIMIZE)

def create_constraints(model, flights, gates, variables):
	num_flights = len(flights["passengers"])
	num_gates = len(gates["distance"])

	# flight constraints - including gate compatibility
	for i in range(num_flights):
		# Only add flight-gate combination to constraint if compatible.
		vars_to_add_f = []
		for j in range(num_gates):
			if flights["category"][i] == gates["category"][j]:
				vars_to_add_f.append(variables[i][j])
		model.addConstr(sum(vars_to_add_f) == 1)

	# gate constraints - including gate compatibility
	# for j in range(num_gates):
	# 	vars_to_add = []
	# 	for k in range(num_flights):
	# 		if flights["category"][k] == gates["category"][j]:
	# 			vars_to_add.append(variables[k][j])
	# 	print(f"varstoadd = {vars_to_add}")
	# 	model.addConstr(sum(vars_to_add) <= 1)


	# timeslot compatibility
	num_slots = 3
	for timeslot in range(num_slots):
		
		# Find flights that need a gate at timeslot 
		need_a_gate_at_timeslot = []
		for i, timeslot_flight in enumerate(flights['time period']):
			# print(i, timeslot)
			if timeslot_flight == timeslot:
				need_a_gate_at_timeslot.append(i)
		

		print(f"flights that need a gate in time slot {timeslot} = {need_a_gate_at_timeslot}")

		for j in range(num_gates):
			vars_to_add = []
			for k in need_a_gate_at_timeslot:
				if flights["category"][k] == gates["category"][j]:
					vars_to_add.append(variables[k][j])
			print(f"varstoadd = {vars_to_add}")
			if not vars_to_add == []:
				model.addConstr(sum(vars_to_add) <= 1)

flights, gates = create_dict("test_flights.csv", "test_gates.csv")
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
