#Brincando com listas

numbers1 = [ 0, 2, 4, 6]
numbers2 = [ 10, 12, 14, 16]

#Colocando uma lista dentro de uma lista
mix = [1, 4, "5", 6.3, [1, 2, 3]]

#Concatenando duas listas
print(numbers1 + numbers2) 

#imprimindo um ídice específico dentro de uma lista
print(numbers1[2])

#imprimindo uma sequencia de indices
print(numbers1[0:3])

#imprimindo uma lista dentro de outra lista
print(mix[4])

#imprimindo um valor especifico de uma lista que está dentro de outra
print(mix[4][2])

# add um número ao fim de uma lista
mix.append(9)
print(mix)

mix.append(9)
print(mix)

#removendo um número de uma lista
mix.remove(9)
print(mix) # Removeu o 9

#removendo pelo indice
del(mix[4])
print(mix)



