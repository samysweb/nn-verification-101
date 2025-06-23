from dnnv.properties import *
import numpy as np

N = Network("N")
epsilon = Parameter("epsilon", type=float, default=1/255)
xc = Image("./provided/images/input0.npy")
#xc = Image("./provided/images/input1.npy")
#xc = Image("./provided/images/input2.npy")
#xc = Image("./provided/images/input7.npy")

Forall(
        x,
        Implies(((xc - epsilon) <= x <= (xc + epsilon)) & (0 <= x <= 1), 
		# index is (0, output_class) and (0, target_class), but DNNV can't take variables in there
		N(x)[(0, 0)] >= N(x)[(0, 1)]
	)
)
