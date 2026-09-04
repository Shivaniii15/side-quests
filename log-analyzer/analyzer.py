with open("Apache_2k.log", "r") as file:
    for line in file:
        if "[error]" in line:
            print(line)