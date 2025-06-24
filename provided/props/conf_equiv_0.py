
from dnnv.properties import *
import numpy as np

N1 = Network("N1")
N2 = Network("N2")

epsilon = Parameter("epsilon", type=float, default=0.01)
xc = np.zeros((1,16))

# your code here ...
