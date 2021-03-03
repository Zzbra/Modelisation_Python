import os
import time
from matplotlib import pyplot as plt

time_val = [[], [], []]
sat = [[], [], []]
n3 = [20, 23, 24, 43, 60, 100]
n4 = [60, 66, 67, 100]
n5 = [140, 150, 160, 170, 171]
n_tab = [n3, n4, n5]
first_part = 'python3 schur_csp.py '
second_part = ' -solver=[choco,limit=600s,v] | python3 test.py'
start_index = 4

k_offset = start_index - 3
for k in range(start_index, 5):

    for n in n_tab[k_offset]:
        print("n = ", n)
        command = first_part + str(k) + " " + str(n) + second_part
        start = time.time()
        print(command)
        stream = os.popen(command)
        output = stream.read()
        end = time.time()
        time_val[k_offset].append(end - start)
        print(output)
        if len(output.split("\t")[1]) > 2:
            sat[k_offset].append("SAT")
        else:
            sat[k_offset].append("UNSAT")

    # plt.plot(n_tab[k_offset], time_val[k_offset])
    # plt.scatter(n_tab[k - 3], time_val[k - 3])
    # for i in range(len(n_tab[k - 3])):
    #     plt.annotate(sat[k - 3][i] + " n: " + str(n_tab[k - 3][i]), (n_tab[k - 3][i], time_val[k - 3][i] * 1.3 + 0.6))
    # plt.xlabel("Nombre de boules")
    # plt.ylabel("Temps de résolution")
    # plt.title("Temps de résolution en fonction du nombre de boules pour " + str(k) + " paniers")
    # plt.show()

ind = k_offset
print(time_val)
print(sat)
print(n_tab)
plt.plot(n_tab[ind], time_val[ind])
plt.scatter(n_tab[ind], time_val[ind])
for i in range(len(n_tab[ind])):
    plt.annotate(sat[ind][i] + " n: " + str(n_tab[ind][i]), (n_tab[ind][i]-3, time_val[ind][i]*1.3+0.6))
plt.xlabel("Nombre de boules")
plt.ylabel("Temps de résolution en secondes")
plt.title("Temps de résolution en fonction du nombre de boules pour quatre paniers")
plt.show()
