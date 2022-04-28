# *args, **kwargs

def sumuj(*args):
    return sum(args)


sumuj(1, 2)
sumuj(1, 2, 3)
print(sumuj(1, 2, 3, 4))
sumuj(1, 2, 3, 4, 10)

# [1, 3, 5, 7, 9]
# [2, 4, 6, 8, 10]
# [1,2,3,4,5,6,7,8,9,10]

def get_interleaved(**kwargs):
    print(kwargs['nieparzyste'])
    print(kwargs['parzyste'])

get_interleaved(nieparzyste=[1, 3, 5, 7, 9], parzyste=[2,4,6,8,10])

def construct(**kwargs):
    print(kwargs['age'])
    print(kwargs['name'])
    print(kwargs['surname'])

construct(age=10, name='Jan', surname='Nowak')