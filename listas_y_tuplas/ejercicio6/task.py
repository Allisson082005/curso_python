abecedario= ['a', 'b',"c", 'd', 'e', "f", 'g', 'h', "i", 'j', 'k', "l", 'm', 'n', "ñ", 'o', 'p', "q", 'r', 's', "t", 'u', 'v', "w", 'x', 'y', "z"]
abecedario= [x for i,x in enumerate(abecedario) if (i+1)%3 != 0]
print(abecedario)
#lista = [x for i,x in enumerate(lista) if (i+1)%3 != 0]
#print(lista)