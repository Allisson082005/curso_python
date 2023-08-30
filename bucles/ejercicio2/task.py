num=int(input("Introduce un número entero positivo:"))
#num_imp=[str(i) for i in range(1, num+1) if i % 2 !=0]
#r=", ". join(num_imp)
#print(r)
for i in range(1, num + 1,2):
    print(i, end=", ")