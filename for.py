#TRabalhando com for

list1 = [2, 4, 6, 8, 10, 12]
list2 = ["Leonardo", "Thaynara", "Pedro", "Anna"]

for item in list1[0:3]:
    if item >2:
        print("Números maiores que 2: {}".format(item))
        
for name in list2:
    # if not name == "Leonardo": //Possibilidade
    # if name == "Leonardo": //Possibilidade
    # if name == list2[0]: 
    if name == list2[0]:
        print(name)
        
        
    list1.append(name)
    print(list1)
    break