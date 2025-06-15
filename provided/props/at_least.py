from dnnv.properties import *
import numpy as np

# We want to speficy a property for the network called N
N = Network("N")

# The lower-bound of inputs is defined as follows:
lb = np.array([-2., -2.])

# The upper-bound of inputs is defined as follows:
ub = np.array([2., 2.])

# For all inputs x we want that...
Forall(x,
    Implies(
        # IF x is within the bounds [lb, ub]
        lb <= x <= ub,
        # THEN the output of the network N is greater than or equal to 1
        N(x) >= 0.9
    )
)