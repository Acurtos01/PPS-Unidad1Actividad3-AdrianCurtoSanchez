#!/usr/bin/env python
# coding: utf-8

# # Calculadora en Python

# Comenzamos creando las funciones básicas:
# - suma: Suma de dos números.
# - resta: Resta de dos números
# - multiplicacion: Multiplicación de dos números.
# - division: División de dos números.
# - isNumber: Indica si el argumento introducido es un número o no.
# - mayorCero: indica si el número pasado es mayor que cero.
# 

# In[1]:


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def is_number(a):
    return isinstance(a, (int, float, complex))

def mayor_cero(a):
    return (a > 0)
    


# Creamos la función principal del programa llamada `calculadora` la cual contendrá la lógica princiapal de ejecución.

# In[2]:


import sys

def calculadora():
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("0. Salir")

    while True:
        operacion = input("Ingrese el número de la operación (0/1/2/3/4): ")
    
        if operacion in ['0', '1', '2', '3', '4']:

            if operacion == '0':
                print("Cerrando calculadora...")
                sys.exit(0)
            
            while True:
                num1 = float(input("Ingrese el primer número: "))
                if not is_number(num1):
                    print("Por favor ingrese un número")
                else:
                    break
    
            while True:
                num2 = float(input("Ingrese el segundo número: "))
                if not is_number(num2):
                    print("Por favor ingrese un número")
                elif operacion=='4' and not mayor_cero(num2):
                        print(num1, "no es divisible entre 0")
                else:
                    break
    
            if operacion == '1':
                print("Resultado:", suma(num1, num2))
            elif operacion == '2':
                print("Resultado:", resta(num1, num2))
            elif operacion == '3':
                print("Resultado:", multiplicacion(num1, num2))
            elif operacion == '4':
                print("Resultado:", division(num1, num2))
        else:
            print("Operación no válida")

if __name__ == "__main__":
    calculadora()


# Aunque indique que se ha producido una excepción, emplear `sys.exit(0)` es la forma correcta de indicar que el programa ha finalizado de forma correcta.
