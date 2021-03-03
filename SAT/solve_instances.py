import subprocess
import time
from matplotlib import pyplot as plt

n3 = [20, 23, 24, 43, 60, 100]
n4 = [60, 66, 67, 100]
n5 = [140, 150, 160, 170, 171]
n_tab = [n3, n4, n5]
time_values = [[], [], []]
sat_values = [[], [], []]

for k in range(3, 4):
    k_offset = k-3
    for n in n_tab[k-3]:
        model_path = "k_"+str(k)+"/"+str(k)+"_"+str(n)+"_model"
        result_path = "k_"+str(k)+"/"+str(k)+"_"+str(n)+"_result"
        start_time = time.time()
        subprocess.Popen(['minisat', model_path, result_path]).wait()
        end_time = time.time()
        time_values[k_offset].append(end_time - start_time)

plt.plot(n_tab[0], time_values[0])
plt.scatter(n_tab[0], time_values[0])
plt.show()