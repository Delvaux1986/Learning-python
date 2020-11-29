# 1
dico = dict(Brand = 'Ford', model = 'Mustang', year = 1964)
# 2
print(dico['year'])
# 3
def displayKey(dic):
    for x in dic:
        print(x)

displayKey(dico)

# 4
def displayValue(dic):
    for i in dic:
        print(dic[i])

displayValue(dico)
# 5
def displayAll(dico):
    index = 1
    for x,y in dico.items():
        print(index,x,y)
        index += 1

displayAll(dico)