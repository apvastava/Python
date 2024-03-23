username = "Arpit"

def func():
    username = "Srivastava"
    print(username)

print(username)
func()


x = 99
def func2(y):
    z = x + y
    return  z

result = func2(51)
print(result)


a = 99
def func3():
    global a 
    a = 88
func3()
print(a)


b = 99
def func4():
    b = 88
    def func5():
        print(b)
    return func5
myResult = func4()
myResult()


def arpitcoder(num):
    def actual(x):
        return x ** num
    return actual

f = arpitcoder(2)
g = arpitcoder(3)

print(f(3))
print(g(3))