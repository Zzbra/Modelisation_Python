import subprocess
import time

n3 = [20, 23, 24, 43, 60, 100]
n4 = [60, 66, 67, 100]
n5 = [140, 150, 160, 170, 171]
n_tab = [n3, n4, n5]
time_values = [[], [], []]
sat_values = [[], [], []]

for k in range(3, 6):
    for n in n_tab[k-3]:
        subprocess.Popen(['python3', "sat.py", str(k), str(n), output_string]).wait()
