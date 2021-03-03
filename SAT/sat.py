import sys
import os
import time

arguments = sys.argv
if len(sys.argv) <4:
    print("Usage: python3 [nombre de paniers] [nombre de balles] [fichier sortie]")
    exit(0)

k = int(arguments[1])
n = int(arguments[2])
output_string = arguments[3]
nb_vars, nb_clauses = k*n, 0
output = open(output_string, "w")
clauses = []

# Clauses: Tous présents
for i in range(n):
    clause = ""
    for j in range(k):
        clause += str((i + j * n) + 1) + " "
    clauses.append(clause)
    nb_clauses += 1


# Clauses: Pas de doublons
for i in range(n):
    for j in range(k):
        clause = ""
        for l in range(k):
            if j != l:
                clause += str(-((i + l * n)+1)) + " "
        clauses.append(clause)
        nb_clauses += 1


# Clauses: Pas de triplets tq: a + b = c dans le même panier
for i in range(1, n):
    for j in range(i+1, n+1):
        if i+j <= n:
            for l in range(k):
                clause = str(-(i + l*n)) + " " + str(-(j + l*n)) + " " + str(-((i+j) + l*n)) + " "
                clauses.append(clause)
                nb_clauses += 1

# On écrit les clauses
output.write("p cnf " + str(nb_vars) + " " + str(nb_clauses) + "\n")
print(len(clauses), nb_clauses)
for i in range(len(clauses)):
    output.write(clauses[i]+"0\n")
output.close()

# stream = os.popen("minisat k_3/3_20_model sat_result.txt")
# output = stream.read()
# stream.close()
# print(output)

