import subprocess
from functions import parse_output

proc = subprocess.Popen(['python3', 'schur_csp.py', '3', '15', '-solver=[choco,v]'], stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
output = parse_output(proc.communicate()[0])
max_value = max(output)
return_tab = [[]]
for i in range(max_value):
    return_tab.append([])
for i in range(len(output)):
    return_tab[output[i]].append(i)

print("")
for i in range(max_value + 1):
    print("Dans la boite n:", i + 1, "il y a les balles:")
    balles = ""
    for j in range(len(return_tab[i])):
        balles += str(return_tab[i][j] + 1) + " "
    print(balles)
