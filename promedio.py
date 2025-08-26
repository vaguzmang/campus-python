import os
os.system("clear")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print("Ahora, ingrese dos notas para calcular el promedio.")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
print(f"{nombre} su promedio es {(nota1+nota2)/2}")
promedio=(nota1+nota2)/2
if promedio >=4.5:
    print(f"{nombre} felicitaciones haz aprobado la materia")
elif promedio >=3.5:
    print(f"{nombre} haz aprobado la materia")
else:
    print(f"{nombre} lo sentimos haz perdido la materia")