def myFun(*kwargs):
    """
    This function takes in any number of keyword arguments and prints the sum of the first two arguments.

    Parameters:
    *args: Any number of keyword arguments.

    Returns:
    None
    """
    print(kwargs[0]+kwargs[1])


myFun(1, 2, 3, 4)


def myFun2(a=100, b=200):
    print(a+b)


myFun2()
myFun2(a=10, b=20)
