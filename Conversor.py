#Tasas de cambio respecto al Euro (1 EUR = X moneda)

# Códigos Textos
# --------------
Negrita = "\033[1m"
Rojo = "\033[31m"
Verde = "\033[32m"
Amarillo = "\033[33m"
RESET = "\033[0m"
# --------------

# Historial
# --------------
historial = []

try:
    with open("historial.txt", "r", encoding="utf-8") as archivo: #lee el archivo historial.txt y guarda cada línea en la lista historial
        for linea in archivo:
            historial.append(linea.strip())
except FileNotFoundError:
    pass  # Si el archivo no existe, simplemente continuamos con un historial vacío
# --------------

tasas_cambio = { #tasas de cambio respecto al Euro (1 EUR = X moneda)
    "EUR": 1.0, #Euro (MONEDA BASE)
    "USD": 1.08, #Dolar
    "GBP": 0.85, #Libra 
    "JPY": 165.20, #Yen Japones
    "MXN": 21.80, #Peso Mexicano
    "BTC": 0.000012, #Bitcoin
    "CNY": 7.50, #Yuan Chino
    "RUB": 90.00, #Rublo Ruso
    "VES": 24.00, #Bolívar Venezolano
    "AED": 3.90, #Dirham de los Emiratos Árabes Unidos
    "INR": 90.00, #Rupia India
}

nombre_monedas = { # Nombre de las monedas
    "EUR": "(€) Euro",
    "USD": "(US$) Dólar estadounidense",
    "GBP": "(£) Libra esterlina",
    "JPY": "(¥) Yen japonés",
    "MXN": "(MX$) Peso mexicano",
    "BTC": "(₿) Bitcoin",
    "CNY": "(¥) Yuan chino",
    "RUB": "(₽) Rublo ruso",
    "VES": "(Bs.S) Bolívar venezolano",
    "AED": "(د.إ) Dirham de los Emiratos Árabes Unidos",
    "INR": "(₹) Rupia india",
}

def convertir_moneda():

    print(f"{Negrita}Inserte la cantidad a convertir:{RESET}")
    while True: #Si no detecta un número, vuelve a pedir la cantidad
        try:
            cantidad = float(input(f"{Negrita}Cantidad: {RESET}"))
            if cantidad < 0:
                print(f"{Rojo}Por favor, ingrese una cantidad positiva.{RESET}")
                continue
            break
        except ValueError:
            print(f"{Rojo}Entrada no válida. Por favor, ingrese un número.{RESET}")

    print(f"{Negrita}--------------------------------{RESET}")
    #Moneda de origen
    print(f"{Verde}Eliga la moneda de origen:{RESET}")
    for f in tasas_cambio:
        print(f"{Amarillo}{f} {nombre_monedas.get(f, '')}{RESET}")
    while True:#Si no detecta una moneda válida, vuelve a pedir la moneda de origen
        try:
            moneda_origen = input(f"{Negrita}Moneda de origen: {RESET}").upper()
            if moneda_origen in tasas_cambio:
                break
            else:
                print(f"{Rojo}Moneda no válida. Por favor, elige una moneda de la lista.{RESET}")
        except ValueError:
            print(f"{Rojo}Entrada no válida. Por favor, ingrese una moneda de la lista.{RESET}")
        
    print(f"{Negrita}--------------------------------{RESET}")
    #Moneda de destino
    print(f"{Verde}Eliga la moneda de destino:{RESET}")
    for f in tasas_cambio:
        print(f"{Amarillo}{f} {nombre_monedas.get(f, '')}{RESET}")
    while True:
        try:
            moneda_destino = input(f"{Negrita}Moneda de destino: {RESET}").upper()
            if moneda_destino in tasas_cambio:
                break
            else:
                print(f"{Rojo}Moneda no válida. Por favor, elige una moneda de la lista.{RESET}")
        except ValueError:
            print(f"{Rojo}Entrada no válida. Por favor, ingrese una moneda de la lista.{RESET}")

    #Conversión
    cantidad_convertida = (cantidad / tasas_cambio[moneda_origen]) * tasas_cambio[moneda_destino] #Codigo para convertir la cantidad de la moneda de origen a la moneda de destino
    print(f"{Negrita}--------------------------------{RESET}")
    print(f"{Verde}Resultado de la conversión:{RESET}")
    print(f"{Amarillo}{cantidad} {moneda_origen} = {Rojo}{cantidad_convertida:.2f}{Amarillo} {moneda_destino}{RESET}") #El .2f es para limitar el resultado a 2 decimales
    return cantidad_convertida, moneda_destino, cantidad, moneda_origen
