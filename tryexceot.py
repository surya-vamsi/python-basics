#except,try,raise- are used with exceptions in python.exceptions are basically errors it will show error when something donev wrong.
def reciprocal(num):
    try:
        r = 1/num

    except:
        print('error')
        return
    return r 

print(reciprocal(10))
print(reciprocal(0))
