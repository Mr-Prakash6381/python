def div(x,y):
    try:
        res=x/y
    except:
        print('The number is divided by zero')
    finally:
        print('This block is always executed')
div(4,4)
