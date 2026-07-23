print(" CALCULADORA MATEMATICA")
print(" 1. Suma")
print(" 2. Resta")
print(" 3. Multiplicacion")
print(" 4. Division")
print(" 5. Modulo (Residuo)")
print(" 6. Potencia")
print(" 7. Expresion libre (Ej: 5 + 7 * 2)")

opcion = 0

while opcion not in (1, 2, 3, 4, 5, 6, 7):
    opcion = int(input("Digite opcion (1-7) para elegir la operacion: "))
    if opcion not in (1, 2, 3, 4, 5, 6, 7):
        print("Opción inválida. Intente de nuevo.\n")

resultado = None

if opcion == 7:
    expresion = input("Digite la expresion matematica: ")
    try:
        resultado = eval(expresion)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except SyntaxError:
        print("Error: Expresion mal escrita.")
else:
    num1 = float(input("Digite el primer numero: "))
    num2 = float(input("Digite el segundo numero: "))

    while (opcion in (4, 5)) and num2 == 0:
        print("Error: No se puede realizar la operación con cero como segundo número.")
        num2 = float(input("Digite el segundo numero (diferente de 0): "))

    if opcion == 1:
        resultado = num1 + num2
    elif opcion == 2:
        resultado = num1 - num2
    elif opcion == 3:
        resultado = num1 * num2
    elif opcion == 4:
        resultado = num1 / num2
    elif opcion == 5:
        resultado = num1 % num2  
    elif opcion == 6:
        resultado = num1 ** num2 

if resultado is not None:
    print(f"\nEl resultado de la operacion es: {resultado}")