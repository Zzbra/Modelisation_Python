
def parse_output(k, n):
    input_file = open("k_" + str(k) + "/" + str(k) + "_" + str(n) + "_result", "r")
    input_file.readline()
    res = input_file.readline()
    print("result", res)
    parser = []
    for i in range(0, len(res)):
        tmp = ""
        if res[i] == " ":
            if i+1 < len(res):
                i += 1
                if res[i] != "-":
                    while res[i] != " " and i+1 < len(res):
                        tmp += res[i]
                        i += 1
                    parser.append(tmp)
    print(parser)
    input_file.close()
    output_file = open("k_" + str(k) + "/" + str(k) + "_" + str(n) + "_parsed_result", "w")
    if len(parser) == 0:
        output_file.write("UNSAT\n")
    else:
        j = 0
        for i in range(1, k+1):
            test = []
            while int(parser[j]) <= i * n and j + 1 < len(parser):
                test.append(int(parser[j])-((i-1)*n))
                j += 1
            output_file.write(str(i) + " : ")
            for l in range(len(test)):
                output_file.write(str(test[l]) + " ")
            output_file.write("\n")
    output_file.close()
