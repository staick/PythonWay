from pkg_resources import EGG_DIST


def spam():
    global eggs
    eggs = "spam"

def bacon():
    eggs = "bacon"

def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)