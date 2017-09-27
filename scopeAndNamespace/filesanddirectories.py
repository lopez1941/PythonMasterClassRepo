import os
# from documentation: For each directory in the directory tree rooted at top (including top
# itself, but excluding '.' and '..'), yields a 3-tuple: dirpath, dirnames, filenames
# nonlocal tells python to look for the variable in the enclosing scopes
# nonlocal won't check global namespace
# nonlocal can't be used to create a new variable
# scope- modules, functions, and classes are the only things that can create scope
# when creating a function, python creates a new scope for that function


def list_directories(s):

    def dir_list(d):
        # with python3 you can use 'nonlocal' to use a variable outside you function scope that's not a true global variable
        # tab stop isn't a global var.  it isn't defined at the global level, it's defined inside a function
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print("directory listing of " + s)
        dir_list(s)
    else:
        print(s + " directory name doesn't exist.")


list_directories('.')
