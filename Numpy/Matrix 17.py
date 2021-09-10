# Vector rank
from numpy import array
from numpy.linalg import matrix_rank

# rank
V1 = array([1, 2, 3])
print(V1)
vr1 = matrix_rank(V1)
print(vr1)
# zero rank
v2 = array([0, 0, 0, 0, 0])
print(v2)
vr2 = matrix_rank(v2)
print(vr2)
