
from enemy import Troll, Vampire

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

# will fail
# monster = Enemy("Basic enemy")
# monster.grunt()
ugly_troll.take_damage(12)

marty = Vampire("Marty")
marty.take_damage(10)
print(marty)

print("-" * 40)
ugly_troll.take_damage(30)
print(ugly_troll)

# while marty.alive:
#     marty.take_damage(1)
#     print(marty)

marty._lives = 0
marty._hit_points = 1
print(marty)