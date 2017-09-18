my_direction = {1: {"W": "I want to go west",
                    "S": "I want to go south"},
                2: {"N": "I want to go north",
                    "E": "I want to go east"}}
print(my_direction[2]["N"])  # 2 is key for the first dictionary, "N" is the key for the sub dictionary
