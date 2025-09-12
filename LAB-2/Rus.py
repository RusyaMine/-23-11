# 16-Variant
# A=[1,2,4,5,-7,-32,6,2,-12,64]
# sq=[x**2 for x in A if x>0]
# if sq:
#     b=sum(sq)/len(sq)
#     print("sq =",sq)
#     print("b =",b)
# else:
#     print("Element jok")

import random
A=[[random.randint(0,9) for i in range(4)] for i in range(4)]
print("massiv:")
for b in A:
    print(b)
s=sum(A[i][j] for i in range(4) for j in range(4) if A[i][j]<5)
print("summa:",s)