def spam1():

    def spam2():


        def spam3():
            z = " even"
            z += y
            print("in spam 3, locals are {}".format(locals()))
            return z

        y = " more " + x
        y += spam3()
        print("in spam 2, locals are {}".format(locals()))
        return y

    x = " spam"
# x = " spam" + spam2()- fails because x hasn't been defined when spam2 tries to call it
# when possible, try to write functions that only use local var and params
# if you write something in two lines that looks like it could be combined to 1 line, write a comment saying why
# you did it that way so you or others will have a better time when going back to adjust the code
    x += spam2()  # x must exist before spam2 is called, don't combine these two statements
    print("in spam 1, locals are {}".format(locals()))
    return x


print(spam1())
print(locals())
print(globals())

# how python scopes for variables- legb(1. local, 2. enclosing, 3. global, 4. builtins) searches local first, enclosing (vars in
# an enclosing function), global, builtins-(built into the language).


