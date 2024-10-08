""" def sum(a,b):
    return (a+b)

try:
    a = int(input('Ingrese el primer numero: '))
    b = int(input('Ingrese el segundo numero: '))
   
except:
    print('Debe ingresar un valor númerico')
    exit()

print(f'La Suma de {a} y {b} es {sum(a,b)}')
 """


""" def sum(a, b):
    return a + b


def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('Debe ingresar un valor numérico')

# Pedimos el primer número
a = pedir_numero('Ingrese el primer numero: ')

# Pedimos el segundo número
b = pedir_numero('Ingrese el segundo numero: ')

# Imprimimos la suma
print(f'La suma de {a} y {b} es {sum(a, b)}')
 """


def sum(a,b):
    return (a+b)

control = True
a = None
b = None

while control:
    try:
        if a == None:
            a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))

        control = False

    except:
        print("Debe ingresar un valor numerico")


print(f'La suma de {a} y {b} es {sum(a, b)}')
