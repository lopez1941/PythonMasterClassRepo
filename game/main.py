from player import Player

tim = Player("Tim")

print(tim.name)
print(tim.lives)

tim.lives -= 1
print(tim)

# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)

tim.level += 50
print(tim)

tim.level = 34
print(tim)