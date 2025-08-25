Ingresar gasto:
23.75
Dinero recibido
100

Vuelto

Pesos:
76
Centavos:
25

gasto = float(input("Ingresar gasto:\n"))
recibido = float(input("Dinero recibido\n"))


vuelto = recibido - gasto


pesos = int(vuelto)  
centavos = round((vuelto - pesos) * 100)


print("\nVuelto\n")
print(f"Pesos:\n{pesos}")
print(f"Centavos:\n{centavos}")