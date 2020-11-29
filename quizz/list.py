# 1
a = [1, 3, 2, 7, 4, 10, 46]
# 2
print('{}{}{}'.format(a[0],a[1],a[2]))

# 3
indices = [3,4,5]
b = [a[i] for i in indices]
print(b)

# 4
c = a + b
print(c)

# 5
d = zip(a, b)
print(d)

# 6

a.append(5)
print(a)

# 7
c.append(None)
print(c)
# 8 , 9

def mulitplyList(lst, n = 2):
    count = 1
    while(count <= n):
        lst += lst
        count = count +1
        print(count)
    print(lst)

mulitplyList([1,2,3])
# 10
def whileToNull(lst):
    while lst:
        print(lst.pop(0))
        if int : 
           continue     
        else:
            break
            

whileToNull(c)
# 11
def sumOfList(lst):
    count = 0
    for i in lst:
        if isinstance(i,int):
            count += i
    print(count)

sumOfList(a)

# 12


for element in a:
    if element %2 == 0:
        print(element)


def firstLetter(str):
    print(str[0])

firstLetter('Becode')

