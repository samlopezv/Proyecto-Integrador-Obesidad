def grafica_mundo():
    xpaises=[]
    y2sex=[]
    dato=[]

    with open ('/workspace/Proyecto-Integrador-Obesidad/assignments/00Archivos/data/Obesidad en el mundo.csv', 'r') as mundo:
       #Gráfica mundo 2016 2 sexos
        for line in mundo:
            dato = line.split(',')
            xpaises.append(dato[0])
            y2sex.append(dato[1])

    print('\n')
    print('Salir Enter')
    return()

def grafica_mexico():
    xregion=[]
    ysobrepeso=[]
    yobesidad=[]
    dato=[]

    with open ('/workspace/Proyecto-Integrador-Obesidad/assignments/00Archivos/data/Obesidad en méxico.csv', 'r') as mexico:
        for line in mexico:
            dato = line.split(',')
            xregion.append(dato[0])
            ysobrepeso.append(dato[1])
            yobesidad.append(dato[2])


def graficas(nombre,num):
    print('¿Qué gráfica deseas conocer?')
    print('Mundo=1     México=2      Salir=3')
    num = int(input())

    while num != 3:
        if num == 1:
            varmundo = grafica_mundo()
            print('Gráfica México=2     Salir =3')
            num=int(input())

        elif num == 2:
            g = graficas()
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





def imc(nombre, num):
    print('\n')
    print('Calculadora de IMC')
    peso = float(input('Ingresa tu peso en kg: '))
    estatura = float(input('Ingresa tu estatura en metros: '))
    imc = round(peso/ estatura**2,1)
    print(f'{nombre} tu IMC es de {imc}')


    #Tipos de peso
    if imc < 18.5 :
        a=[]
        print('Lo que significa que tienes un bajo peso')

        #Comidas
        print("Opciones de comidas: ")
        a = [['       ','Lunes','Martes','Miercoles','Viernes'],
        ['Desayuno','Huevos con jamón','colache','Calabazas a la mexica','Yogurt sin azucar con fruta'],
        ['Comida  ','Caldo de pollo','Ceviche','Carne con verduras','Caldo de res','ensalda de atún'],
        ['Cena','Tacos de queso fresco','Avena','sandwinch de jamón','Rollitos de primavera','frijol con queso']]
        print (a)


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
            g = graficas(nombre,num)
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
