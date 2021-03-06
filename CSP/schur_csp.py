from pycsp3 import *
import os
import subprocess

if len(sys.argv) < 3:
    print("Usage: python3 schur_csp.py [k = nombre de boites] [n = nombre de balles]")
    exit(0)

k = int(sys.argv[1])
n = int(sys.argv[2])
variables = VarArray(size=n+1, dom=range(k))
# print("k = ", k, "\tn = ", n, "\n")

satisfy(
    (variables[i] != variables[j]) | (variables[i] != variables[l]) | (variables[j] != variables[l])
    for i in range(n - 2) for j in range(i + 1, n - 1) for l in range(j + 1, n) if (i + 1) + (j + 1) == (l + 1)
)

command = "mv schur_csp.xml " + "k_" + str(k) + "/" + str(k) + "_" + str(n) + "_model"
print(command)
os.system(command)

