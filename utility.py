

def parse_output(output):
    output_strings = str(output).split(" ")
    print(output)
    values = []
    i = 0
    while output_strings[i] != "\\t<values>0":
        i += 1
    i += 1
    while output_strings[i] != "</values>\\nv":
        values.append(int(output_strings[i]))
        i += 1
    return values

