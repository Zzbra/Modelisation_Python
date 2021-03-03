import sys

res = ""
assign = ""
for line in sys.stdin:
    if line[0] == 's':
        res = line.split(" ")[1]
    elif len(line.split(" ")) > 1:
        if line.split(" ")[1] == "\t<values>0":
            i = 2
            while line.split(" ")[i] != "</values>\n":
                assign += line.split(" ")[i] + " "
                i += 1
assign = assign[:-1]

print(assign)

