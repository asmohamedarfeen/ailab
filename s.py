from numpy import asarray, exp
from numpy.random import randn, rand, seed
from matplotlib import pyplot


# Define objective function
def objective(step):
    return step[0] ** 2.0


# Define simulated annealing algorithm
def sa(objective, area, iterations, step_size, temperature):

    # Create initial point
    current = area[:, 0] + rand(len(area)) * (area[:, 1] - area[:, 0])
    current_eval = objective(current)

    # Best solution found
    best, best_eval = current, current_eval

    outputs = []

    for i in range(iterations):

        # Generate candidate solution
        candidate = current + randn(len(area)) * step_size
        candidate_eval = objective(candidate)

        # Difference in evaluation
        difference = candidate_eval - current_eval

        # Temperature schedule
        t = temperature / float(i + 1)

        # Metropolis Acceptance Criterion
        mac = exp(-difference / t)

        # Accept or reject the candidate
        if difference < 0 or rand() < mac:
            current, current_eval = candidate, candidate_eval

        # Update best solution
        if current_eval < best_eval:
            best, best_eval = current, current_eval

        outputs.append(best_eval)

        print(
            f"Iteration {i:4d} | "
            f"MAC = {mac:.5f} | "
            f"Best Solution = {best} | "
            f"Best Eval = {best_eval:.5f}"
        )

    return best, best_eval, outputs


# Seed for reproducibility
seed(1)

# Define search space
area = asarray([[-6.0, 6.0]])

# Initial temperature
temperature = 12

# Number of iterations
iterations = 1200

# Step size
step_size = 0.1

# Run simulated annealing
best_point, best_value, outputs = sa(
    objective, area, iterations, step_size, temperature
)

# Plot results
pyplot.plot(outputs, 'ro-')
pyplot.xlabel('Iteration')
pyplot.ylabel('Best Objective Function Value')
pyplot.title('Simulated Annealing Optimization')
pyplot.show()
