import sys

output_path = sys.argv[1]

res = ""
assign = ""
for line in sys.stdin:
    if line[0] == 's':
        res = line.split(" ")[1]
    elif len(line.split(" ")) > 1:
        if "<values>" in line.split(" ")[1]:
            i = 2
            while "</values>" not in line.split(" ")[i]:
                assign += line.split(" ")[i] + " "
                i += 1
assign = assign[:-1]

output = open(output_path, "w")
print("assignation:\t", assign)

