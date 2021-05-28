#Parâmetros nomeados e return

def calculator(x=10, y=15):
    return x-y
    
result = calculator(5)
print("O resultado é {}!".format(result))