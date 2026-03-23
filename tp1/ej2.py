segundos = int (input("ingrese una cantidad de segundos: "))
horas = segundos // 3600
resto = segundos % 3600

minutos = resto // 60
segundos_final = resto & 60

print("horas: ",horas)
print("minutos: ",minutos)
print("segundos: ",segundos_final)
