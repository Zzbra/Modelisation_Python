import subprocess

n3 = [20, 23, 24, 43, 60, 100]
n4 = [60, 66, 67, 100]
n5 = [140, 150, 160, 170, 171]
n_tab = [n3, n4, n5]

for k in range(3, 6):
    k_offset = k-3
    for n in n_tab[k_offset]:
        command = "schur_csp.py " + str(k) + " " + str(n)
        destination_path = "k_" + str(k) + "/" + str(k) + "_" + str(n) + "_model"
        p = subprocess.Popen(['python3', 'schur_csp.py', str(k), str(n)]).wait()
        # p = subprocess.Popen(['mv', 'schur_csp.xml', destination_path]).wait()
