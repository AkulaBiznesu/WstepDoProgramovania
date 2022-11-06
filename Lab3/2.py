#𝑦=2𝑥2−5𝑥−8, dla 𝑥∈[−4,4], z krokiem 0.5.
import numpy as np
for x in np.arange(-4, 4, 0.5):
    y = 2*x**2-5*x-8
    print(y)