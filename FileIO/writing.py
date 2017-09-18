cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

# in write mode, the file will be created if it doesn't already exist
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

# strip can be used on strings to strip out data from beginning or end of a string.
# in this case, the newline
# cities = []
# with open("cities.txt", 'r')as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))
#
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "imelda may", "2011", (
#     (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# with open("imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

with open("imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

# using eval is dangerous, as it can change things
imelda = eval(contents)
#print(imelda)

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)
