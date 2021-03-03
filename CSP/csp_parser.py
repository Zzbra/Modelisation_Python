import sys

output_path = sys.argv[1]

res = ""
assign = ""
for line in sys.stdin:
    if line[0] == 's':
        res = line.split(" ")[1]
    elif len(line.split(" ")) > 1:
        if "<values>" in line.split(" ")[1]:
            # Ici line.spli(" ")[1] vaut <values>x avec x l'assignation de la première variable
            # on récupère donc x
            assign += line.split(" ")[1][9] + " "
            i = 2
            while "</values>" not in line.split(" ")[i]:
                assign += line.split(" ")[i] + " "
                i += 1
assign = assign[:-1]
print("assign: ", assign)
output = open(output_path, "w")


i = 0
tab = []
if len(assign) > 0:
    while assign[i+1] != " ":
         i += 1
    while i < len(assign):
        if assign[i] != " ":
            tab.append(int(assign[i]))
        i += 1

    for i in range(max(tab)+1):
        tmp = []
        for j in range(len(tab)):
            if tab[j] == i:
                tmp.append(j+1)

        for l in range(len(tmp)):
            output.write(str(tmp[l]) + " ")
        output.write("\n")
else:
    output.write("UNSAT\n")

output.close()
