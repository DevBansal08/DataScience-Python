import numpy as np
a = np.arange(12).reshape(3,4)


# for row in a:
#     for cell in row:
#         print(cell)
yb = ""
for yb in np.nditer(a,order="C"):
    print(yb)
for yb in np.nditer(a,order="F"):
    print(yb)