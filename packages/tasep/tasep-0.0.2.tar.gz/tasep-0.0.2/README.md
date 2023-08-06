# example:

This is just a proof of concept package.
Please do not use unless instucted by author.

```python
import tasep # import this awesome module
from matplotlib import pyplot as plt # for ploting.


N = 1000 # size of the tasep

t = tasep.Tasep(N) # create the tasep
r = tasep.RandState() # This provides random numbers for tasep.

# normal tasep
#rho = t.evolve(alpha=0.8, beta=0.8, mc_step=10000000, rand=r)

# lk_tasep
# simulate
rho = t.lk_evolve(alpha=0.4, beta=0.4, Omega_a=0.3, Omega_d=0.3,
                  mc_step=1000000, rand=r)

# plot the density.
plt.plot(rho)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()
```
