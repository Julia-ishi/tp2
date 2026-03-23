multiplos = []
otros = []

for i in range (1,101):
    if i % 5 == 0:
        multiplos.append(i)
    else:
        otros.append(i)

print("Múltiplos de 5:", multiplos)
print("Otros números:", otros)