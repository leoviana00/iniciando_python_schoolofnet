#Trabalhando com dicionários

cars = {}

cars['corola'] = "red"
cars['fit'] = "green"
cars['320'] = "black"

people = dict(Leonardo='Pai', Thaynara='Mae', AnnaJulia='Filha', PedroVictor='Filho')

family = {
    'LeoViana':'Father',
    'ThayMatos':'Mother',
    'Julia':'Daughter',
    'Pedro':'Son'    
}

print(cars)
print(cars.keys())
print(cars.values())

print(people)
print(people['Leonardo'])
print(family)
print(family.keys())