total = 0
while True:
    precio = float(input("ingrese un precio: "))
    if precio == 0:
        break
    total = total + precio
print("total a pagar: ",total)