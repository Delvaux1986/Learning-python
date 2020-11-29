dictionnaire = dict(Beer = 'Biere' , Cola = 'Coca' , Water = 'Eau' , Cofee = 'café' , Milk = 'Lait')

print('Veuillez entrer un nouveau mot dans le dictionnaire ;)')
newEnglishInput = input('En anglais :')
newFrenchInput = input('En Francais :')
dictionnaire[newEnglishInput] = newFrenchInput
print('Voici le nouveau dictionnaire' , dictionnaire)

# Exo 3

universalNumber =  "The_universal_number_is_42"

arrayWord = universalNumber.split('_')

print(arrayWord)

# 555

heroes = {"Superman" : "Clark kent", "Batman" : "Bruce Wayne", "Spiderman" : "Tony Parker"}

heroesNames = heroes.values()
aliasNames = heroes.keys()

print(heroesNames)
print(aliasNames)
heroes['Spiderman'] = 'Peter Parker'
print('Petite erreur rectification du tableau assoc' , heroes)