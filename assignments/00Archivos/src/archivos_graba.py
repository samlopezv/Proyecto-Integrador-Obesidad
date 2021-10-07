def imc(nombre):
    print('Calculadora de IMC')
    peso = float(input('Ingresa tu peso en kg: '))
    estatura = float(input('Ingresa tu estatura en metros: '))
    imc = round(peso/ estatura**2,1)
    print(f'{nombre} tu IMC es de {imc}')


    #Tipos de peso
    if imc < 18.5 :
        print('Lo que significa que tienes un bajo peso')
    elif imc < 25:
        print('Lo que significa que tienes un peso saludable')
    elif imc < 30:
        print('Lo que significa que tienes sobrepeso')
    elif imc < 35:
        print('Lo que significa que tienes obesidad I')
    elif imc < 40:
        print('Lo que significa que tienes obesidad II')
    elif imc < 50:
        print('Lo que significa que tienes obesidad III')
    else:
        print('Lo que significa que tienes obesidad IV')

def graficas():
    



def main():
    nombre = (input('Ingresa tu nombre: '))
    print(f'¡Hola {nombre}! ¿qué deseas conocer?')
    print('IMC= 1     Gráficas=2     Salir=3')
    num = int(input())
    if num == 1:
        imc(nombre)
        nombre = num
    elif num == 2:
        print('Gráficas')
    elif num == 3:
        print('Gracias por tu visita')
    else:
        #editar para que siga pidiendo y redirija
            print('Favor de ingresar un dato válido')


if __name__=='__main__':
    main()
