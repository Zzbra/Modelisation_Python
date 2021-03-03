import sys

res = ""
assign = ""
for line in sys.stdin:
    if line[0] == 's':
        res = line.split(" ")[1]
    elif len(line.split(" ")) > 1:
        print(line.split(" "))
        if "<values>" in line.split(" ")[1]:
            i = 2
            while "</values>" not in line.split(" ")[i]:
                assign += line.split(" ")[i] + " "
                i += 1
assign = assign[:-1]

print("assignation:\t", assign)

