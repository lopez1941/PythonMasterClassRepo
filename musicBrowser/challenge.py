def build_tuple(*args):
    return args


message_tuple = build_tuple("hello", "planet", "earth")
print(type(message_tuple))
print(message_tuple)