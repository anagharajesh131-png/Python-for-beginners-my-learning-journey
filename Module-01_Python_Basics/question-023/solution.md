x = float(input("Enter initial value:"))
tolerance = float(input("Enter the tolerance : "))
max_iterations = int(input("Enter maximum iterations: "))

count = 0

while count < max_iterations:

    new_x = 0.5 * x + 1

    print(f" Iteration {count + 1}:  {new_x: .6f}")

    if abs(new_x - x) < tolerance:
        break

    x = new_x
    count += 1

print(f"Converged value = {new_x:.6f}")
