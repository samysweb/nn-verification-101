
from dnnv.properties import *
import numpy as np

N1 = Network("N1")
N2 = Network("N2")

epsilon = Parameter("epsilon", type=float, default=0.01)
delta = Parameter("delta", type=float, default=0.9)
idx = 1

L = np.log(delta / (1 - delta))

xc = np.zeros((1,16))

Forall(
        x,
        Implies(
		(xc - epsilon <= x <= xc + epsilon)
		& (N1(x)[0,0] - N1(x)[0,1] >= L)
		& (N1(x)[0,0] - N1(x)[0,2] >= L)
		& (N1(x)[0,0] - N1(x)[0,3] >= L)
		& (N1(x)[0,0] - N1(x)[0,4] >= L),
		# ==> 
		np.argmax(N2(x)) == 0
	)
)
