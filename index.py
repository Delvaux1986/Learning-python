import re



name = "Alan turing"
age = 42 
person = [ name , age , "mathématicien"]
text = "Hello, my name is {},and i am {} old and i am {}".format(person[0], person[1], person[2])

age += 10

divAge = age / 7

students =  ["Merouane", "Baptiste", "Caroline", "Joe", "Sophie", "Nathan", "Raphaël", "Axel", "Mathieu", "Adrien"]
studen = None
for x in students:
    studen = x
    if("M" in studen):
        print(x)
        print("first exo")


for y in range(0,10):
    print(y)
    if(y == 5):
        continue