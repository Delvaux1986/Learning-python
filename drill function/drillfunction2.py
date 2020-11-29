def isDivisible(n , y , x):
    if(n % y == 0 and n % x == 0):
        print("True car {} est divisible par {} et {}".format(n,y,x))
    else:
        print('False car {} n\'est pas divisible par {} et {}'.format(n,y,x))     


isDivisible(12,6,2)
isDivisible(9,6,2)
isDivisible(24,6,2)

def abbrevName(name):
    array = name.split()
    print('Bonjour {} {}'.format(array[0][0],array[1][0]))
    

abbrevName('Robby Delvaux')
abbrevName('Alain Delon')
abbrevName('Phillip Morris')