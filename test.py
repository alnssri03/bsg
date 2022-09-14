!pip install numpy
import numpy as np

t1=(100,200)
t2=(300,100)

dist = np.linalg.norm(t1 - t2)
print(dist)