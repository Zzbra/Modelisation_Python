import os
import time
from matplotlib import pyplot as plt

time_val = []
sat = []
n_tab = []
n3 = [20, 23, 24, 43, 60, 100]
n4 = [60, 66, 67, 100]
n5 = [140, 150, 160, 170, 171]
n_tab.append(n3)
n_tab.append(n4)
n_tab.append(n5)

first_part = 'python3 schur_csp.py '
second_part = ' -solver=[choco,v] | python3 test.py'
for k in range(3, 6):
    time_val.append([])
    sat.append([])
    for n in n_tab[k - 3]:
        command = first_part + str(k) + " " + str(n) + second_part
        start = time.time()
        stream = os.popen(command)
        output = stream.read()
        end = time.time()
        time_val[k - 3].append(end - start)
        if len(output) > 2:
            sat[k - 3].append("SAT")
        else:
            sat[k - 3].append("UNSAT")

    # print(time_val)
    # print(sat)
    # print(n_tab)
    plt.plot(n_tab[k-3], time_val[k-3])
    plt.scatter(n_tab[k-3], time_val[k-3])
    for i in range(len(n_tab[k-3])):
        plt.annotate(sat[k-3][i] + " n: " + str(n_tab[k-3][i]), (n_tab[k-3][i], time_val[k-3][i] * 1.3 + 0.6))
    plt.xlabel("Nombre de boules")
    plt.ylabel("Temps de résolution")
    plt.title("Temps de résolution en fonction du nombre de boules pour " + str(k) + " paniers")
    plt.show()

