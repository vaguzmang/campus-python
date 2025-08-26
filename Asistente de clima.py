print("--- BIENVENIDO A TU ASISTENTE INTELIGENTE DE PLANES ---")
nombre = input("Ingresa tu nombre: \n")
clima = input("Ingresa el estado del clima (soleado, lluvioso, nublado, nevado): \n").lower()
presupuesto = float(input("Ingresa tu presupuesto para el plan: \n"))



if clima == "soleado" and presupuesto <= 50000:
    print(f"Ok {nombre}, con un presupuesto bajo y día soleado, ¡a hacer un picnic en el parque!")

elif (clima == "lluvioso" or clima == "nublado") and presupuesto <= 50000:
    print(f"Ok {nombre}, con un presupuesto bajo y el día así, ¡maratón de películas en casa!")

elif clima == "nevado" and presupuesto <= 50000:
    print(f"Ok {nombre}, con un presupuesto bajo y nevando, ¡a hacer un muñeco de nieve!")
    
elif clima == "soleado" and (presupuesto > 50000 and presupuesto <= 200000):
    print(f"Genial {nombre}, con un presupuesto medio y sol, ¡un día de playa o piscina!")

elif (clima == "lluvioso" or clima == "nublado") and (presupuesto > 50000 and presupuesto <= 200000):
    print(f"Genial {nombre}, con un presupuesto medio y el día así, ¡vamos al cine a ver un estreno!")

elif clima == "nevado" and (presupuesto > 50000 and presupuesto <= 200000):
    print(f"Genial {nombre}, con un presupuesto medio y nevando, ¡una tarde de patinaje sobre hielo!")

elif clima == "soleado" and presupuesto > 200000:
    print(f"¡Excelente, {nombre}! Con un gran presupuesto y sol, ¡un día de deportes acuáticos!")

elif (clima == "lluvioso" or clima == "nublado") and presupuesto > 200000:
    print(f"¡Excelente, {nombre}! Con un gran presupuesto y el día así, ¡tarde de bolos y cena fuera!")

elif clima == "nevado" and presupuesto > 200000:
    print(f"¡Excelente, {nombre}! Con un gran presupuesto y nevando, ¡un día completo de ski en la montaña!")

else:  
    
    print(f"Lo  siento {nombre}, no tengo un plan específico para la combinación de '{clima}' y un presupuesto de {presupuesto}.")