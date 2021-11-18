from gatePlanning import model
import gurobipy
import seaborn as sb

print("\n\n\n\n\n\n ### Sensitivity Report ###")

var = model.getVars()
cons = model.getConstrs()

#RHS
print("\n\n RHS")
for c in cons:
    print(c.ConstrName,':', c.RHS)

#Slack
print("\n\n Slack")

for c in cons:
    print(c.ConstrName,':', c.Slack)

#Reduced Cost
print("\n\n Reduced Cost")
print(var[0].RC)
