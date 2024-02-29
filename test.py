from nonconvexoptimizationlib import nonconvexfunctions

continuous_obj = nonconvexfunctions.NonconvexFunctions.ContinuousFunctions()
non_continuous_obj = nonconvexfunctions.NonconvexFunctions.NoncontinuousFunctions()
print(continuous_obj.rastrigin([-5.12, 5.12]))
print(non_continuous_obj.rastrigin([-5.12, 5.12]))

# Example: Using the Sphere function
result = continuous_obj.sphere([1, 2])
print(f"Sphere function result: {result}")

# Example: Using the Booth function
result = continuous_obj.booth(1, 3)
print(f"Booth function result: {result}")

# Example: Using the Step function
result = non_continuous_obj.step_fun([0, 0.99, -0.99])
print(f"Step function result: {result}")