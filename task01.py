# Import the PuLP library for linear programming
import pulp

# Create a linear programming problem with the goal to maximize production
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Define decision variables:
# x = number of lemonades to produce (must be an integer ≥ 0)
# y = number of fruit juices to produce (must be an integer ≥ 0)
x = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
y = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Objective function: maximize the total number of drinks (lemonade + fruit juice)
model += x + y, "Total_Production"

# Add constraints based on resource availability:

# Water constraint: 2 units per lemonade, 1 unit per fruit juice
model += 2*x + 1*y <= 100, "Water_Constraint"

# Sugar constraint: 1 unit per lemonade
model += x <= 50, "Sugar_Constraint"

# Lemon juice constraint: 1 unit per lemonade
model += x <= 30, "Lemon_Juice_Constraint"

# Fruit puree constraint: 2 units per fruit juice
model += 2*y <= 40, "Fruit_Puree_Constraint"

# Solve the problem
model.solve()

# Output the results
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonades to produce: {int(x.varValue)}")
print(f"Fruit juices to produce: {int(y.varValue)}")
print(f"Total drinks: {int(pulp.value(model.objective))}")
