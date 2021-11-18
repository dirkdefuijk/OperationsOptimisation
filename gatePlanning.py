from gurobipy import Model,GRB,LinExpr
import numpy as np
import math
from variable_loader import *
from flight_gate_maker import no_timeslots


def create_variables(model, flights, gates):

	num_flights = len(flights["passengers"])
	num_gates = len(gates["distance"])

	# variables: list of lists. Fill with gurobi var objects (variables[i][j] = "flight i used gate j").
	variables = list(list(i) for i in np.zeros((num_flights,num_gates)))
	# coeff: matrix with num_flights rows and num_gates columns. Fill with coefficients of obj function.
	coeff = np.zeros((num_flights,num_gates))
	for i in range(num_flights):
		num_pax = flights["passengers"][i]
		for j in range(num_gates):
			distance = gates["distance"][j]
			var_name = 'X' + str(i) + '|'+ str(j)
			coeff[i,j] = distance * num_pax / 10000
			variables[i][j] = model.addVar(lb=0, ub=1, vtype=GRB.BINARY,name=var_name)

	return variables, coeff

def create_objective(model, variables, coeff):
	model.setObjective(np.dot(np.array(variables).flatten(), coeff.flatten()), GRB.MINIMIZE)

threshold = 30

def create_constraints(model, flights, gates, variables):
	num_flights = len(flights["passengers"])
	num_gates = len(gates["distance"])

	# flight constraints - including gate compatibility
	for i in range(num_flights):
		# Only add flight-gate combination to constraint if compatible.
		vars_to_add_f = []
		for j in range(num_gates):
			if flights["category"][i] == gates["category"][j]:
				if flights["VIP"][i] == 1:
					if gates["distance"][j] < threshold:
						vars_to_add_f.append(variables[i][j])
				else:
					vars_to_add_f.append(variables[i][j])

		flight_constr_name = "flight_" + str(i)
		model.addConstr(sum(vars_to_add_f) == 1, flight_constr_name)

	# timeslot compatibility,
	num_slots = 2
	counter = 0
	for timeslot in range(num_slots):

		# Find flights that need a gate at timeslot
		need_a_gate_at_timeslot = []
		for i, timeslot_flight in enumerate(flights['time period']):
			if timeslot_flight == timeslot:
				need_a_gate_at_timeslot.append(i)

		for j in range(num_gates):
			vars_to_add = []
			
			for k in need_a_gate_at_timeslot:
				if flights["category"][k] == gates["category"][j]:
					if flights["VIP"][k] == 1:
						if gates["distance"][j] < threshold:
							vars_to_add.append(variables[k][j])
					else:
						vars_to_add.append(variables[k][j])

			# print(f"varstoadd = {vars_to_add}")
			if not vars_to_add == []:
				gate_constr_name = "gate_" + str(counter)
				model.addConstr(sum(vars_to_add) <= 1, name=gate_constr_name)
				counter += 1


def print_optimal_sol(model):
	try:
		print('\nThe optimal solution: \n')
		for var in model.getVars():
			print(f"{var.VarName} = {var.X}")
	except AttributeError:
		print("\nNo optimal solution: infeasible problem ")

def write_solution(sol_filename, variables, flights):
	with open(sol_filename, 'w') as f:
		for i in range(len(variables)):
			for j in range(len(variables[i])):
				if variables[i][j].X == 1:
					timeslot = flights["time period"][i]
					f.write(f"Aircraft {i} goes to Gate {j}, at timeslot {timeslot} \n")

		obj = model.getObjective()
		f.write(f"\nOptimal Objective value = Total walking distance = {obj.getValue()*10} km")

# Modify first argument to create_dict below to use different dataset.
flights, gates = create_dict("test_datasets/test08/test_flights.csv", "test_datasets/test08/test_gates.csv")
model = Model()
variables, coeff = create_variables(model, flights, gates)
model.update()
create_objective(model, variables, coeff)
create_constraints(model, flights, gates, variables)
model.update()
model.write("test_datasets/test08/LP_problem.lp")
model.optimize()
print_optimal_sol(model)
write_solution("test_datasets/test08/solution.txt", variables, flights)
