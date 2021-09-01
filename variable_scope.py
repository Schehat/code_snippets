# LEGB: Local, Enclosing, Global, Built-in

x = "global x"


def outer():
    # global x to change global x here
    x = "enclosing x"

    def inner():
        # nonlocal x to change enclosing x here
        x = "local x"
        print(x)

    inner()
    print(x)


print(x)
outer()