def comision(cantidad_convertida, moneda_destino):
    print(f"{Negrita}--------------------------------{RESET}")
    print(f"{Verde}Comisión por conversión:{RESET}")
    while True:
        try:
            comisionañadida = float(input(f"{Negrita}Ingrese la comisión en porcentaje (ej. 2 para 2%): {RESET}"))
            if comisionañadida < 0:
                print(f"{Rojo}Por favor, ingrese un porcentaje positivo.{RESET}")
                continue
            break
        except ValueError:
            print(f"{Rojo}Entrada no válida. Por favor, ingrese un número.{RESET}")

    cantidad_final = cantidad_convertida - (cantidad_convertida * (comisionañadida / 100))
    print(f"{Amarillo}Cantidad final después de aplicar la comisión: {Rojo}{cantidad_final:.2f}{Amarillo} {moneda_destino}{RESET}")
    return cantidad_final, comisionañadida


print(f"{Negrita}{Amarillo}Bienvenido al Conversor de Monedas \n {RESET}")
while True: #Menú principal 
    print(f"{Negrita}Que desea hacer?{RESET}")
    print(f"{Negrita}--------------------------------{RESET}")
    print(f"{Amarillo}1. Convertir moneda{RESET}")
    print(f"{Amarillo}2. Ver historial de conversiones{RESET}")
    print(f"{Amarillo}3. Borrar historial de conversiones{RESET}")
    print(f"{Amarillo}4. Salir{RESET}")
    print(f"{Negrita}--------------------------------{RESET} \n ")

    menu_opcion = input(f"{Negrita}Ingrese el número de la opción deseada: {RESET}").strip()
    if menu_opcion == "1":
        cantidad_convertida, moneda_destino, cantidad, moneda_origen = convertir_moneda() #Convertir moneda
        while True: #Añadir comisión
            print(f"{Negrita}--------------------------------{RESET}")
            print(f"{Verde}¿Desea añadir comisión? (Y/N){RESET}")
            respuesta = input(f"{Negrita}Respuesta: {RESET}").strip().upper()
            if respuesta == "Y":
                cantidad_final, comisionañadida = comision(cantidad_convertida, moneda_destino)
                with open("historial.txt", "a", encoding="utf-8") as archivo: #Guarda la conversión en el historial.txt
                    archivo.write(f"{cantidad} {moneda_origen} = {cantidad_convertida:.2f} {moneda_destino} (Comisión: {comisionañadida:.2f}%) - Cantidad final: {cantidad_final:.2f} {moneda_destino}\n")
                break
            elif respuesta == "N":
                with open("historial.txt", "a", encoding="utf-8") as archivo: #Guarda la conversión en el historial.txt
                    archivo.write(f"{cantidad} {moneda_origen} = {cantidad_convertida:.2f} {moneda_destino} (Comisión: 0.00%) - Cantidad final: {cantidad_convertida:.2f} {moneda_destino}\n")
                break
            else:
                print(f"{Rojo}Entrada no válida. Por favor, ingrese 'Y' o 'N'.{RESET}")
        print(f"{Negrita}--------------------------------{RESET}")      
    elif menu_opcion == "2":
        print(f"{Verde}Mostrando historial de conversiones...{RESET}")
        print(f"{Negrita}--------------------------------{RESET}")
        try:
            with open("historial.txt", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                if not lineas:
                    print(f"{Rojo}No hay conversiones en el historial.{RESET}")
                else:
                    for linea in lineas:
                        print(f"{Amarillo}{linea.strip()}{RESET}")
        except FileNotFoundError:
            print(f"{Rojo}No hay conversiones en el historial.{RESET}")
    elif menu_opcion == "3":
        print(f"{Verde}Borrando historial de conversiones...{RESET}")
        with open("historial.txt", "w", encoding="utf-8") as archivo:
            archivo.write("")  # Borra el contenido del archivo
        print(f"{Verde}Historial borrado correctamente.{RESET}")
   
    elif menu_opcion == "4":
        print(f"{Verde}Gracias por usar el Conversor de Monedas{RESET}")
        break

    else:
        print(f"{Rojo}Opción no válida. Por favor, ingrese 1, 2 o 3.{RESET}")
        print(f"{Negrita}--------------------------------{RESET}")





