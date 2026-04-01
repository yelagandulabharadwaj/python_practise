

'''
def greet(name):
    print("hello ",name)

print('regular ')
greet('Bharadwaj')
'''


def my_dec(funct_name):
    def wrapper(name):
        print('before execution')
        funct_name(name)
        print('after exec')
    return wrapper

@my_dec
def greet(name):
    print("hello ",name)

greet('Bharat')