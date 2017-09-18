my_List = ["bob", "brett", "boyd", "billy", "jermaine"]
index = len(my_List)
print("Your list is {0} long: ".format(index))

my_Iter = iter(my_List)

for i in range(0, index):
    print(next(my_Iter))
