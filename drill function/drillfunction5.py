def summation(num):
    count = 1
    somme = 0
    while(count <= num):
        somme += count
        count = count+1
    print(somme)

summation(8)
summation(2)

def count_sheep(n):
    count = 1
    while(count <= n):
        print('{}....sheep'.format(count))
        count += 1

count_sheep(3)