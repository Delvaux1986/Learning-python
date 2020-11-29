def positive_sum(numbers):
    count = 0
    for x in numbers:
        if x > 0:
            count += x
        else:
            continue
    print(count)


firstArray = [1,-4,7,12]
secondArray = [-7,15,98,-101,-200,1000,-400,610]
positive_sum(firstArray)
positive_sum(secondArray)

testArray = ['5', '0', 9, 3, 2, 1, '9', 6, 7]

def sum_mix(arr):
    count = 0
    for x in arr:
        if str(x):
            count += int(x)
        else:
            count += x
    print(count)

sum_mix(testArray)

    