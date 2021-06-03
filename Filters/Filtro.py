import re

with open("Monogenic_2.variant_function", "r") as file, open("Monogenic_2.variant_function_new","a+") as output: 
    file = file.readlines()
    regexp = re.compile("Isolated cases")
    regexp2 = re.compile("Multifactorial")
    for line in file:
        match = regexp.search(line)
        match2 = regexp2.search(line)
        if match or match2:
            continue
        else:
            output.write(line)

