#invi*(1+4/100)**100*
# 1
invi=float(input("Introduce la inversión inicial:"))
balance1=round(invi*(1+0.04),2)
balance2=round(balance1*(1+0.04),2)
balance3=round(balance2*(1+0.04),2)
print("Balance tras el primer año:", round(balance1, 2))
print("Balance tras el segundo año:", round(balance2, 2))
print("Balance tras el tercer año:", round(balance3, 2))