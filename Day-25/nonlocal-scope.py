def a():
    msg="Hi"
    def b():
        nonlocal msg
        msg="Hello"
        print(msg)
    b()
    print(msg)

a()
