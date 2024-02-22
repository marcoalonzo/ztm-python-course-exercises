# Docstrings

def test(a):
    """
    Info : This function tests and prints param a
    :param a:
    :return:
    """

    print(a)


test('!!!')

help(test) #a way to obtain info on what a function does
#print()
print(test.__doc__) #dunder method