from email.policy import compat32
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.arange(10)
print(x)


cat1 = [i for i in range(10)]
cat2 = [i for i in range(9, 0, -1)]

plt.bar(x -0.2, cat1)
plt.bar(x +0.2, cat2)

plt.show()