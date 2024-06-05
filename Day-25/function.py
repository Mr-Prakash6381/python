def a():
    msg="I am is outer function"
    def b():
        print(msg)
    b()
a()
