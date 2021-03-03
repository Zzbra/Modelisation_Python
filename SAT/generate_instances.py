import subprocess

n3 = [20, 23, 24, 43, 60, 100]
n4 = [60, 66, 67, 100]
n5 = [140, 150, 160, 170, 171]
n_tab = [n3, n4, n5]
for k in range(3, 6):
    for n in n_tab[k-3]:
        output_string = "k_3 + str(k) + "/" + str(k) + "_" + str(n) + "_model"
        subprocess.Popen(['python3', "sat.py", str(k), str(n), output_string]).wait()

