def imc(nombre, num):
    print('\n')
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
    print('\n')
    print('IMC= 1     Gráficas=2     Salir=3')
    numnuevo = int(input())
    return(nombre, numnuevo)
     

def graficas():
    x =[]
    y1=[]
    with open('assignments/00Archivos/data/Obesidad en méxico.csv', 'r') as f:
        for column in f:
            lista_column = column.split(',')
            x.append(lista_column[f])
        print(x)


def main():
    nombre = (input('Ingresa tu nombre: '))
    print('\n')
    print(f'¡Hola {nombre}! ¿qué deseas conocer?')
    print('IMC= 1     Gráficas=2     Salir=3')
    num = int(input())
    while num != 3:
        if num == 1:
            variableimc = imc(nombre, num)
            num = variableimc[1]
        elif num == 2:
            graficas()
        else:
            print('Favor de ingresar un dato válido')
            num = int(input())
            if num != 1 or num !=2 or num !=3:
                num = num
            else:
                num = 4
            while num == 4:
                print('Favor de ingresar un dato válido')
                num = int(input())
        
    print('Gracias por tu visita')



if __name__=='__main__':
    main()
