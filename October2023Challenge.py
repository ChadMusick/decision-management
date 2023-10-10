from constraint import Problem, ExactSumConstraint

denom = [1, 2, 5, 10, 20, 50, 100]
target = 100

problem = Problem()
for i in denom:
	problem.addVariable(str(i), [X * i for X in range((target // i) + 1)])
problem.addConstraint(ExactSumConstraint(target))
print(len(problem.getSolutions()))
