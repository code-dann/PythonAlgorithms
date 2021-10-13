#Import

from functools import reduce

def run(func):
    func()


def hello():
    print("Hello there!")

def goodbye():
    print("Bye, see u later.")

run(hello)
run(goodbye)

#Filter

my_list=[1,4,5,6,9,13,19,21]

#odd = [i for i in my_list if i%2 !=0]

odd = list(filter(lambda x: x%2 !=0, my_list))
print(odd)

#MAP

numbers =[1,2,3,4,5]

#double = [ i**2 for i in list ]

square=list(map(lambda i: i**2, numbers))

print(square)


list_two=[2,2,2,2,2]

all_multiplied = reduce(lambda a,b: a*b, list_two)
print(all_multiplied)
