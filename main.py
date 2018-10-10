# Copyright (c) 2018 Noah Dominic Silvio <ndsilvio@gmail.com>
# version 1.0.0

import matplotlib.pyplot as plt
import encoder

# for dev purposes only
print(encoder.rz([1,0,0,1, 0.9]))
print(encoder.nrz([1,0,0,1, 0.9]))
print(encoder.nrzi([0,1,0,1,0,1,1,0,0,1]))
