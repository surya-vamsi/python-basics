globavar = 10
def read():
    print(globavar)
def write1():
    global globavar
    globavar = 1
def write2():
    globavar = 2
read()
write1()
read()
write2()
read()
