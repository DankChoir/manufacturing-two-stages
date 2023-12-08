from gamspy import Model, Variable

import numpy as np
from numpy import array


def printOptimal(model: Model, result: Variable):
    print(f"> Optimal Result: {-model.objective_value}")

    print("> Parts Ordered [x]")
    print(result.records)


def printScenerioResult(demand: array, y: Variable, z: Variable, order: int):
    print(f"\n==== Scenerio {order} ============================\n")

    print("> Demand: ", end="")
    print(demand)

    print(f"\n> Parts Left Over [y{order}]")
    print(y.records)

    print(f"\n> Products Manufacured [z{order}]")
    print(z.records)


def randomDemand(element: int):
    # Number of trials and probability of success
    n_trials = 10
    p_success = 0.5

    # Number of elements in the vector
    n_elements = element

    # Generate the random demand vector
    return np.random.binomial(n_trials, p_success, n_elements)
